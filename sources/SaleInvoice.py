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
            "company_id",
            "company_uuid",
            "counter",
            "inv_nr",
            "counterparty_id",
            "created_at",
            "DataSprzedazy",
            "date_posting",
            "KodKraju",
            "KodUE",
            "KsefRef",
            "KsefStatus",
            "KsefJsonFile",
            "KsefXmlFile",
            "model_name",
            "my_id",
            "Nazwa",
            "original_payload_ref",
            "rodzaj_fv",
            "total_gross",
            "Waluta",
            "WyslijDoKsef"
        ]
        default_sort_field = "counter"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "sale_invoice"

# SELECT COUNT(*) AS total_records
# FROM `Accounting`.`sources`.`sale_invoice` d
# WHERE d.company_id = "offlite"
#   AND d.company_uuid = "9f919fc1-b45d-45de-ad67-18db2960e443"
#   AND d.details.createdAt < "2026-03-01"
#
#
# {
#   "company_id": "offlite",
#   "company_uuid": "9f919fc1-b45d-45de-ad67-18db2960e443",
#   "details": {
#     "addressCustomer": {
#       "city": "Szczecin",
#       "class": "house",
#       "companyName": null,
#       "companyTaxNumber": null,
#       "country": "PL",
#       "department": null,
#       "email": "mwfhe51mjg+28d78da07@allegromail.pl",
#       "id": 12423,
#       "name": "Dorota Simankowicz",
#       "parcelIdExternal": null,
#       "parcelName": null,
#       "phone": "+48 538 209 693",
#       "streetName": "Milczańska",
#       "streetNumber": "6b/2",
#       "zipCode": "70-117"
#     },
#     "addressDelivery": {
#       "city": "Szczecin",
#       "class": "parcel",
#       "companyName": null,
#       "companyTaxNumber": null,
#       "country": "PL",
#       "department": null,
#       "email": "mwfhe51mjg+28d78da07@allegromail.pl",
#       "id": 12426,
#       "name": "Łukasz Simankowicz",
#       "parcelIdExternal": "AL025ZS1",
#       "parcelName": "Allegro One Box - AL025ZS1",
#       "phone": "+48538209693",
#       "streetName": "al. Powstańców Wielkopolskich",
#       "streetNumber": "39D",
#       "zipCode": "70-111"
#     },
#     "addressInvoice": null,
#     "carrierAccount": 5,
#     "carrierId": 143,
#     "createdAt": "2026-02-23T09:43:55+0100",
#     "customerLogin": "DORCIA114",
#     "id": "AL260200066",
#     "idExternal": "7c51a0b0-1092-11f1-844a-5dc3fc9cc8e8",
#     "isCanceledByBuyer": false,
#     "isEncrypted": false,
#     "isInvoice": false,
#     "orderDiscounts": [],
#     "orderItems": [
#       {
#         "ean": "5903899665679",
#         "id": 12561,
#         "idExternal": "7c4c4980-1092-11f1-844a-5dc3fc9cc8e8",
#         "media": "https://a.allegroimg.com/s128/115659/0f1e6c294acfbcd2fa46ba4a0b3d",
#         "originalCode": "15290967388",
#         "originalName": "Chlorox S podchloryn sodu do dezynfekcji wody 6 kg",
#         "originalPriceWithTax": "48.49",
#         "originalPriceWithoutTax": "44.90",
#         "productId": null,
#         "productSet": null,
#         "quantity": 1,
#         "sku": "15290967388",
#         "status": 1,
#         "tax": "8.00",
#         "type": 1,
#         "unit": null
#       },
#       {
#         "ean": null,
#         "id": 12564,
#         "idExternal": null,
#         "media": null,
#         "originalCode": "0b257488-c85d-4507-b967-9b45ffbfa2e8",
#         "originalName": "Allegro One Box, DPD",
#         "originalPriceWithTax": "0.00",
#         "originalPriceWithoutTax": "0.00",
#         "productId": null,
#         "productSet": null,
#         "quantity": 1,
#         "sku": null,
#         "status": 1,
#         "tax": null,
#         "type": 2,
#         "unit": null
#       }
#     ],
#     "orderNotes": [],
#     "orderPayments": [
#       {
#         "amount": "48.49",
#         "comment": null,
#         "currency": "PLN",
#         "id": 5604,
#         "idExternal": "7ca36a6f-1092-11f1-82b2-7bf799245b7f",
#         "orderId": "AL260200066",
#         "paymentDate": "2026-02-23T00:00:00+0100",
#         "type": 3
#       }
#     ],
#     "orderedAt": "2026-02-23T09:37:35+0100",
#     "originalAmountTotalPaid": "48.49",
#     "originalAmountTotalWithTax": "48.49",
#     "originalAmountTotalWithoutTax": "44.90",
#     "originalCurrency": "PLN",
#     "paymentStatus": 2,
#     "paymentType": 3,
#     "platformAccountId": 2,
#     "platformId": 11,
#     "preferences": {
#       "idUser": "3133635",
#       "isSmart": true
#     },
#     "sendDateMax": "2026-02-24T00:00:00+0100",
#     "sendDateMin": null,
#     "status": 14,
#     "updatedAt": null
#   },
#   "last_sync": "2026-03-06T08:49:02.905821+00:00",
#   "model_name": "ApiloOrder",
#   "payment": {
#     "description": "serwis PayU.",
#     "id": 3,
#     "isBroker": null,
#     "key": "PAYMENT_TYPE_SERVICE_PAYU",
#     "name": "PayU",
#     "originalAmountTotalPaid": "48.49"
#   },
#   "processed_at": "2026-03-06T15:42:34.592337Z",
#   "processed_to_invoice": true,
#   "shipping_date": "2026-03-01",
#   "simple": {
#     "addressCustomer": {
#       "city": "Szczecin",
#       "class": "house",
#       "country": "PL",
#       "department": "70-117",
#       "email": "mwfhe51mjg+28d78da07@allegromail.pl",
#       "id": 12423,
#       "name": "Dorota Simankowicz",
#       "phone": "+48 538 209 693",
#       "streetName": "Milczańska",
#       "streetNumber": "6b/2",
#       "zipCode": "70-117"
#     },
#     "carrierId": 143,
#     "createdAt": "2026-02-23T09:43:55+0100",
#     "id": "AL260200066",
#     "idExternal": "7c51a0b0-1092-11f1-844a-5dc3fc9cc8e8",
#     "isCanceledByBuyer": false,
#     "isEncrypted": false,
#     "isInvoice": false,
#     "orderItems": [
#       {
#         "ean": "5903899665679",
#         "id": 12561,
#         "idExternal": "7c4c4980-1092-11f1-844a-5dc3fc9cc8e8",
#         "media": "https://a.allegroimg.com/s128/115659/0f1e6c294acfbcd2fa46ba4a0b3d",
#         "originalCode": "15290967388",
#         "originalName": "Chlorox S podchloryn sodu do dezynfekcji wody 6 kg",
#         "originalPriceWithTax": "48.49",
#         "originalPriceWithoutTax": "44.90",
#         "quantity": 1,
#         "sku": "15290967388",
#         "status": 1,
#         "tax": "8.00",
#         "type": 1,
#         "unit": null
#       },
#       {
#         "ean": null,
#         "id": 12564,
#         "idExternal": null,
#         "media": null,
#         "originalCode": "0b257488-c85d-4507-b967-9b45ffbfa2e8",
#         "originalName": "Allegro One Box, DPD",
#         "originalPriceWithTax": "0.00",
#         "originalPriceWithoutTax": "0.00",
#         "quantity": 1,
#         "sku": null,
#         "status": 1,
#         "tax": null,
#         "type": 2,
#         "unit": null
#       }
#     ],
#     "originalCurrency": "PLN",
#     "paymentStatus": 2,
#     "paymentType": 3,
#     "platformAccountId": 2,
#     "platformId": 11,
#     "status": 2,
#     "updatedAt": null
#   },
#   "status_zamowienia": "completed",
#   "sync_status": "PENDING",
#   "updated_at": "2026-03-02T23:30:16.250311Z",
#   "user_id": "375bed95-5a27-45e6-8093-9b56a0331c4e",
#   "sale_invoice_ref": "9f919fc1-b45d-45de-ad67-18db2960e443::SaleInvoice::LbUIRwsOZD4IPvrt-Rb2Cg"
# }
#
# SELECT COUNT(*) AS total_records
# FROM `Accounting`.`raw`.`apilo_order` d
# WHERE d.company_id = "offlite"
#   AND d.company_uuid = "9f919fc1-b45d-45de-ad67-18db2960e443"
#   AND d.simple.createdAt < "2026-03-01"