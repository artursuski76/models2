from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras


Podmiot1 = make_ksef_model_with_extras(
    "PodmiotPL",
    fields={
        "NIP": "TNrNIP",
        "Nazwa": "TZnakowy512"
    },
    field_extras={
        "NIP": {"json_schema_extra": {"exclude_from_form": True, "order": 1}},
        "Nazwa": {"json_schema_extra": {"exclude_from_form": True, "order": 2}},
    }
)