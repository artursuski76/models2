from datetime import date

from pydantic import BaseModel

from models2.enums_all.vehicle_usage_type import VehicleUsageType


class TaxRuleUsagePeriodF(BaseModel):
    valid_from: date
    usage_type: VehicleUsageType = VehicleUsageType.MIXED

    def __repr__(self):
        return f"UsagePeriod(valid_from={self.valid_from}, usage_type={self.usage_type})"