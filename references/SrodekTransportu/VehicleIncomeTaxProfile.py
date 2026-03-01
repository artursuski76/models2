from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from models2.references.SrodekTransportu.FuelVehicleTaxCategory import FuelTaxVehicleCategory
from models2.references.SrodekTransportu.IncomeTaxForm import IncomeTaxForm
from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType


class VehicleIncomeTaxProfile(BaseModel):

    tax_form: IncomeTaxForm = IncomeTaxForm.LEASE_OPERATING

    tax_category_fuel: FuelTaxVehicleCategory = Field(default=FuelTaxVehicleCategory.GASOLINE)

    # dla zakupu → wartość początkowa środka trwałego
    # dla leasingu operacyjnego → wartość pojazdu z umowy leasingu
    # dla leasingu finansowego → wartość początkowa do amortyzacji

    tax_purchase_value: Decimal = Field(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    tax_custom_limit: Optional[Decimal] = Field(None, max_digits=12, decimal_places=2)

    tax_usage_type: VehicleUsageType = VehicleUsageType.MIXED_USE

