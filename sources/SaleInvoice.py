from datetime import date
from decimal import Decimal
from typing import Annotated, Dict
from typing import List
from typing import Optional, Union, Any

from pydantic import AliasChoices, model_serializer
from pydantic import Field, ConfigDict, model_validator
from pydantic import computed_field

from models2.basic.SaleInvoiceBasic import SaleInvoiceBasic
from models2.helpers.InvoicePlatnosc import InvoicePlatnosc
from models2.helpers.address import AddressCounterparty
from models2.helpers.forms_type_sales_inv import DostawaWDacieWystawienia, WspolnaDataDostawy, DostawaWOkresieCzasu
from models2.helpers.sale_invoice_adnotacje import AdnotacjeNie, AdnotacjeTak
from models2.helpers.sale_invoice_type import Podstawowa, Zaliczkowa, Rozliczeniowa, Korekta, SaleTransactionRows
from models2.xxx.h_dane_identyfikacyjne import (OsobaFizyczna,
                                                PodatnikKrajowy,
                                                PodatnikVIES,
                                                PodatnikZagraniczny
                                                )
from models2.xxx.h_enums import CurrencyAB

RodzajFV = Annotated[
    Union[
        Podstawowa,
        Zaliczkowa,
        Rozliczeniowa,
        Korekta
    ],
    Field(
        discriminator="rodzaj_fv"
    )
]



