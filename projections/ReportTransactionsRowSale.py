from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic
# from models2.helpers.money import Money


class ReportTransactionsRowSale(BasicBasic):
    model_name: str = Field(
        "ReportTransactionsRowSale",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    sale_inv_my_id: str
    sale_inv_status: str
    sale_inv_source: str
    sale_inv_counter: int
    sale_inv_date_posting: date
    sale_inv_date_sale: Optional[date]
    sale_inv_counterparty_id: str
    sale_inv_currency: str
    sale_inv_ksef_ref: Optional[str]
    sale_inv_original_payload_ref: Optional[str] = None

    sale_inv_cash_method: bool = False
    sale_inv_self_billing: bool = False
    sale_inv_reverse_charge: bool = False
    sale_inv_split_payment: bool = False
    sale_inv_ec_simplified: bool = False

    vat_category: Optional[str] = None
    tu: Optional[str] = None
    inventory_item_id: Optional[str] = Field(
        default=None,
        title="Kod inwent."
    )
    quantity: Optional[Decimal] = None
    uom: Optional[str] = None
    unit_price_net: Optional[Decimal] = None
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    amount_net: Decimal = Field(..., max_digits=12, decimal_places=2, title="Netto")
    amount_vat: Decimal = Field(..., max_digits=12, decimal_places=2, title="VAT")
    amount_gross: Decimal = Field(..., max_digits=12, decimal_places=2, title="Brutto")

    vat_rate_doc: Optional[float] = Field(default=0, title="VAT_doc %")
    vat_rate_oss: Optional[float] = Field(default=0, title="VAT_oss %")
    ctry_oss: Optional[str] = None

    class Couchbase:
        bucket = "Accounting"
        scope = "projections"
        collection = "transactions_row_sale"