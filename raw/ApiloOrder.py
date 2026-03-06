from datetime import date
from typing import Optional, List, Any

from pydantic import Field
from pydantic import ConfigDict, Field

from models2.abase import BasicBasic
from models2.helpers.WooOrdersHelpers import WooBillingAndShipping, WooLineItems, WooShippingLines, WooMetaData



class ApiloOrder(BasicBasic):
    model_config = ConfigDict(extra='allow')

    model_name: str = Field(
        "ApiloOrder",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        title="Unikalny ID, np.: Abcde:PL789331 *",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )

    processed_at: Optional[date] = Field(
        None,
        title="Data przetworzenia zamówienia",
        json_schema_extra={"exclude_from_form": True}
    )
    inv_gen_at: Optional[date] = Field(
        None,
        title="Data przetworzenia zamówienia",
        json_schema_extra={"exclude_from_form": True}
    )

    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
        "my_id", "simple", "payment", "processed_to_invoice" "processed_at", "sale_invoice_ref"
        ]
        default_sort_field = "date_completed"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "apilo_order"

