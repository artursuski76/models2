from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras


Podmiot1 = make_ksef_model_with_extras(
    "PodmiotPL",
    fields={
        "NIP": "TNrNIP",
        "Nazwa": "TZnakowy512"
    },
    field_extras={
        "NIP": {
            "title": "Numer Identyfikacji Podatkowej (NIP)",
            "json_schema_extra": {
                "exclude_from_form": False,
                "order": 1
            }
        },
        "Nazwa": {
            "title": "Pełna nazwa firmy / Imię i nazwisko",
            "json_schema_extra": {
                "exclude_from_form": False,
                "order": 2
            }
        },
    }
)