class SaleInvoice(SaleInvoiceBasic):
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True,
        title="Formularz Dodawania Sale Invoice"
    )

    model_name: str = Field(
        "SaleInvoice",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    @model_validator(mode="before")
    @classmethod
    def _preprocess_typtransakcji_vs_rodzajfv(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # 1. Obsługa transaction_items i transaction_items_after na najwyższym poziomie
            # Jeśli są w TypTransakcji lub rodzaj_fv, wyciągnij je wyżej
            for field in ["rodzaj_fv", "TypTransakcji"]:
                val = data.get(field)
                if isinstance(val, dict):
                    # transaction_items
                    for item_field in ["transaction_items", "WierszTransakcji"]:
                        if item_field in val and "transaction_items" not in data:
                            data["transaction_items"] = val[item_field]
                    # transaction_items_after
                    for item_field_after in ["transaction_items_after", "WierszTransakcjiPoKorekcie"]:
                        if item_field_after in val and "transaction_items_after" not in data:
                            data["transaction_items_after"] = val[item_field_after]

            # 2. Mapowanie rodzaj_fv -> TypTransakcji (rodzaj_fv_obj odpowiednik) dla pydantica
            # SaleInvoice używa pola 'rodzaj_fv' z aliasem 'TypTransakcji'
            if "rodzaj_fv" in data and "TypTransakcji" not in data:
                if isinstance(data["rodzaj_fv"], str):
                    data["TypTransakcji"] = {"rodzaj_fv": data["rodzaj_fv"]}
                else:
                    data["TypTransakcji"] = data.pop("rodzaj_fv")

        return data

    # --- KOLUMNA 1: GŁÓWNE DANE ---

    rodzaj_fv: RodzajFV = Field(
        default_factory=lambda: Podstawowa,
        discriminator='rodzaj_fv',
        alias="TypTransakcji",
        title="Typ transakcji",
        exclude=True,
        json_schema_extra={
            "section": "header",
            "column": 1,
            "order": 1,
        }
    )

    @computed_field(alias="rodzaj_fv")
    @property
    def rodzaj_fv_flat(self) -> str:
        return self.rodzaj_fv.rodzaj_fv




    date_sale: Union[
        DostawaWDacieWystawienia,
        DostawaWOkresieCzasu,
        WspolnaDataDostawy
    ] = Field(
        ...,
        discriminator='date_sale',
        validation_alias=AliasChoices("DataSprzedazy", "date_sale"),
        serialization_alias="DataSprzedazy",
        title="Data sprzedaży",
        json_schema_extra={
            "section": "header",
            "column": 1,
            "order": 3,
        }
    )

    @computed_field(alias="date_sale")
    @property
    def date_sale_flat(self) -> str:
        return self.date_sale.date_sale

    @computed_field
    @property
    def common_date_sale(self) -> date | None:
        return getattr(self.date_sale, "common_date_sale", None)

    @computed_field
    @property
    def date_sale_from(self) -> date | None:
        return getattr(self.date_sale, "date_sale_from", None)

    @computed_field
    @property
    def date_sale_to(self) -> date | None:
        return getattr(self.date_sale, "date_sale_to", None)

    # --- KOLUMNA 2: ADRES I ADNOTACJE ---

    counterparty_id: str = Field(
        title="Kontrahent",
        json_schema_extra={
            "section": "header",
            "column": 2,
            "order": 1,
        }
    )

    dane_identyfikacyjne: Union[
        OsobaFizyczna,
        PodatnikKrajowy,
        PodatnikVIES,
        PodatnikZagraniczny
    ] = Field(
        ...,
        discriminator='rodzaj_kontr',
        alias="DaneIdentyfikacyjne",
        title="Rodzaj",
        json_schema_extra={
            "section": "header",
            "column": 2,
            "order": 2,
        }
    )

    @model_validator(mode="before")
    @classmethod
    def wrap_dane_identyfikacyjne(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # Jeśli dane_identyfikacyjne nie ma w słowniku, a jest rodzaj_kontr,
            # to próbujemy "zwinąć" płaskie pola do dane_identyfikacyjne.
            if "dane_identyfikacyjne" not in data and "DaneIdentyfikacyjne" not in data:
                if "rodzaj_kontr" in data:
                    # Pola, które mogą należeć do dane_identyfikacyjne
                    # Możemy po prostu przekazać cały słownik jako dane_identyfikacyjne,
                    # Pydantic wybierze to co potrzebuje dla konkretnego modelu z Union.
                    data["dane_identyfikacyjne"] = data.copy()
        return data

    @model_serializer(mode="wrap")
    def serialize_flat(self, handler) -> Dict[str, Any]:
        # Pobieramy standardowy słownik (wywołując oryginalny serializer)
        data = handler(self)

        # Wyciągamy dane identyfikacyjne
        dane_ident = data.pop("dane_identyfikacyjne", {})

        # Łączymy główny słownik z polami z dane_identyfikacyjne
        # Uwaga: Jeśli klucze się powtórzą, dane_ident nadpiszą te z poziomu głównego
        return {**data, **dane_ident}

    address: Optional[AddressCounterparty] = Field(
        default_factory=lambda: AddressCounterparty(),
        validate_default=True,  # Ważne: wymusza walidację nawet dla wartości domyślnych/pustych
        validation_alias=AliasChoices("address", "Address"),
        serialization_alias="Address",
        title="Adres kontrahenta",
        json_schema_extra={
            "section": "header",
            "column": 2,
            "order": 3,
        }
    )

    adnotacje: Union[
        AdnotacjeNie,
        AdnotacjeTak
    ] = Field(
        ...,
        discriminator='adnotacje',
        validation_alias=AliasChoices("Adnotacje", "adnotacje"),
        serialization_alias="Adnotacje",
        title="Adnotacje",
        json_schema_extra={
            "section": "header",
            "column": 3,
            "order": 2,
        }
    )

    # --- KOLUMNA 3: PŁATNOŚCI I WALUTA ---

    currency: CurrencyAB = Field(
        CurrencyAB.PLN,
        validation_alias=AliasChoices("Waluta", "currency"),
        serialization_alias="Waluta",
        title="Waluta dokumentu",
        json_schema_extra={
            "section": "header",
            "column": 3,
            "order": 1,
        }
    )

    platnosc: InvoicePlatnosc = Field(
        title="Dane płatności",
        json_schema_extra={
            "section": "header",
            "column": 3,
            "order": 3,
        }
    )

    user_inv_nr: Optional[str] = Field(
        None,
        title="Własny numer faktury",
        json_schema_extra={
            "section": "header",
            "column": 3,
            "order": 4,
        }
    )


    # --- DÓŁ FORMULARZA (Pełna szerokość lub ostatnie sekcje) ---

    transaction_items: List[SaleTransactionRows] = Field(
        default_factory=list,
        validation_alias=AliasChoices("transaction_items", "WierszTransakcji"),
        serialization_alias="WierszTransakcji",
        title="Pozycje faktury",
        json_schema_extra={
            "section": "main",  # Nowy podział
            "full_width": True,
            "order": 1
        }
    )

    total_net: Decimal = Field(
        max_digits=12,
        decimal_places=2,
        title="Razem Netto",
        json_schema_extra={
            "section": "footer",
            "column": 3,
            "order": 110,
        }
    )

    total_vat: Decimal = Field(
        max_digits=12,
        decimal_places=2,
        title="Razem VAT",
        json_schema_extra={
            "section": "footer",
            "column": 3,
            "order": 111,
        }
    )

    total_gross: Decimal = Field(
        max_digits=12,
        decimal_places=2,
        title="Razem Brutto",
        json_schema_extra={
            "section": "footer",
            "column": 3,
            "order": 112,
        }
    )

    @model_validator(mode="after")
    def validate_totals(self) -> "SaleInvoiceBasic":
        # 1. Sprawdzenie równania: Netto + VAT = Brutto (z tolerancją 1 grosza)
        calculated_gross = self.total_net + self.total_vat

        if abs(self.total_gross - calculated_gross) > 1:
            raise ValueError(
                f"Błąd sumaryczny w nagłówku: Netto ({self.total_net}) + VAT ({self.total_vat}) "
                f"daje {calculated_gross}, a w Brutto wpisano {self.total_gross}. "
                f"Różnica przekracza 1 grosz."
            )

        return self

    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "company_id",
            "company_uuid",
            "counter",
            "inv_nr",
            "counterparty_id",
            "created_at",
            "DataSprzedazy",
            "date_posting",
            "KodKraju",
            "KodUE",
            "KsefRef",
            "KsefStatus",
            "KsefJsonFile",
            "KsefXmlFile",
            "ksef_status_code",
            "model_name",
            "my_id",
            "Nazwa",
            "original_payload_ref",
            "rodzaj_fv",
            "total_gross",
            "Waluta",
            "WyslijDoKsef",
            "KsefProcessingStatus"
        ]
        default_sort_field = "counter"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "sale_invoice"
