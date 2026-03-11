from typing import Optional

from models2.abase import BasicBasic


class KsefSaleInvoice(BasicBasic):
    saleInvoiceId: str
    ksefNumber: Optional[str]
    sessionReferenceNumber: str
    invoiceReferenceNumber: str
    statusCode: str
    hasUpo: bool = False
    upoFileKey: Optional[str] = None

class Couchbase:
    bucket = "Accounting"
    scope = "services"
    collection = "ksef_sale_invoice"
