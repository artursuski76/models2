from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic
# from models2.helpers.money import Money


class ReportTransactionsRowSale(BasicBasic):
    cost_inv_my_id: str
    cost_inv_source: str
    cost_inv_inv_nr: str
    cost_inv_counterparty_id: str
    cost_inv_currency: str
    cost_inv_date_posting: date
    cost_inv_ksef_ref: Optional[str]
    cost_inv_original_payload_ref: str


    row_type: Optional[str] = Field()
    amount_net: Decimal = Field(..., max_digits=12, decimal_places=2, title="Netto")
    amount_vat: Decimal = Field(..., max_digits=12, decimal_places=2, title="VAT")
    amount_gross: Decimal = Field(..., max_digits=12, decimal_places=2, title="Brutto")

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    inventory_item_id: Optional[str] = Field(
        default=None,
        title="Kod inwent."
    )
    description: Optional[str] = Field(
        None,
        title="Opis"
    )

    class Couchbase:
        bucket = "Accounting"
        scope = "projections"
        collection = "transactions_row_sale"