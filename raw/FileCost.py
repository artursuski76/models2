import secrets
from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel
from pydantic import Field

from models2.abase import BasicBasic
from models2.enums import SourceInvoiceStatus, InvoiceType, SourceInvoiceSource
from models2.xxx.h_files import TransactionFiles


class InvoiceItem(BaseModel):
    name: Optional[str]
    quantity: Optional[float]
    unit: Optional[str]
    unit_price_net: Optional[float]
    unit_price_gross: Optional[float]
    net: Optional[float]
    vat: Optional[float]
    gross: Optional[float]
    vat_rate: Optional[str]
    cn: Optional[str]
    fuel_type: Optional[str]

class InvoiceTransactionType(str, Enum):
    DOMESTIC = "domestic"
    EU_VAT = "eu_vat"
    NON_EU = "non_eu"
    INDIVIDUAL = "individual"

class FileCostSeller(BaseModel):
    name: Optional[str]

    # Rodzaj podatnika
    type: InvoiceTransactionType  # 'domestic', 'eu_vat', 'non_eu', 'individual'

    # Identyfikatory
    nip: Optional[str]  # dla krajowego podatnika
    vat_ue: Optional[str]  # dla transakcji wewnątrzunijnej
    tax_id: Optional[str]  # dla import/export spoza UE

    # Kod kraju (ISO 3166-1 alpha-2)
    country_code: Optional[str]  # PL, DE, FR, US etc.


class Invoice(BaseModel):
    type: InvoiceTransactionType
    invoice_number: Optional[str]
    issue_date: Optional[date]
    sale_date: Optional[date]

    seller: Optional[FileCostSeller]
    buyer: Optional[FileCostSeller]

    items: List[InvoiceItem]

    total_net: Optional[float]
    total_vat: Optional[float]
    total_gross: Optional[float]

class FileCost(BasicBasic):
    model_name: str = Field(
        "FileCost",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(  # Zmieniono z UUID na str
        default_factory=lambda: secrets.token_urlsafe(16),
        json_schema_extra={"exclude_from_form": True}
    )

    inv_type: InvoiceType = Field(
        InvoiceType.PURCHASE,
        alias="TypFaktury",
        json_schema_extra={"exclude_from_form": True}
    )

    files: List[TransactionFiles] = Field(default_factory=list)

    status: SourceInvoiceStatus = Field(
        SourceInvoiceStatus.DRAFT,
        title="Status",
        json_schema_extra = {"exclude_from_form": True}
    )

    source: SourceInvoiceSource = Field(
        SourceInvoiceSource.MANUAL,
        title="Zródło",
        json_schema_extra={"exclude_from_form": True}
    )

    ocr_text: str = Field(
        default="",
        title="Tekst OCR",
        description="Tekst wykryty przez OCR",
        json_schema_extra={"exclude_from_form": True}
    )

    ocr_status: str = Field(
        default="",
        title="Status OCR",
        description="Status przetwarzania OCR",
        json_schema_extra={"exclude_from_form": True}
    )

    openai_status: str = Field(
        default="",
        title="Status OpenAI",
        description="Status przetwarzania OpenAI",
        json_schema_extra={"exclude_from_form": True}
    )

    invoice: Optional[Invoice] = Field(
        default=None,
        json_schema_extra={"exclude_from_form": True}
    )


    class FormConfig:
        page_title = "Koszty FileCost"
        header = "Lista kosztów FileCost"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "model_name", "my_id", "files", "created_at", "invoice.seller.name", "invoice.buyer.name",
            "invoice.total_gross", "invoice.invoice_number", "invoice.sale_date"
        ]
        default_sort_field = "created_at"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "file_cost"

