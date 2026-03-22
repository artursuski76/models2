from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

DodatkowyOpis = make_ksef_model_with_extras(
    "DodatkowyOpis",
    fields={
        "Klucz": "TZnakowy",
        "Wartosc": "TTekstowy",
    }
)