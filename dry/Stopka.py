from pydantic import BaseModel, Field
from typing import Optional, List
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

# 1. Informacje dodatkowe (np. stopka tekstowa)
Informacje = make_ksef_model_with_extras(
    "Informacje",
    fields={
        "StopkaFaktury": "TTekstowy",
    },
    field_extras={
        "StopkaFaktury": {
            "title": "Treść dodatkowa w stopce (np. marketingowa, informacyjna)",
            "json_schema_extra": {"order": 1}
        }
    }
)

# 2. Dane z rejestrów (KRS, REGON, BDO)
Rejestry = make_ksef_model_with_extras(
    "Rejestry",
    fields={
        "PelnaNazwa": "TZnakowy",
        "KRS": "TNrKRS",
        "REGON": "TNrREGON",
        "BDO": "TZnakowy9",
    },
    field_extras={
        "PelnaNazwa": {"title": "Pełna nazwa organu rejestrowego", "order": 1},
        "KRS": {"title": "Numer KRS", "order": 2},
        "REGON": {"title": "Numer REGON", "order": 3},
        "BDO": {"title": "Numer BDO", "order": 4},
    }
)

# 3. Model Stopka (Klasyczny Pydantic)
class Stopka(BaseModel):
    # Używamy List[Informacje], ponieważ KSeF pozwala na wielokrotne wystąpienie tych sekcji
    informacje: Optional[List[Informacje]] = Field(
        None,
        validation_alias="Informacje",
        serialization_alias="Informacje",
        title="Informacje dodatkowe",
        description="Dodatkowe informacje tekstowe umieszczane w stopce dokumentu"
    )
    rejestry: Optional[List[Rejestry]] = Field(
        None,
        validation_alias="Rejestry",
        serialization_alias="Rejestry",
        title="Dane z rejestrów",
        description="Informacje o wpisach do KRS, REGON lub BDO"
    )