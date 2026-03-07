from typing import Annotated, Union, Any, List

from pydantic import Field, computed_field, model_validator, AliasChoices, ConfigDict

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
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

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
        validation_alias=AliasChoices("transaction_items", "WierszTransakcji"),
        serialization_alias="WierszTransakcji",
        title="Pozycje księgowania",
    )



    @computed_field(alias="rodzaj_fv")
    @property
    def rodzaj_fv_flat(self) -> str:
        return self.rodzaj_fv.rodzaj_fv

    model_name: str = Field(
        "SaleInvoice",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )


    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            # "Adnotacje",
            # "CAdresL1",
            # "CAdresL2",
            # "CKraj",
            "common_date_sale",
            "company_id",
            "company_uuid",
            "counter",
            "counterparty_id",
            "created_at",
            "DataSprzedazy",
            "date_posting",
            # "date_sale_from",
            # "date_sale_to",
            "date_sale",
            "KodKraju",
            "KodUE",
            "KsefJsonFile",
            "KsefRef",
            "KsefStatus",
            "KsefJsonFile",
            "KsefXmlFile",
            # "last_sync",
            "model_name",
            "my_id",
            "Nazwa",
            # "NIP",
            # "NrID",
            # "NrVatUE",
            "original_payload_ref",
            "rodzaj_fv",
            # "RodzajKontr",
            # "sha",
            # "source",
            # "status",
            # "StatusKonta",
            "total_gross",
            # "total_net",
            # "total_vat",
            # "user_id",
            "Waluta",
            # "WierszTransakcji",
            "WyslijDoKsef",
        ]
        default_sort_field = "date_posting"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "sale_invoice"