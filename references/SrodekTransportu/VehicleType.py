from enum import Enum


class VehicleType(str, Enum):
    PASSENGER_CAR = "passenger_car"
    TRUCK = "truck"
    VAN = "van"
    SPECIAL = "special"
    OTHER = "other"