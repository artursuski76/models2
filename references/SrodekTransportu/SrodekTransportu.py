from datetime import date
from decimal import Decimal
from typing import List



from pydantic import BaseModel, model_validator

from models2.references.SrodekTransportu.TaxRuleUsagePeriod import TaxRuleUsagePeriod
from models2.references.SrodekTransportu.VehicleIncomeTaxProfile import VehicleIncomeTaxProfile
from models2.references.SrodekTransportu.VehicleType import VehicleType
from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType
from models2.references.SrodekTransportu.VehicleVatProfile import VehicleVatProfile



class SrodekTransportu(BaseModel):

    vehicle_type: VehicleType
    usage_history: List[TaxRuleUsagePeriod]
    vat_profile: VehicleVatProfile
    income_tax_profile: VehicleIncomeTaxProfile

    # =====================================================
    # WALIDATOR SPÓJNOŚCI MIĘDZY PROFILAMI
    # =====================================================

    @model_validator(mode="after")
    def validate_cross_logic(self):

        # Jeśli VAT 100% to CIT nie może być prywatny
        if (
            self.vat_profile.deduction_percentage == Decimal("100.00")
            and self.income_tax_profile.usage_type == VehicleUsageType.PRIVATE_ONLY
        ):
            raise ValueError("Nie można mieć 100% VAT i użytku prywatnego w CIT.")

        return self

    # =====================================================
    # METODY
    # =====================================================

    def get_usage_for_date(self, check_date: date) -> VehicleUsageType:
        sorted_history = sorted(
            self.usage_history,
            key=lambda x: x.valid_from,
            reverse=True
        )
        for period in sorted_history:
            if period.valid_from <= check_date:
                return period.usage_type
        return VehicleUsageType.BUSINESS_ONLY