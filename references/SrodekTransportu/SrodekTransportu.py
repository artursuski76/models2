from decimal import Decimal
from typing import List
from typing import Optional

from pydantic import BaseModel, Field

from models2.references.SrodekTransportu.FuelVehicleTaxCategory import FuelTaxVehicleCategory
from models2.references.SrodekTransportu.IncomeTaxForm import IncomeTaxForm
from models2.references.SrodekTransportu.TaxRuleUsagePeriod import TaxRuleUsagePeriod
from models2.references.SrodekTransportu.VatDeductionBasis import VatDeductionBasis
from models2.references.SrodekTransportu.VehicleType import VehicleType
from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType


class SrodekTransportu(BaseModel):

    vehicle_type: VehicleType

    usage_history: List[TaxRuleUsagePeriod] = Field(default_factory=list)

    tax_form: IncomeTaxForm = IncomeTaxForm.LEASE_OPERATING
    tax_category_fuel: FuelTaxVehicleCategory = Field(default=FuelTaxVehicleCategory.GASOLINE)
    tax_purchase_value: Decimal = Field(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    tax_custom_limit: Optional[Decimal] = Field(None, max_digits=12, decimal_places=2)
    tax_usage_type: VehicleUsageType = VehicleUsageType.MIXED_USE

    vat_deduction_basis: VatDeductionBasis = Field(
        default=VatDeductionBasis.MIXED_USE_50
    )
    vat_deduction_percentage: Decimal = Field(
        default=50.0,
        max_digits=5,
        decimal_places=2
    )
    vat_26_submitted: bool = False
    vat_mileage_log_kept: bool = False
    vat_structural_full_right: bool = False
    vat_correction_period_monats: int = 60  # standard 5 lat dla środków trwałych