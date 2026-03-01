from enum import Enum


class FuelTaxVehicleCategory(str, Enum):
    GASOLINE = "benzyna"
    DIESEL = "diesel"
    HYBRID_PLUGIN = "hybryda_plugin"
    ELECTRIC = "elektryczny"
    HYDROGEN = "wodor"


