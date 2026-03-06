from datetime import date, datetime
from typing import Optional, Any, Dict

from pydantic import ConfigDict, Field

from models2.abase import BasicBasic
from models2.helpers.TaskTaskName import StatusZamowienia


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
    status_zamowienia: StatusZamowienia = Field(default=StatusZamowienia.PENDING)

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

    # --- Twoje zdefiniowane pola najwyższego rzędu ---
    processed_to_invoice: bool = Field(default=False)
    processed_at: Optional[datetime] = None
    sale_invoice_ref: Optional[str] = None

    # Przykładowe pola obiektowe, które też mogą być "elastyczne"
    # (Pamiętaj, by w ich definicjach w models2 również dodać extra='allow')
    simple: Optional[Dict[str, Any]] = Field(default_factory=dict)
    details: Optional[Dict[str, Any]] = Field(default_factory=dict)
    payment: Optional[Dict[str, Any]] = Field(default_factory=dict)


    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
        "my_id", "simple", "payment", "processed_to_invoice" "processed_at", "sale_invoice_ref", "status_zamowienia"
        ]
        default_sort_field = "date_completed"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "apilo_order"

