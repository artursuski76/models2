from typing import Optional

from models2.abase import BasicBasic


class KsefSaleInvoice(BasicBasic):
    saleInvoiceId: str
    ksefNumber: Optional[str] = None
    sessionReferenceNumber: str
    invoiceReferenceNumber: Optional[str] = None
    referenceNumber: Optional[str] = None
    invoiceNumber: Optional[str] = None
    ordinalNumber: Optional[int] = None
    invoiceHash: Optional[str] = None
    acquisitionDate: Optional[str] = None
    invoicingDate: Optional[str] = None
    permanentStorageDate: Optional[str] = None
    upoDownloadUrl: Optional[str] = None
    upoDownloadUrlExpirationDate: Optional[str] = None
    invoicingMode: Optional[str] = None
    statusCode: str
    statusDescription: Optional[str] = None
    hasUpo: bool = False
    upoFileKey: Optional[str] = None

class Couchbase:
    bucket = "Accounting"
    scope = "services"
    collection = "ksef_sale_invoice"
