import secrets
from datetime import datetime, date, timezone
from decimal import Decimal
from typing import List, Optional, Any  # Dodano Annotated
from typing import Union

from pydantic import ConfigDict
from pydantic import Field, model_validator

from models2.abase import BasicBasic
from models2.enums import InvoiceType, SourceInvoiceSource
from models2.helpers.FlattenMixin import FlattenMixin
from models2.helpers.sale_invoice_adnotacje import AdnotacjeNie, AdnotacjeTak
from models2.xxx.h_enums import CurrencyAB, EuropeLandsEnum, WorldLandsEnum
from models2.xxx.h_files import TransactionFiles
from models2.xxx.h_transaction_types import DataWspolna, RozneDaty, SprzedazOdDo


class CostInvoiceBasic(BasicBasic, FlattenMixin):
    files: List[TransactionFiles] = Field(default_factory=list)

    model_config = ConfigDict(populate_by_name=True, title="Formularz Dodawania Cost")

    transaction_type: Union[
        DataWspolna, RozneDaty, SprzedazOdDo
    ] = Field(
        ...,
        discriminator='typ_transakcji',
        alias="TypTransakcji",
        title="Typ transakcji",
        json_schema_extra={"flatten": True}
    )

    adnotacje: Union[
        AdnotacjeNie,
        AdnotacjeTak
    ] = Field(
        ...,
        discriminator='adnotacje',
        alias="Adnotacje",
        title="Adnotcje",
    )

    my_id: str = Field(  # Zmieniono z UUID na str
        default_factory=lambda: secrets.token_urlsafe(16),
        json_schema_extra={"exclude_from_form": True}
    )



    source: SourceInvoiceSource = Field(
        SourceInvoiceSource.MANUAL,
        title="Zródło",
        json_schema_extra={"exclude_from_form": True}
    )

    inv_type: InvoiceType = Field(
        InvoiceType.PURCHASE,
        alias="TypFaktury",
        json_schema_extra={"exclude_from_form": True}
    )

    inv_nr: str

    date_posting: date = Field(
        ...,
        alias="date_posting",  # Wymuszenie poprawnej nazwy
        title="Data księgowania"
    )

    counterparty_id: str = Field(
        title="Kontrahent",
    )

    currency: CurrencyAB = Field(
        CurrencyAB,
        alias="Waluta",
        title="Waluta",
    )

    total_net: Decimal = Field(max_digits=12, decimal_places=2, title="Razem Netto")
    total_vat: Decimal = Field(max_digits=12, decimal_places=2, title="Razem VAT")
    total_gross: Decimal = Field(max_digits=12, decimal_places=2, title="Razem Brutto")

    @model_validator(mode="before")
    @classmethod
    def wrap_transaction_type(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # Jeśli transaction_type (lub alias) nie ma w danych, a jest typ_transakcji
            if 'TypTransakcji' not in data and 'transaction_type' not in data and 'typ_transakcji' in data:
                # Pola, które mogą należeć do transaction_type
                # Pobieramy je z definicji Union
                # Dla uproszczenia: wszystko co nie jest w SourceInvoice, a jest w modelach transakcji
                # Ale bezpieczniej: wiemy jakie to pola
                tt_fields = {
                    'typ_transakcji', 'date_vat', 'date_cit', 'date_supply', 
                    'date_settlement', 'date_issue', 'date_received', 
                    'date_goods_receipt', 'date_supply_from', 'date_supply_to'
                }
                
                tt_data = {}
                for field in tt_fields:
                    if field in data:
                        tt_data[field] = data.pop(field)
                
                if tt_data:
                    data['transaction_type'] = tt_data
        return data

    @model_validator(mode="after")
    def validate_totals(self) -> "SourceInvoice":
        # 1. Sprawdzenie równania: Netto + VAT = Brutto (z tolerancją 1 grosza)
        # Tutaj definiujemy zmienną pomocniczą:
        calculated_gross = self.total_net + self.total_vat

        if abs(self.total_gross - calculated_gross) > 1:
            raise ValueError(
                f"Błąd sumaryczny: Netto ({self.total_net}) + VAT ({self.total_vat}) "
                f"daje {calculated_gross}, a w Brutto wpisano {self.total_gross}. "
                f"Różnica przekracza 1 grosz."
            )

        return self



    ksef_ref: str = Field(
        default="",
        alias="KsefRef",
        json_schema_extra = {"exclude_from_form": True}
    )

    original_payload_ref: Optional[str] = Field(
        None,
        title="Oryg Payload Ref",
        json_schema_extra = {"exclude_from_form": True}

    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),  # Dodaj import timezone z datetime
        json_schema_extra={"exclude_from_form": True}
    )

    c_nazwa: Optional[str] = Field(
        None,
        alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200,
        json_schema_extra={"exclude_from_form": True}
    )
    c_nip: Optional[str] = Field(
        None,
        alias="NIP",
        title="NIP",
        min_length=10,
        max_length=10,
        pattern=r'^\d{10}$|^brak$',
        json_schema_extra={"exclude_from_form": True}
    )
    c_kod_ue: Optional[EuropeLandsEnum] = Field(
        None,
        alias="KodUE",
        title="VIESS – kod UE",
        json_schema_extra={"exclude_from_form": True}
    )
    c_nr_vat_ue: Optional[str] = Field(
        None,
        alias="NrVatUE",
        title="VIESS – nr identyfikacyjny bez kodu kraju",
        json_schema_extra={"exclude_from_form": True}
    )

    c_kod_kraju: Optional[WorldLandsEnum] = Field(
        None,
        alias="KodKraju",
        title="EKSPORT – kod kraju",
        json_schema_extra={"exclude_from_form": True}
    )
    c_tax_id: Optional[str] = Field(
        None,
        alias="NrID",
        title="EKSPORT – Numer podatkowy",
        json_schema_extra={"exclude_from_form": True}
    )
