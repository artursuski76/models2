from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, model_validator

from models2.references.SrodekTransportu.FuelVehicleTaxCategory import FuelTaxVehicleCategory
from models2.references.SrodekTransportu.IncomeTaxForm import IncomeTaxForm
from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType


class VehicleIncomeTaxProfile(BaseModel):

    tax_form: IncomeTaxForm = IncomeTaxForm.LEASE_OPERATING

    fuel: FuelTaxVehicleCategory = Field(default=FuelTaxVehicleCategory.GASOLINE)

    purchase_value: Decimal = Field(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    custom_limit: Optional[Decimal] = None

    usage_type: VehicleUsageType = VehicleUsageType.MIXED_USE

    # =====================================================
    # LOGIKA LIMITU
    # =====================================================

    def get_limit(self) -> Decimal:
        if self.custom_limit:
            return self.custom_limit

        if self.fuel == FuelTaxVehicleCategory.GASOLINE:
            return Decimal("100000.00")

        if self.fuel == FuelTaxVehicleCategory.DIESEL:
            return Decimal("100000.00")

        if self.fuel == FuelTaxVehicleCategory.HYBRID_PLUGIN:
            return Decimal("150000.00")

        if self.fuel == FuelTaxVehicleCategory.ELECTRIC:
            return Decimal("225000.00")

        return Decimal("225000.00")

    def get_deductible_ratio(self) -> Decimal:
        """
        Zwraca proporcję kosztową przy przekroczeniu limitu.
        """
        limit = self.get_limit()

        if self.purchase_value == 0:
            return Decimal("0")

        if self.purchase_value <= limit:
            return Decimal("1")

        return limit / self.purchase_value

    def get_cost_usage_ratio(self) -> Decimal:
        """
        75% kosztów przy użytku mieszanym (eksploatacja).
        100% przy firmowym.
        """
        if self.usage_type == VehicleUsageType.MIXED_USE:
            return Decimal("0.75")

        if self.usage_type == VehicleUsageType.BUSINESS_ONLY:
            return Decimal("1.00")

        return Decimal("0.00")

    # =====================================================
    # WALIDATOR
    # =====================================================

    @model_validator(mode="after")
    def validate_income_tax_logic(self):

        if self.purchase_value < 0:
            raise ValueError("Wartość pojazdu nie może być ujemna.")

        if self.tax_form == IncomeTaxForm.LEASE and self.purchase_value == 0:
            raise ValueError("Leasing wymaga określenia wartości pojazdu do limitu.")

        return self