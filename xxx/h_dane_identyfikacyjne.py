from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict, AliasChoices

from models2.xxx.h_enums import EuropeLandsEnum, WorldLandsEnum
from models2.enums import CounterpartyType


class ZagraniczneFirmoweDaneIdentyfikacyjne(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    nazwa: str = Field(
        ...,
        validation_alias=AliasChoices( "Nazwa", "nazwa" ),
        serialization_alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    kod_ue: EuropeLandsEnum = Field(
        None,
        validation_alias=AliasChoices( "KodUE", "kod_ue" ),
        serialization_alias="KodUE",
        title="VIESS – kod UE"
    )
    nr_vat_ue: Optional[str] = Field(
        None,
        validation_alias=AliasChoices( "NrVatUE", "nr_vat_ue" ),
        serialization_alias="NrVatUE",
        title="VIESS – nr identyfikacyjny bez kodu kraju"
    )

    kod_kraju: WorldLandsEnum = Field(
        None,
        validation_alias=AliasChoices( "KodKraju", "kod_kraju" ),
        serialization_alias="KodKraju",
        title="EKSPORT – kod kraju"
    )
    tax_id: str = Field(
        None,
        validation_alias=AliasChoices( "NrID", "tax_id" ),
        serialization_alias="NrID",
        title="EKSPORT – Numer podatkowy"
    )

class OsobaFizyczna(BaseModel):
    rodzaj_kontr: Literal["osoba_fizyczna"] = Field(
        "osoba_fizyczna",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )
    brak_id: str = Field(
        default="1",
        validation_alias=AliasChoices( "BrakID", "brak_id" ),
        serialization_alias="BrakID",
        description="znacznik braku ID",
        json_schema_extra={"exclude_from_form": True}
    )
    nazwa: str = Field(
        ...,
        validation_alias=AliasChoices( "Nazwa", "nazwa" ),
        serialization_alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )

    type: CounterpartyType = Field(
        CounterpartyType,
        validation_alias=AliasChoices( "Typ", "type"),
        serialization_alias="Typ",
        title="Typ"
    )

class PodatnikKrajowy(BaseModel):
    rodzaj_kontr: Literal["podatnik_krajowy"] = Field(
        "podatnik_krajowy",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )

    nazwa: str = Field(
        ...,
        validation_alias=AliasChoices( "Nazwa", "nazwa" ),
        serialization_alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    nip: str = Field(
        ...,
        validation_alias=AliasChoices( "NIP", "nip"),
        serialization_alias="NIP",
        title="NIP",
        min_length=10,
        max_length=10,
        pattern=r'^\d{10}$|^brak$'
    )
    type: CounterpartyType = Field(
        CounterpartyType,
        validation_alias=AliasChoices( "Typ", "type"),
        serialization_alias="Typ",
        title="Typ"
    )

class PodatnikVIES(ZagraniczneFirmoweDaneIdentyfikacyjne):
    rodzaj_kontr: Literal["podatnik_vies"] = Field(
        "podatnik_vies",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )

    nazwa: str = Field(
        ...,
        validation_alias=AliasChoices( "Nazwa", "nazwa" ),
        serialization_alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    type: CounterpartyType = Field(
        CounterpartyType,
        validation_alias=AliasChoices("Typ", "type"),
        serialization_alias="Typ",
        title="Typ"
    )
class PodatnikZagraniczny(ZagraniczneFirmoweDaneIdentyfikacyjne):
    rodzaj_kontr: Literal["podatnik_zagraniczny"] = Field(
        "podatnik_zagraniczny",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )

    nazwa: str = Field(
        ...,
        validation_alias=AliasChoices( "Nazwa", "nazwa" ),
        serialization_alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    type: CounterpartyType = Field(
        CounterpartyType,
        validation_alias=AliasChoices("Typ", "type"),
        serialization_alias="Typ",
        title="Typ"
    )



class UrzadSkarbowy(BaseModel):
    rodzaj_kontr: Literal["urzad_skarbowy"] = Field(
        "urzad_skarbowy",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    nazwa_urzedu: str = Field(
        None,
        validation_alias=AliasChoices( "NazwaUrzedu", "nazwa_urzedu" ),
        serialization_alias="NazwaUrzedu",
        title="Nazwa urzędu"
    )

class Pracownik(BaseModel):
    rodzaj_kontr: Literal["pracownik"] = Field(
        "pracownik",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    imie: str = Field(
        None,
        title="Imię"
    )
    nazwisko: str = Field(
        None,
        title="Nazwisko"
    )
    data_ur: date = Field(
        None,
        title="Data ur."
    )

class CzlonekZarzadu(BaseModel):
    rodzaj_kontr: Literal["czlonek_zarzadu"] = Field(
        "czlonek_zarzadu",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    imie: str = Field(
        None,
        title="Imię"
    )
    nazwisko: str = Field(
        None,
        title="Nazwisko"
    )
    data_ur: date = Field(
        None,
        title="Data ur."
    )