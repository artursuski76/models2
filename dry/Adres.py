from typing import Optional

from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

Adres = make_ksef_model_with_extras(
    "Adres",
    fields={
        "KodKraju": "TKodKraju",
        "AdresL1": "TZnakowy512",
        "AdresL2": Optional["TZnakowy512"]
    },
    field_extras={
        "KodKraju": {"title": "Kod kraju (np. PL)", "order": 1},
        "AdresL1": {"title": "Ulica, numer domu/lokalu", "order": 2},
        "AdresL2": {"title": "Kod pocztowy i miejscowość", "order": 3},
    }
)