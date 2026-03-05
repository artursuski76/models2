from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel


class TransactionFiles(BaseModel):
    status: str = Field(description="status", json_schema_extra={"exclude_from_form": True})
    filename: str = Field(description="filename")  # pojawi się w formularzu
    minio_key: str = Field(description="Plik - key")
    minio_bucket: str = Field(description="Plik - bucket", json_schema_extra={"exclude_from_form": True})
    minio_url: Optional[str] = Field(default=None, description="Plik - url", json_schema_extra={"exclude_from_form": True})
    uploaded_at: Optional[datetime] = Field(default=None, description="uploaded_at", json_schema_extra={"exclude_from_form": True})
    file_size: Optional[int] = Field(default=None, description="file_size", json_schema_extra={"exclude_from_form": True})
    checksum: Optional[str] = Field(default=None, description="checksum", json_schema_extra={"exclude_from_form": True})