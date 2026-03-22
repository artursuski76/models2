from typing import Annotated, Union, Literal
from pydantic import Field

from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

# 1. Podmiot Firma Krajowa (NIP)
PodmiotFirmaKrajowa = make_ksef_model_with_extras(
    "PodmiotFirmaKrajowa",
    fields={
        "typ_podmiotu": Literal["krajowy"], # Stała wartość dla tego modelu
        "NIP": "TNrNIP",
        "Nazwa": "TZnakowy512"
    },
    field_extras={
        "typ_podmiotu": {"json_schema_extra": {"exclude_from_form": True}}, # Ukrywamy w samym formularzu jako pole tekstowe
        "NIP": {"json_schema_extra": {"order": 1}},
        "Nazwa": {"json_schema_extra": {"order": 2}},
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
        "typ_podmiotu": {"json_schema_extra": {"exclude_from_form": True}},
        "KodUE": {"json_schema_extra": {"order": 1}},
        "NrVatUE": {"json_schema_extra": {"order": 2}},
        "Nazwa": {"json_schema_extra": {"order": 3}},
    }
)

# 3. Podmiot Firma Zagraniczna
PodmiotFirmaZagraniczna = make_ksef_model_with_extras(
    "PodmiotFirmaZagraniczna",
    fields={
        "typ_podmiotu": Literal["zagraniczny"],
        "KodKraju": "TKodKraju",
        "NrID": "TZnakowy50",
        "Nazwa": "TZnakowy512"
    },
    field_extras={
        "typ_podmiotu": {"json_schema_extra": {"exclude_from_form": True}},
        "KodKraju": {"json_schema_extra": {"order": 1}},
        "NrID": {"json_schema_extra": {"order": 2}},
        "Nazwa": {"json_schema_extra": {"order": 3}},
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
        "typ_podmiotu": {"json_schema_extra": {"exclude_from_form": True}},
        "BrakID": {"json_schema_extra": {"exclude_from_form": True}},
        "Nazwa": {"json_schema_extra": {"order": 2}},
    }
)

Podmiot2 = Annotated[
    Union[PodmiotFirmaKrajowa, PodmiotFirmaZagraniczna, PodmiotFirmaUE, PodmiotBrakID],
    Field(discriminator="typ_podmiotu")
]