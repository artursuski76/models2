from typing import Annotated, Union, Any, List

from pydantic import Field, computed_field, model_validator, AliasChoices

from models2.basic.SaleInvoiceBasic import SaleInvoiceBasic
from models2.helpers.sale_invoice_type import Podstawowa, Zaliczkowa, Rozliczeniowa, Korekta, SaleTransactionRows

RodzajFV = Annotated[
    Union[
        Podstawowa,
        Zaliczkowa,
        Rozliczeniowa,
        Korekta
    ],
    Field(
        discriminator="rodzaj_fv"
    )
]


class SaleInvoice(SaleInvoiceBasic):
    @model_validator(mode="before")
    @classmethod
    def _preprocess_typtransakcji_vs_rodzajfv(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # 1. Obsługa transaction_items i transaction_items_after na najwyższym poziomie
            # Jeśli są w TypTransakcji lub rodzaj_fv, wyciągnij je wyżej
            for field in ["rodzaj_fv", "TypTransakcji"]:
                val = data.get(field)
                if isinstance(val, dict):
                    # transaction_items
                    for item_field in ["transaction_items", "WierszTransakcji"]:
                        if item_field in val and "transaction_items" not in data:
                            data["transaction_items"] = val[item_field]
                    # transaction_items_after
                    for item_field_after in ["transaction_items_after", "WierszTransakcjiPoKorekcie"]:
                        if item_field_after in val and "transaction_items_after" not in data:
                            data["transaction_items_after"] = val[item_field_after]

            # 2. Mapowanie rodzaj_fv -> TypTransakcji (rodzaj_fv_obj odpowiednik) dla pydantica
            # SaleInvoice używa pola 'rodzaj_fv' z aliasem 'TypTransakcji'
            if "rodzaj_fv" in data and "TypTransakcji" not in data:
                if isinstance(data["rodzaj_fv"], str):
                    data["TypTransakcji"] = {"rodzaj_fv": data["rodzaj_fv"]}
                else:
                    data["TypTransakcji"] = data.pop("rodzaj_fv")

        return data

    rodzaj_fv: RodzajFV = Field(
        default=Podstawowa,
        discriminator='rodzaj_fv',
        alias="TypTransakcji",
        title="Typ transakcji",
        exclude=True
    )

    transaction_items: List[SaleTransactionRows] = Field(
        default_factory=list,
        alias="WierszTransakcji",
        validation_alias=AliasChoices("transaction_items", "WierszTransakcji"),
        title="Pozycje księgowania",
    )

    transaction_items_after: List[SaleTransactionRows] = Field(
        default_factory=list,
        alias="WierszTransakcjiPoKorekcie",
        validation_alias=AliasChoices("transaction_items_after", "WierszTransakcjiPoKorekcie"),
        title="Pozycje księgowania po korekcie",
    )

    @computed_field(alias="rodzaj_fv")
    @property
    def rodzaj_fv_flat(self) -> str:
        return self.rodzaj_fv.rodzaj_fv

    model_name: str = Field(
        "CostInvoice",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )



    @model_validator(mode="after")
    def validate_totals_integrity(self) -> "SaleInvoice":
        """
        Sprawdza czy sumy w nagłówku (z SaleInvoiceBasic)
        zgadzają się z sumą poszczególnych wierszy.
        """
        # Dla korekty sprawdzamy sumy jako różnicę między 'after' a 'before'
        if self.rodzaj_fv.rodzaj_fv == "Korekta":
            items_before = self.transaction_items
            items_after = self.transaction_items_after

            sum_net = sum(row.amount_net for row in items_after) - sum(row.amount_net for row in items_before)
            sum_vat = sum(row.amount_vat for row in items_after) - sum(row.amount_vat for row in items_before)
            sum_gross = sum(row.amount_gross for row in items_after) - sum(row.amount_gross for row in items_before)
        else:
            items = self.transaction_items
            if not items:
                return self

            # Obliczamy sumy z wierszy
            sum_net = sum(row.amount_net for row in items)
            sum_vat = sum(row.amount_vat for row in items)
            sum_gross = sum(row.amount_gross for row in items)

        # 2. Porównanie z nagłówkiem (tolerancja 0, bo to liczby całkowite - grosze)
        if sum_net != self.total_net:
            raise ValueError(f"Suma Netto wierszy ({sum_net}) != Razem Netto ({self.total_net})")

        if sum_vat != self.total_vat:
            raise ValueError(f"Suma VAT wierszy ({sum_vat}) != Razem VAT ({self.total_vat})")

        if sum_gross != self.total_gross:
            raise ValueError(f"Suma Brutto wierszy ({sum_gross}) != Razem Brutto ({self.total_gross})")

        return self

    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "counterparty_id", "currency", "my_id", "date_posting", "total_net",
            "total_vat", "total_gross", "rodzaj_fv_flat", "original_payload_ref", "status",
            "transaction_items", "transaction_items_after", "transaction_items_count"
        ]
        default_sort_field = "date_posting"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "sale_invoice"