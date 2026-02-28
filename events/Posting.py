from datetime import date
from decimal import Decimal
from typing import Optional, List

from pydantic import Field, model_validator, ConfigDict

from models2.abase import BasicBasic
from models2.enums import VATTransactionType
from models2.xxx.h_enums import Currency, UnitType, EuropeLandsEnum, WorldLandsEnum


# from models2.enums import VATTransactionType, PostingFlags  # Decoupled to avoid import issues


class Posting(BasicBasic):
    model_config = ConfigDict(populate_by_name=True)

    model_name: str = Field(
        "Posting",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        pattern=r"^[A-Za-z0-9\-:]+$",
        json_schema_extra={"exclude_from_form": True}
    )


    account_id: str = Field(..., title="Konto*")
    account_type: Optional[str] = Field(None, title="Typ konta (automatycznie pobierany z account_id)", json_schema_extra={"exclude_from_form": True})

    journal_entry_id: Optional[str] = Field(None, title="ID nagłówka księgowania", json_schema_extra={"exclude_from_form": True})

    counterparty_id: Optional[str] = Field(None, title="Partner do rozliczenia")

    amount: Decimal = Field(..., title="Kwota*")
    original_amount: Optional[Decimal] = Field(None, title="Kwota oryginalna")
    original_ccy: Optional[Currency] = Field(None, title="Waluta oryginalna")
    exchange_rate: Optional[Decimal] = Field(None, title="Kurs waluty oryginalny")
    exchange_date: Optional[date] = Field(None, title="Data kursu waluty oryginalny")

    settlement_ref: Optional[str] = Field(None, title="Referencja rozliczenia", json_schema_extra={"exclude_from_form": True})

    quantity: Optional[Decimal] = Field(None, title="Ilość", json_schema_extra={"exclude_from_form": True},)
    unit: Optional[UnitType] = Field(None, title="Jednostka miary", json_schema_extra={"exclude_from_form": True})
    item_id: Optional[str] = Field(None, title="ID przedmiotu", json_schema_extra={"exclude_from_form": True})
    lot_id: Optional[str] = Field(None, title="ID partii", json_schema_extra={"exclude_from_form": True})
    c_nazwa: Optional[str] = Field(
        None,
        alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    c_nip: Optional[str] = Field(
        None,
        alias="NIP",
        title="NIP",
        min_length=10,
        max_length=10,
        pattern=r'^\d{10}$|^brak$'
    )
    c_kod_ue: Optional[EuropeLandsEnum] = Field(
        None,
        alias="KodUE",
        title="VIESS – kod UE"
    )
    c_nr_vat_ue: Optional[str] = Field(
        None,
        alias="NrVatUE",
        title="VIESS – nr identyfikacyjny bez kodu kraju"
    )

    c_kod_kraju: Optional[WorldLandsEnum] = Field(
        None,
        alias="KodKraju",
        title="EKSPORT – kod kraju"
    )
    c_tax_id: Optional[str] = Field(
        None,
        alias="NrID",
        title="EKSPORT – Numer podatkowy"
    )
    doc_nr: Optional[str] = Field(
        None,
        alias="NrDok",
        title="Numer dokumentu"
    )
    doc_type: Optional[str] = Field(
        None,
        alias="TypDok",
        title="Typ dokumentu"
    )

    vat_transaction_type: Optional[VATTransactionType] = Field(
        None,
        title="Typ transakcji VAT"
    )

    inventory_ref: Optional[str] = None

    is_tax_deductible: Optional[bool] = None

    vat_base_amount: Optional[Decimal] = None
    vat_amount: Optional[Decimal] = None

    tags: Optional[List[str]] = Field(
        None,
        title="Tagi",
        json_schema_extra={
            "form_widget": "select_multiple"
        }
    )

    flags: Optional[List[str]] = Field(
        None,
        title="Flagi",
        json_schema_extra={
            "form_widget": "select_multiple"
        }
    )

    # ------------------------
    # WALIDATORY / AUTOMATYCZNE POLA
    # ------------------------

    @model_validator(mode='before')
    def validate_amount_and_set_account_type(cls, values):
        # Automatyczne ustawienie account_type
        account_id = values.get('account_id')
        if account_id and ':' in account_id:
            values['account_type'] = account_id.split(':')[0]
        elif account_id:
            # Jeśli brak dwukropka, traktujemy cały account_id jako typ
            values['account_type'] = account_id
        else:
            values['account_type'] = None

        return values

    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "posting"