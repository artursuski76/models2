from typing import Annotated, Union, Any

from pydantic import Field, AliasChoices, model_validator, computed_field

from models2.basic.CostInvoiceBasic import CostInvoiceBasic
from models2.helpers.cost_invoice_type import PodstawowaK, ZaliczkowaK, RozliczeniowaK, KorektaK, TransactionRow



RodzajFV = Annotated[
    Union[
        PodstawowaK,
        ZaliczkowaK,
        RozliczeniowaK,
        KorektaK
    ],
    Field(
        discriminator="rodzaj_fv"
    )
]


class CostInvoice(CostInvoiceBasic):
    # Pre-procesing: jeżeli klient wysyła dawny format z \"TypTransakcji\" zawierającym \"rodzaj_fv\",
    # to przenieś to do pola \"rodzaj_fv\" i ustaw domyślny \"transaction_type\".
    @model_validator(mode="before")
    @classmethod
    def _preprocess_typtransakcji_vs_rodzajfv(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # 1. Obsługa transaction_items na najwyższym poziomie
            # Jeśli transaction_items są w rodzaj_fv lub TypTransakcji, wyciągnij je wyżej
            for field in ["rodzaj_fv", "rodzaj_fv_obj", "TypTransakcji", "transaction_type"]:
                val = data.get(field)
                if isinstance(val, dict) and "transaction_items" in val:
                    if "transaction_items" not in data:
                        data["transaction_items"] = val["transaction_items"]

            tt = data.get("TypTransakcji") or data.get("transaction_type")
            # Stary/pomyłkowy przypadek: w \"TypTransakcji\" siedzi strukturę unionu rodzaj_fv
            if isinstance(tt, dict) and ("rodzaj_fv" in tt or "transaction_items" in tt):
                # Przenieś do pola rodzaj_fv_obj (jeśli nie ma już podane osobno)
                if "rodzaj_fv_obj" not in data and "rodzaj_fv" not in data:
                    data["rodzaj_fv_obj"] = tt
                # Ustaw minimalny transaction_type, by spełnić dyskryminator 'typ_transakcji'
                # Wybieramy najprostszy wariant 'data_wspolna'.
                data["TypTransakcji"] = {"typ_transakcji": "data_wspolna"}

            # Mapowanie rodzaj_fv -> rodzaj_fv_obj dla pydantica
            if "rodzaj_fv" in data and "rodzaj_fv_obj" not in data:
                # Jeśli to jest string, musimy go zamienić na dict dla dyskryminatora RodzajFV
                if isinstance(data["rodzaj_fv"], str):
                    data["rodzaj_fv_obj"] = {"rodzaj_fv": data["rodzaj_fv"]}
                else:
                    data["rodzaj_fv_obj"] = data.pop("rodzaj_fv")

        return data

    @computed_field
    @property
    def rodzaj_fv(self) -> str:
        return self.rodzaj_fv_obj.rodzaj_fv

    rodzaj_fv_obj: RodzajFV = Field(
        default=PodstawowaK(),
        alias="rodzaj_fv_obj",
        validation_alias=AliasChoices("rodzaj_fv_obj", "rodzaj_fv", "TypTransakcji"),
        title="Typ transakcji",
        exclude=True
    )

    transaction_items: list[TransactionRow] = Field(
        default_factory=list,
        alias="transaction_items",
        validation_alias=AliasChoices("transaction_items", "WierszTransakcji"),
        title="Pozycje księgowania",
    )

    @property
    def rodzaj_fv_flat(self) -> str:
        return self.rodzaj_fv_obj.rodzaj_fv

    model_name: str = Field(
        "CostInvoice",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    inv_type: str = Field(
        default="PURCHASE",
        json_schema_extra = {"exclude_from_form": True}
    )



    @model_validator(mode="after")
    def validate_totals_integrity(self) -> "CostInvoice":
        """
        Sprawdza czy sumy w nagłówku (z SourceInvoice)
        zgadzają się z sumą poszczególnych wierszy.
        """
        # 1. Najpierw wywołujemy walidację z klasy bazowej (Netto + VAT = Brutto)
        # Pydantic robi to automatycznie, ale tutaj skupiamy się na relacji nagłówek-wiersze.

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
            "counterparty_id", "inv_nr", "currency", "my_id", "date_posting", "total_net",
            "total_vat", "total_gross", "transaction_items"
        ]
        default_sort_field = "date_posting"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "cost_invoice"

