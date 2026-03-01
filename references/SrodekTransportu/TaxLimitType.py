from enum import Enum




class TaxLimitType(str, Enum):
    SAMOCHOD_OSOBOWY_SPALINOWY = "sam_osobowy_spalinowy"
    SAMOCHOD_OSOBOWY_PLUGIN_DO_50G = "sam_osobowy_plugin_do_50g"
    SAMOCHOD_OSOBOWY_ELEKTRYCZNY = "sam_osobowy_elektryczny"
    BEZ_LIMITU = "bez_limitu"