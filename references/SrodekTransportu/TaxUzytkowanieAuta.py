from enum import Enum



class TaxUzytkowanieAuta(str, Enum):
    TYLKO_FIRMOWO = "tylko_firmowo"
    TYLKO_PRYWATNIE = "tylko_prywatnie"
    MIESZANY = "mieszany"