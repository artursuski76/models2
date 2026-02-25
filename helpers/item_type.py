from typing import Literal, Optional

from pydantic import BaseModel, Field

from models2.enums import ValuationMethod
from models2.helpers.deduction import Deduction


class PozycjaMagazynowa(BaseModel):
    item_type: Literal["Pozycja_Magazynowa"] = Field(
        "Pozycja_Magazynowa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    valuation_method: ValuationMethod = Field(
        ValuationMethod.FIFO,
        title = "Metoda wyceny*",
        alias="valuation_method"
    )

class SrodekTrwaly(BaseModel):
    item_type: Literal["Srodek_Trwaly"] = Field(
        "Srodek_Trwaly",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    deduction_vat: Optional[float] = Field(
        default=100,
        alias="deduction_VAT"
    )
    deduction_cit: Optional[float] = Field(
        default=100
    )
    nierozl_vat_w_cit: bool = Field(default=True, alias="Nierozliczony VAT rozlicz w CIT")


class RzeczUzytkowana(BaseModel):
    item_type: Literal["Rzecz_Uzytkowana"] = Field(
        "Rzecz_Uzytkowana",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    deduction_vat: Optional[float] = Field(
        default=100,
        alias="deduction_VAT"
    )
    deduction_cit: Optional[float] = Field(
        default=100
    )
    nierozl_vat_w_cit: bool = Field(default=True, alias="Nierozliczony VAT rozlicz w CIT")



class LicencjePrawa(BaseModel):
    item_type: Literal["Licencje_Prawa"] = Field(
        "Licencje_Prawa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class ProduktWlasny(BaseModel):
    item_type: Literal["Produkt_Wlasny"] = Field(
        "Produkt_Wlasny",
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
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class Produkt(Deduction):
    item_type: Literal["Produkt"] = Field(
        "Produkt",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
