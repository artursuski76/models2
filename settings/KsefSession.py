from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import Field
from models2.abase import BasicBasic

class KsefSessionStatus(BasicBasic):
    code: int
    description: str

class KsefSession(BasicBasic):
    model_name: str = Field("KsefSession", json_schema_extra={"exclude_from_form": True})
    
    referenceNumber: str = Field(..., title="Numer referencyjny sesji")
    status: Dict[str, Any] = Field(..., title="Status sesji")
    dateCreated: Optional[str] = Field(None, title="Data utworzenia")
    dateUpdated: Optional[str] = Field(None, title="Data aktualizacji")
    validUntil: Optional[str] = Field(None, title="Ważna do")
    
    totalInvoiceCount: Optional[int] = Field(0, title="Całkowita liczba faktur")
    successfulInvoiceCount: Optional[int] = Field(0, title="Liczba poprawnych faktur")
    failedInvoiceCount: Optional[int] = Field(0, title="Liczba odrzuconych faktur")
    
    type: str = Field("ksef_session", title="Typ dokumentu")

    class Couchbase:
        bucket = "Accounting"
        scope = "services"
        collection = "ksef_session"
