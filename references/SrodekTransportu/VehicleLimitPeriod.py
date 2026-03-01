from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class TaxLimitType(str, Enum):
    SAMOCHOD_OSOBOWY_SPALINOWY = "sam_osobowy_spalinowy"
    SAMOCHOD_OSOBOWY_PLUGIN_DO_50G = "sam_osobowy_plugin_do_50g"
    SAMOCHOD_OSOBOWY_ELEKTRYCZNY = "sam_osobowy_elektryczny"
    BEZ_LIMITU = "bez_limitu"

class TaxUzytkowanieAuta(str, Enum):
    TYLKO_FIRMOWO = "tylko_firmowo"
    TYLKO_PRYWATNIE = "tylko_prywatnie"
    MIESZANY = "mieszany"

class VehicleLimitPeriod(BaseModel):
    valid_from: date = Field(..., title="Data obowiązywania", description="Data, od kiedy obowiązuje limit")
    limit_type: TaxLimitType = Field(
        TaxLimitType.BEZ_LIMITU,
        title="Typ limitu",
    )
    car_use: TaxUzytkowanieAuta = Field(
        TaxUzytkowanieAuta.TYLKO_FIRMOWO,
    )
