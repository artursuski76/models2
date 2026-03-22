from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

Naglowek = make_ksef_model_with_extras(
    "Naglowek",
    fields={
        "KodFormularza": "TZnakowy50",
        "WariantFormularza": "TZnakowy50",
        "DataWytworzeniaFa": "TDataCzas",
        "SystemInfo": "TZnakowy50"
    },
    field_extras={
        "KodFormularza": {"json_schema_extra": {"order": 1}},
        "WariantFormularza": {"json_schema_extra": {"order": 2}},
        "DataWytworzeniaFa": {"json_schema_extra": {"order": 3}},
        "SystemInfo": {"json_schema_extra": {"order": 4}}
    }
)