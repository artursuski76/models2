import datetime
from enum import Enum
from pydantic import Field
from typing import Optional

# Zakładam, że BasicBasic dostarcza podstawowej funkcjonalności modelu
from models2.abase import BasicBasic


class SyncStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"
    PENDING = "PENDING"


class ApiloToken(BasicBasic):
    __auto_id__ = False

    model_name: str = Field(
        "ApiloToken",
        json_schema_extra={"exclude_from_form": True}
    )

    # Rozszerzony wzorzec, by opcjonalnie zawierał NIP
    my_id: str = Field(
        default="Settings",
        title="Unikalny ID",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        json_schema_extra={"exclude_from_form": True}
    )

    last_sync: Optional[datetime.datetime] = Field(None, title="Data ostatniej synchronizacji")
    sync_status: SyncStatus = Field(default=SyncStatus.PENDING, title="Status synchronizacji")
    last_error: Optional[str] = Field(None, title="Ostatni błąd", description="Treść błędu z API KSeF, jeśli wystąpił")

    endpoint: str = Field(
        ...,
        title="Endpoint API",
        description="Adres URL API APIlo"
    )
    client_id: Optional[str] = Field()
    client_secret: Optional[str] = Field()
    authorize_code: Optional[str] = Field()
    waznosc_do: Optional[str] = Field()

    access_token: Optional[str] = Field(None, alias="accessToken")
    at_expires_at: Optional[str] = Field(None, alias="atExpiresAt")
    refresh_token: Optional[str] = Field(None, alias="refreshToken")
    rt_expires_at: Optional[str] = Field(None, alias="tokenExpiresAt")

    status_for_inv: Optional[int] = Field(None, title="Status Apilo Order do automatycznych faktur", json_schema_extra={"exclude_from_visibility_logic": True})
    payment_status_for_counterparty: Optional[int] = Field(None, title="Status patności dla tworzenia kontrahenta", json_schema_extra={"exclude_from_visibility_logic": True})

    class FormConfig:
        prefill_initial_data = True
        list_view_fields = [
            "last_sync", "sync_status"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "settings"
        collection = "ksef_token"