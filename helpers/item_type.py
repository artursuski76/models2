from typing import Literal, Optional

from pydantic import BaseModel, Field

from models2.enums import ValuationMethod
from models2.helpers.deduction import Deduction

class DeductionCitVat(BaseModel):
    deduction_vat: Optional[float] = Field(
        default=100,
        alias="deduction_vat"
    )
    deduction_cit: Optional[float] = Field(
        default=100
    )
    nierozl_vat_w_cit: bool = Field(default=True, title="Nierozliczony VAT rozlicz w CIT")

class PozycjaMagazynowa(BaseModel):
    item_type: Literal["Pozycja_Magazynowa"] = Field(
        "Pozycja_Magazynowa",
        alias="typ_transakcji",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    valuation_method: ValuationMethod = Field(
        ValuationMethod.FIFO,
        title = "Metoda wyceny*",
        alias="valuation_method"
    )

class SrodekTrwaly(DeductionCitVat):
    item_type: Literal["Srodek_Trwaly"] = Field(
        "Srodek_Trwaly",
        alias="typ_transakcji",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class RzeczUzytkowana(DeductionCitVat):
    item_type: Literal["Rzecz_Uzytkowana"] = Field(
        "Rzecz_Uzytkowana",
        alias="typ_transakcji",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class LicencjePrawa(BaseModel):
    item_type: Literal["Licencje_Prawa"] = Field(
        "Licencje_Prawa",
        alias="typ_transakcji",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class ProduktWlasny(BaseModel):
    item_type: Literal["Produkt_Wlasny"] = Field(
        "Produkt_Wlasny",
        alias="typ_transakcji",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    valuation_method: ValuationMethod = Field(
        ValuationMethod.FIFO,
        title = "Metoda wyceny*",
        alias="valuation_method"
    )


class Usluga(Deduction):
    item_type: Literal["Usluga"] = Field(
        "Usluga",
        alias="typ_transakcji",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )



class Produkt(Deduction):
    item_type: Literal["Produkt"] = Field(
        "Produkt",
        alias="typ_transakcji",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
