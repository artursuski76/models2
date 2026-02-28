from datetime import date, datetime
from typing import Optional

from pydantic import Field, model_validator

from models2.abase import BasicBasic
from models2.enums import SourceDocumentType
from models2.enums_all.ksef import KSeFStatus
from models2.xxx.h_enums import Currency


class JournalEntry(BasicBasic):


    model_name: str = Field(
        "JournalEntry",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        pattern=r"^[A-Za-z0-9\-:]+$",
        json_schema_extra={"exclude_from_form": True}
    )

    counter: int = Field(
        default=0,
        json_schema_extra={"exclude_from_form": True}
    )

    transaction_date: Optional[date] = Field(None, title="Data transakcji", json_schema_extra={"exclude_from_form": True})

    posting_date: date = Field(default_factory=date.today, title="Data wystawienia")

    year: int = Field(default=0, json_schema_extra={"exclude_from_form": True})
    month: int = Field(default=0, json_schema_extra={"exclude_from_form": True})


    @model_validator(mode="after")
    def set_year_month(self):
        self.year = self.posting_date.year
        self.month = self.posting_date.month
        return self

    tax_date: Optional[date] = Field(None, title="Data podatkowa", json_schema_extra={"exclude_from_form": True})

    source_doc_type: Optional[SourceDocumentType] = Field(None, title="Typ Dokumentu Źródłowego", json_schema_extra={"exclude_from_form": True})
    source_doc_id: Optional[str] = Field(None, title="ID Dokumentu Źródłowego", json_schema_extra={"exclude_from_form": True})
    source_doc_number: Optional[str] = Field(None, title="Nr dok źródłowego", json_schema_extra={"exclude_from_form": True})

    source_snapshot: dict = Field(default_factory=dict, title="Snapshot dokumentu", json_schema_extra={"exclude_from_form": True})

    base_ccy: Currency = Field(Currency.PLN, title="Podstawowa waluta", json_schema_extra={"exclude_from_form": True})

    description: Optional[str] = Field(None, title="Opis")

    ksef_status: Optional[KSeFStatus] = Field(
        None,
        title="Status w KSeF",
        json_schema_extra={"exclude_from_form": True}
    )
    ksef_reference_number: Optional[str] = Field(
        None,
        title="Numer referencyjny KSeF",
        json_schema_extra={"exclude_from_form": True}
    )
    ksef_sent_at: Optional[datetime] = Field(
        None,
        title="Data wysłania do KSeF",
        json_schema_extra={"exclude_from_form": True}
    )
    ksef_error_message: Optional[str] = Field(
        None,
        title="Błąd z KSeF",
        json_schema_extra={"exclude_from_form": True}
    )
    ksef_payload_hash: Optional[str]
    ksef_schema_version: Optional[str]

    is_correction: bool = False
    corrected_entry_id: Optional[str] = None
    correction_reason: Optional[str] = None

    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "journal_entry"