from typing import Literal, Optional
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

Naglowek = make_ksef_model_with_extras(
    "Naglowek",
    fields={
        "KodFormularza": Literal["FA"],
        "WariantFormularza": Literal[3],
        "DataWytworzeniaFa": "TDataCzas",
        "SystemInfo": Optional["TZnakowy"]
    },
    field_extras={
        "KodFormularza": {
            "title": "Kod Formularza",
            "json_schema_extra": {"order": 1}
        },
        "WariantFormularza": {
            "title": "Wariant Formularza",
            "json_schema_extra": {"order": 2}
        },
        "DataWytworzeniaFa": {
            "title": "Data i czas wytworzenia faktury",
            "json_schema_extra": {"order": 3}
        },
        "SystemInfo": {
            "title": "Nazwa systemu (System Info)",
            "json_schema_extra": {"order": 4}
        }
    }
)