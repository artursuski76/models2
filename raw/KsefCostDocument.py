from typing import Optional, List
from datetime import datetime
from pydantic import Field, BaseModel, ConfigDict
from models2.abase import BasicBasic


# --- PODMODELE (Czysty BaseModel) ---

class IdentifierKsefCost(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str  # np. "Nip", "VatUe", "Other"
    value: str


class FormCodeKsef(BaseModel):
    model_config = ConfigDict(extra='ignore')
    systemCode: str
    schemaVersion: str
    value: str


class SellerKsefCostDoc(BaseModel):
    model_config = ConfigDict(extra='ignore')
    nip: str
    name: Optional[str] = None


class BuyerKsefCostDoc(BaseModel):
    model_config = ConfigDict(extra='ignore')
    identifier: IdentifierKsefCost
    name: Optional[str] = None


class ThirdSubjectKsef(BaseModel):
    model_config = ConfigDict(extra='ignore')
    identifier: IdentifierKsefCost
    name: Optional[str] = None
    role: int  # np. 5 w Twoim przykładzie


# --- MODEL GŁÓWNY (Dziedziczy po BasicBasic) ---

class KSeFCostDoc(BasicBasic):
    model_config = ConfigDict(extra='ignore')

    my_id: str = Field(
        title="Unikalny ID (np. Numer KSeF)",
        pattern=r"^[A-Z0-9\-]+$",
        json_schema_extra={"exclude_from_form": True}
    )

    # Pola z rekordu KSeF
    ksefNumber: Optional[str] = None
    invoiceNumber: Optional[str] = None
    issueDate: Optional[str] = None
    invoicingDate: Optional[str] = None
    acquisitionDate: Optional[str] = None
    permanentStorageDate: Optional[str] = None

    seller: SellerKsefCostDoc
    buyer: BuyerKsefCostDoc

    # Nowe pola znalezione w rekordzie
    formCode: Optional[FormCodeKsef] = None
    thirdSubjects: List[ThirdSubjectKsef] = []

    # Kwoty i waluty
    netAmount: float = 0.0
    grossAmount: float = 0.0
    vatAmount: float = 0.0
    currency: Optional[str] = "PLN"

    invoicingMode: Optional[str] = None
    invoiceType: Optional[str] = None
    isSelfInvoicing: bool = False
    hasAttachment: bool = False
    invoiceHash: Optional[str] = None

    class FormConfig:
        page_title = "Faktury kosztowe KSeF"
        header = "Lista faktur kosztowych KSeF"
        list_view_fields = [
            "seller.name", "issueDate", "invoiceNumber", "grossAmount",
            "currency", "invoiceType", "ksefNumber"
        ]
        default_sort_field = "issueDate"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "ksef_cost"