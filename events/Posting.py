from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import Field

from models2.xxx.h_enums import Currency, UnitType, PostingTags, PostingFlags
from models2.abase import BasicBasic


class Posting(BasicBasic):
    model_name: str = Field(
        "JournalEntry",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="ID (A-Z,a-z,0-9,:, np.: Abc-sp-zoo:NIP789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )


    journal_entry_id: str
    account_id: str
    counterparty_id: Optional[str] = None

    amount: Decimal  # w base currency
    original_amount: Optional[Decimal]
    original_ccy: Optional[Currency]
    exchange_rate: Optional[Decimal]
    exchange_date: Optional[date]

    # opcjonalne:
    settlement_ref: Optional[str] = None
    quantity: Optional[Decimal] = None
    unit: Optional[UnitType] = None
    inventory_item_id: Optional[str] = None
    lot_id: Optional[str] = None

    tags: PostingTags = PostingTags.N
    flags: PostingFlags = PostingFlags.N

# JournalEntry → Posting (1:N)
# Posting → InventoryBatch
# Posting → InventoryItem


    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "posting"

