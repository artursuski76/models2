from typing import Annotated, Union, Literal
from pydantic import Field
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

# 1. Podmiot Firma Krajowa (NIP)
PodmiotFirmaKrajowa = make_ksef_model_with_extras(
    "PodmiotFirmaKrajowa",
    fields={
        "typ_podmiotu": Literal["krajowy"],
        "NIP": "TNrNIP",
        "Nazwa": "TZnakowy512",
        "JST": "TWybor1_2",
        "GV": "TWybor1_2"
    },
    field_extras={
        "typ_podmiotu": {
            "title": "Typ podmiotu: Krajowy",
            "json_schema_extra": {"exclude_from_form": True}
        },
        "NIP": {
            "title": "Numer NIP",
            "json_schema_extra": {"order": 1}
        },
        "Nazwa": {
            "title": "Nazwa nabywcy (Firma lub Imię i Nazwisko)",
            "json_schema_extra": {"order": 2}
        },
        "JST": {
            "title": "Czy jednostka podrzędna JST?",
            "json_schema_extra": {"order": 3}
        },
        "GV": {
            "title": "Czy członek grupy VAT?",
            "json_schema_extra": {"order": 4}
        },
    }
)

# 2. Podmiot Firma UE
PodmiotFirmaUE = make_ksef_model_with_extras(
    "PodmiotUE",
    fields={
        "typ_podmiotu": Literal["ue"],
        "KodUE": "TKodyKrajowUE",
        "NrVatUE": "TNrVatUE",
        "Nazwa": "TZnakowy512"
    },
    field_extras={
        "typ_podmiotu": {
            "title": "Typ podmiotu: UE",
            "json_schema_extra": {"exclude_from_form": True}
        },
        "KodUE": {
            "title": "Kod kraju członkowskiego UE",
            "json_schema_extra": {"order": 1}
        },
        "NrVatUE": {
            "title": "Numer VAT UE (bez kodu kraju)",
            "json_schema_extra": {"order": 2}
        },
        "Nazwa": {
            "title": "Nazwa nabywcy z UE",
            "json_schema_extra": {"order": 3}
        },
    }
)

PodmiotFirmaZagraniczna = make_ksef_model_with_extras(
    "PodmiotFirmaZagraniczna",
    fields={
        "typ_podmiotu": Literal["zagraniczny"],
        "KodKraju": "TKodKraju",
        "NrID": "TZnakowy50",
        "Nazwa": "TZnakowy512"
    },
    field_extras={
        "typ_podmiotu": {
            "title": "Typ podmiotu: Zagraniczny (poza UE)",
            "json_schema_extra": {"exclude_from_form": True}
        },
        "KodKraju": {
            "title": "Kod kraju (ISO 3166)",
            "json_schema_extra": {"order": 1}
        },
        "NrID": {
            "title": "Numer identyfikacyjny (VAT ID / Business ID)",
            "json_schema_extra": {"order": 2}
        },
        "Nazwa": {
            "title": "Nazwa nabywcy zagranicznego",
            "order": 3
        },
    }
)

# 4. Podmiot Brak ID (np. osoba fizyczna / brak numeru)
PodmiotBrakID = make_ksef_model_with_extras(
    "PodmiotBrakID",
    fields={
        "typ_podmiotu": Literal["brak_id"],
        "BrakID": "BrakID_Literal1",
        "Nazwa": "TZnakowy512"
    },
    field_extras={
        "typ_podmiotu": {
            "title": "Typ podmiotu: Osoba fizyczna / Brak ID",
            "json_schema_extra": {"exclude_from_form": True}
        },
        "BrakID": {
            "title": "Brak identyfikatora",
            "json_schema_extra": {"exclude_from_form": True}
        },
        "Nazwa": {
            "title": "Imię i Nazwisko / Nazwa nabywcy",
            "json_schema_extra": {"order": 2}
        },
    }
)

# Definicja Nabywcy z użyciem diskryminatora dla Pydantic i JSON Schema
Podmiot2 = Annotated[
    Union[PodmiotFirmaKrajowa, PodmiotFirmaZagraniczna, PodmiotFirmaUE, PodmiotBrakID],
    Field(discriminator="typ_podmiotu", title="Dane Nabywcy")
]