
from enum import Enum





class VehicleUsageType(str, Enum):
    BUSINESS_ONLY = "tylko_firmowo"
    MIXED_USE = "mieszany"
    PRIVATE_ONLY = "tylko_prywatnie"