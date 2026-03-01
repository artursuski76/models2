from enum import Enum


class FuelTaxVehicleCategory(str, Enum):
    GASOLINE = "benzyna"
    DIESEL = "diesel"
    HYBRID_PLUGIN_DO_50G = "hybryda_plugin_do_50g"
    ELECTRIC = "elektryczny"
    HYDROGEN = "wodor"

    def __str__(self) -> str:
        return self.value
