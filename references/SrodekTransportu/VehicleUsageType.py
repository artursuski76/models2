
from enum import Enum





class VehicleUsageType(str, Enum):
    BUSINESS_ONLY = "business_only"
    MIXED_USE = "mixed_use"
    PRIVATE_ONLY = "private_only"