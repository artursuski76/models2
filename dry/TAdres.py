from typing import Optional
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

TAdres = make_ksef_model_with_extras(
    "TAdres",
    fields={
        "KodKraju": "TKodKraju",
        "AdresL1": "TZnakowy512",
        "AdresL2": Optional["TZnakowy512"],
        "GLN": Optional["TGLN"],
    },
    field_extras={
        "KodKraju": {"title": "Kod Kraju", "order": 1},
        "AdresL1": {"title": "Ulica, nr domu, nr lokalu / Adres linia 1", "order": 2},
        "AdresL2": {"title": "Miejscowość, kod pocztowy / Adres linia 2", "order": 3},
        "GLN": {"title": "Globalny Numer Lokalizacyjny (GLN)", "order": 4},
    }
)
