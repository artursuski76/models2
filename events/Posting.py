from datetime import date
from decimal import Decimal
from typing import Optional, List

from pydantic import Field, model_validator

from models2.abase import BasicBasic
from models2.enums import VATTransactionType, PostingFlags
from models2.xxx.h_enums import Currency, UnitType


class Posting(BasicBasic):
    __auto_id__ = True

    model_name: str = Field(
        "Posting",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="ID (A-Z,a-z,0-9,:, np.: Abc-sp-zoo:NIP789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki.",
        json_schema_extra={"exclude_from_form": True}
    )

    journal_entry_id: str = Field(..., title="ID wpisu dzienniczka*", json_schema_extra={"exclude_from_form": True})

    account_id: str = Field(..., title="Konto*")
    account_type: Optional[str] = Field(None, title="Typ konta (automatycznie pobierany z account_id)", json_schema_extra={"exclude_from_form": True})

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

    tags: List[VATTransactionType] = Field(
        None,
        title="Tagi",
        json_schema_extra={
            "form_widget": "select_multiple"
        }
    )

    flags: List[PostingFlags] = Field(
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
        # Walidacja amount
        amount = values.get('amount')
        if amount is not None and amount <= 0:
            raise ValueError("Amount must be > 0")

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