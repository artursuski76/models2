from pydantic import ConfigDict, Field, AliasChoices

from .Fa import Fa
from .Podmiot1 import Podmiot1
from .Podmiot2 import Podmiot2
from .Stopka import Stopka
from .base import BaseX
from models3.Fa3.Naglowek import Naglowek


class FakturaSprzedazy(BaseX):
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True
    )

    naglowek: Naglowek = Field(
        validation_alias=AliasChoices("Naglowek", "naglowek"),
        serialization_alias="Naglowek",
        title="Nagłówki systemowe"
    )
    podmiot1: Podmiot1 = Field(
        validation_alias=AliasChoices("Podmiot1", "podmiot1"),
        serialization_alias="Podmiot1",
        title="Sprzedawca"
    )
    podmiot2: Podmiot2 = Field(
        validation_alias=AliasChoices("Podmiot2", "podmiot2"),
        serialization_alias="Podmiot2",
        title="Nabywca"
    )
    fa: Fa = Field(
        validation_alias=AliasChoices("Fa", "fa"),
        serialization_alias="Fa",
        title="Dane merytoryczne faktury"
    )
    stopka: Stopka = Field(
        validation_alias=AliasChoices("Stopka", "stopka"),
        serialization_alias="Stopka",
        title="Stopka dokumentu"
    )

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "sale_invoice"

# Bardzo ważne dla Pydantic v2 przy dynamicznych modelach:
FakturaSprzedazy.model_rebuild()