from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field, model_validator

from models2.references.SrodekTransportu.FuelVehicleTaxCategory import FuelTaxVehicleCategory
from models2.references.SrodekTransportu.IncomeTaxForm import IncomeTaxForm
from models2.references.SrodekTransportu.TaxRuleUsagePeriod import TaxRuleUsagePeriod
from models2.references.SrodekTransportu.VatDeductionBasis import VatDeductionBasis
from models2.references.SrodekTransportu.VehicleType import VehicleType
from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType


class SrodekTransportu(BaseModel):

    # =====================================================
    # OGÓLNE
    # =====================================================

    vehicle_type: VehicleType

    usage_history: List[TaxRuleUsagePeriod] = Field(
        default_factory=list,
        min_length=1
    )

    # =====================================================
    # CIT / PIT
    # =====================================================

    tax_form: IncomeTaxForm = IncomeTaxForm.LEASE_OPERATING

    tax_category_fuel: FuelTaxVehicleCategory = Field(
        default=FuelTaxVehicleCategory.GASOLINE
    )

    tax_purchase_value: Decimal = Field(
        default=Decimal("0.00"),
        max_digits=12,
        decimal_places=2,
        ge=0
    )

    tax_custom_limit: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=2,
        ge=0
    )

    tax_usage_type: VehicleUsageType = VehicleUsageType.MIXED_USE

    # =====================================================
    # VAT
    # =====================================================

    vat_deduction_basis: VatDeductionBasis = Field(
        default=VatDeductionBasis.MIXED_USE_50
    )

    vat_deduction_percentage: Decimal = Field(
        default=Decimal("50.00"),
        max_digits=5,
        decimal_places=2,
        ge=0,
        le=100
    )

    vat_26_submitted: bool = False
    vat_mileage_log_kept: bool = False
    vat_structural_full_right: bool = False

 # potrzebne do modelu SrodekTrwaly
    # vat_correction_period_months: int = Field(
    #     default=60,
    #     ge=1
    # )

    # =====================================================
    # WALIDACJA VAT
    # =====================================================

    @model_validator(mode="after")
    def validate_vat_logic(self):

        if self.vat_deduction_basis == VatDeductionBasis.NONE:
            if self.vat_deduction_percentage != Decimal("0.00"):
                raise ValueError("Przy braku prawa do VAT procent musi wynosić 0%.")

        if self.vat_deduction_basis == VatDeductionBasis.MIXED_USE_50:
            if self.vat_deduction_percentage != Decimal("50.00"):
                raise ValueError("Użytek mieszany wymaga 50% VAT.")

        if self.vat_deduction_basis == VatDeductionBasis.BUSINESS_WITH_LOGBOOK:
            if not self.vat_26_submitted:
                raise ValueError("100% VAT wymaga VAT-26.")
            if not self.vat_mileage_log_kept:
                raise ValueError("100% VAT wymaga ewidencji przebiegu.")
            if self.vat_deduction_percentage != Decimal("100.00"):
                raise ValueError("Pełne odliczenie wymaga 100%.")

        if self.vat_deduction_basis == VatDeductionBasis.STRUCTURAL_FULL:
            if not self.vat_structural_full_right:
                raise ValueError("Brak konstrukcyjnego prawa do 100% VAT.")
            if self.vat_deduction_percentage != Decimal("100.00"):
                raise ValueError("Pełne odliczenie wymaga 100%.")

        return self

    # =====================================================
    # WALIDACJA CIT
    # =====================================================

    @model_validator(mode="after")
    def validate_income_tax_logic(self):

        if self.tax_form in {
            IncomeTaxForm.LEASE_OPERATING,
            IncomeTaxForm.LEASE_FINANCIAL
        } and self.tax_purchase_value == Decimal("0.00"):
            raise ValueError("Leasing wymaga podania wartości pojazdu do limitu.")

        if self.tax_custom_limit is not None:
            if self.tax_custom_limit <= 0:
                raise ValueError("Limit niestandardowy musi być > 0.")

        return self