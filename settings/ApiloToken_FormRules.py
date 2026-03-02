# AUTO-GENERATED FORM RULES
# Generated from models2/settings/ApiloToken.py

FORM_RULES = {
    "last_sync": { "type": "optional<datetime>", "required": False, "visibleIf": {'sync_status': 'EXPECTED_VALUE'}, "label": "Data ostatniej synchronizacji" },
    "sync_status": { "type": "SyncStatus", "required": False, "visibleIf": {}, "label": "Status synchronizacji", "options": ['OK', 'ERROR', 'PENDING'] },
    "last_error": { "type": "optional<str>", "required": False, "visibleIf": {'sync_status': 'EXPECTED_VALUE'}, "label": "Ostatni błąd" },
    "endpoint": { "type": "str", "required": True, "visibleIf": {}, "label": "Endpoint API" },
    "client_id": { "type": "optional<str>", "required": True, "visibleIf": {}, "label": "client_id" },
    "client_secret": { "type": "optional<str>", "required": True, "visibleIf": {}, "label": "client_secret" },
    "authorize_code": { "type": "optional<str>", "required": True, "visibleIf": {}, "label": "authorize_code" },
    "waznosc_do": { "type": "optional<str>", "required": True, "visibleIf": {}, "label": "waznosc_do" },
    "access_token": { "type": "optional<str>", "required": False, "visibleIf": {'sync_status': 'EXPECTED_VALUE'}, "label": "access_token", "alias": "accessToken" },
    "at_expires_at": { "type": "optional<str>", "required": False, "visibleIf": {'sync_status': 'EXPECTED_VALUE'}, "label": "at_expires_at", "alias": "atExpiresAt" },
    "refresh_token": { "type": "optional<str>", "required": False, "visibleIf": {'sync_status': 'EXPECTED_VALUE'}, "label": "refresh_token", "alias": "refreshToken" },
    "rt_expires_at": { "type": "optional<str>", "required": False, "visibleIf": {'sync_status': 'EXPECTED_VALUE'}, "label": "rt_expires_at", "alias": "tokenExpiresAt" },
    "status_for_inv": { "type": "optional<int>", "required": False, "visibleIf": {}, "label": "Status Apilo Order do automatycznych faktur" },
    "payment_status_for_counterparty": { "type": "optional<int>", "required": False, "visibleIf": {}, "label": "Status patności dla tworzenia kontrahenta" },
}
