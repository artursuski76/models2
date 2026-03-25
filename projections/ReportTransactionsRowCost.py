from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic



class ReportTransactionsRowCost(BasicBasic):

    model_name: str = Field(
        "ReportTransactionsRowCost",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    cost_inv_my_id: str
    cost_inv_status: str
    cost_inv_source: str
    cost_inv_nr: str
    cost_inv_date_posting: date
    cost_inv_counterparty_id: str
    cost_inv_currency: str
    cost_inv_ksef_ref: Optional[str]
    cost_inv_original_payload_ref: Optional[str] = None

    row_type: Optional[str]
    vat_category: Optional[str]

    inventory_item_id: Optional[str] = Field(
        default=None,
        title="Kod inwent."
    )

    description:  Optional[str] = Field(
        None,
        title="Opis"
    )
    amount_net: Decimal = Field(..., title="Netto")
    amount_vat: Decimal= Field(..., title="VAT")
    amount_gross: Decimal = Field(..., title="Brutto")
    nkup: bool = Field(False, title="NKUP")


    vat_rate_doc:  Optional[float] = Field(
        ...,
        title="VAT_doc %",
        json_schema_extra={"exclude_from_form": True}
    )
    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )



    class Couchbase:
        bucket = "Accounting"
        scope = "projections"
        collection = "transactions_row_cost"