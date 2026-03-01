from datetime import date
from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field

from models2.references.SrodekTransportu.VatDeductionBasis import VatDeductionBasis
from models2.references.SrodekTransportu.VehicleLimitPeriod import VehicleLimitPeriod
from models2.references.SrodekTransportu.VehicleType import VehicleType
from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType


class VehicleTaxProfile(BaseModel):
    vehicle_type: VehicleType
    usage_type: VehicleUsageType

    # historia limitów 150k/225k
    limit_history: List[VehicleLimitPeriod] = Field(default_factory=list)

    # wartość pojazdu do wyliczenia proporcji limitu
    vehicle_value_for_limit: Decimal = Field(
        default=Decimal("0.00"),
        max_digits=12,
        decimal_places=2,
        ge=0,
        description="Wartość pojazdu netto, do wyliczenia proporcji limitu"
    )

    # VAT
    vat_deduction_basis: VatDeductionBasis = Field(default=VatDeductionBasis.MIXED_USE_50)
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

    # pomocnicze metody
    def get_limit_for_date(self, invoice_date: date) -> VehicleLimitPeriod:
        """Zwraca obowiązujący limit na dzień dokumentu"""
        sorted_periods = sorted(self.limit_history, key=lambda x: x.valid_from, reverse=True)
        for period in sorted_periods:
            if period.valid_from <= invoice_date:
                return period
        # domyślnie brak limitu
        return VehicleLimitPeriod(valid_from=invoice_date, limit_type="nie_podlega")