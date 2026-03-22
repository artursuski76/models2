from pydantic import BaseModel, Field
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras


Informacje = make_ksef_model_with_extras(
    "Informacje",
    fields={
        "StopkaFaktury": "TTekstowy",
    }
)


Rejestry = make_ksef_model_with_extras(
    "Rejestry",
    fields={
        "PelnaNazwa": "TZnakowy",
        "KRS": "TNrKRS",
        "REGON": "TNrREGON",
        "BDO": "TZnakowy9",
    }
)


class Stopka(BaseModel):
    informacje: list[Informacje] | None = Field(None, validation_alias="Informacje", serialization_alias="Informacje", description="Informacje o stopce")
    rejestry: list[Rejestry] | None = Field(None, validation_alias="Rejestry", serialization_alias="Rejestry", description="Rejestry")
