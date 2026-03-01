from typing import Literal

from pydantic import BaseModel
from pydantic import Field

from models2.enums import ValuationMethod




class PozycjaMagazynowa(BaseModel):
    item_type: Literal["pozycja_magazynowa"] = Field(
        "pozycja_magazynowa",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )

    valuation_method: ValuationMethod = Field(
        ValuationMethod.FIFO,
        title="Metoda wyceny"
    )


class SrodekTrwaly(BaseModel):
    item_type: Literal["srodek_trwaly"] = Field(
        "srodek_trwaly",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )


class SrodekTrwalyTransportu(SrodekTransportu):
    item_type: Literal["srodek_trwaly_transportu"] = Field(
        "srodek_trwaly_transportu",
        alias="typ_transakcji"
    )



class UzytkowanaRzecz(BaseModel):
    item_type: Literal["uzytkowana_rzecz"] = Field(
        "uzytkowana_rzecz",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )


class UzytkowanySrodekTransportu(SrodekTransportu):
    item_type: Literal["uzytkowany_srodek_transportu"] = Field(
        "uzytkowany_srodek_transportu",
        alias="typ_transakcji"
    )


class WartosciNiematerialneIPrawne(BaseModel):
    item_type: Literal["wartosci_niematerialne_i_prawne"] = Field(
        "wartosci_niematerialne_i_prawne",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )


class ProduktWlasny(BaseModel):
    item_type: Literal["produkt_wlasny"] = Field(
        "produkt_wlasny",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )

    valuation_method: ValuationMethod = Field(
        ValuationMethod.FIFO,
        title="Metoda wyceny"
    )

class Produkt(BaseModel):
    item_type: Literal["produkt"] = Field(
        "produkt",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )

class Usluga(BaseModel):
    item_type: Literal["usluga"] = Field(
        "usluga",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )

class NieruchomosciWlasne(BaseModel):
    item_type: Literal["budynki_lokalne"] = Field(
        "budynki_lokale_wlasne",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )

class NieruchomosciNajmowane(BaseModel):
    item_type: Literal["budynki_lokalne"] = Field(
        "budynki_lokale_najmowane",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )
