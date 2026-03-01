from enum import Enum


class IITaxCategoryVehicle(str, Enum):
    SAM_OSOBOWY = "sam_osobowy"
    SAM_INNY = "sam_ciezarowy"
    SAM_SPECJALNY = "specjalny"
    NONE = "standard"

class IITaxCategory(str, Enum):
    PERSONAL_CAR = "osobowy"
    RESIDENTIAL_PROP = "nieruchomosc_mieszkalna"
    ART = "dzielo_sztuki"
    TRUCK = "ciezarowy"
    NONE = "standard"

class VehicleTypeB(str, Enum):
    PASSENGER_CAR = "samochod osobowy"
    TRUCK = "samochod_ciezarowy"
    VAN = "kombi"
    SPECIAL = "specjalny"
    OTHER = "inny"

class VehicleUsagetype(str, Enum):
    BUSINESS_ONLY = "tylko_biznes"
    MIXED_USE = "mieszany"
    PRIVATE_ONLY = "tylko_prywatnie"

class VatDeductionBasis(str, Enum):
    NONE = "brak"
    MIXED_USE_LIMITED_50 = "mieszany_ograniczony_50"
    BUSINESS_ONLY_WITH_LOGBOOK = "biznes_z_logbookiem"
    STRUCTURAL_FULL_DEDUCTION = "konstrukcyjnie_pelne_odliczenie"
    OTHER_FULL_DEDUCTION = "inne_pelne_odliczenie"