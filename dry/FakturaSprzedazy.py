from pydantic import ConfigDict, Field, AliasChoices

from models2.dry.Fa import Fa
from models2.dry.Podmiot1 import Podmiot1
from models2.dry.Podmiot2 import Podmiot2
from models2.dry.Stopka import Stopka
from models2.dry.base import BaseX
from models3.Fa3.Naglowek import Naglowek


class FakturaSprzedazy(BaseX):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    naglowek: Naglowek = Field(
        validation_alias=AliasChoices("Naglowek", "naglowek"),
        serialization_alias="Naglowek"
    )
    podmiot1: Podmiot1 = Field(
        validation_alias=AliasChoices("Podmiot1", "podmiot1"),
        serialization_alias="Podmiot1"
    )
    podmiot2: Podmiot2 = Field(
        validation_alias=AliasChoices("Podmiot2", "podmiot2"),
        serialization_alias="Podmiot2"
    )
    fa: Fa = Field(
        validation_alias=AliasChoices("Fa", "fa"),
        serialization_alias="Fa"
    )
    stopka: Stopka = Field(
        validation_alias=AliasChoices("Stopka", "stopka"),
        serialization_alias="Stopka"
    )

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "sale_invoice"