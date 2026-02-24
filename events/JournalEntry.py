from datetime import date
from typing import Optional

from pydantic import Field

from models2.xxx.h_enums import Currency
from models2.abase import BasicBasic
from models2.enums import EntryType, SourceDocumentType


class JournalEntry(BasicBasic):

    __auto_id__ = True

    model_name: str = Field(
        "JournalEntry",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Unikalny ID (A-Z, a-z, 0-9, myślniki, np.: AbcSpZoo:PL789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z",
        json_schema_extra={"exclude_from_form": True}
    )
    counter: int = Field(
        default=0,
        json_schema_extra={"exclude_from_form": True}
    )

    journal_number: Optional[str] = None

    transaction_date: date
    posting_date: date

    entry_type: EntryType = EntryType.GENERAL

    source_doc_type: Optional[SourceDocumentType] = None
    source_doc_id: Optional[str] = None
    source_doc_number: Optional[str] = None

    source_snapshot: Optional[dict] = None

    base_ccy: Currency = Currency.PLN

    description: Optional[str] = None


    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "journal_entry"