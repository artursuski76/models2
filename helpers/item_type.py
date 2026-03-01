from typing import Literal

from pydantic import BaseModel
from pydantic import Field

from models2.enums import ValuationMethod
from models2.references.SrodekTransportu.VehicleTaxProfile import VehicleTaxProfile


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

class SrodekTrwalyTransportowy(VehicleTaxProfile):
    item_type: Literal["srodek_trwaly_transportowy"] = Field(
        "srodek_trwaly_transportowy",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )



class UzytkowanaRzecz(BaseModel):
    item_type: Literal["uzytkowana_rzecz"] = Field(
        "uzytkowana_rzecz",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
    )

class UzytkowanaRzeczTransportowa(VehicleTaxProfile):
    item_type: Literal["uzytkowana_rzecz_transportowa"] = Field(
        "uzytkowana_rzecz_transportowa",
        alias="typ_transakcji",
        json_schema_extra={"exclude_from_form": True}
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
