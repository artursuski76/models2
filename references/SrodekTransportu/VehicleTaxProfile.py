from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field

from models2.references.SrodekTransportu.VehicleLimitPeriod import VehicleLimitPeriod


class VehicleTaxProfile(BaseModel):

    limit_history: List[VehicleLimitPeriod] = Field(default_factory=list)
    vehicle_value_for_limit: Decimal = Field(
        default=Decimal("0.00"),
        max_digits=12,
        decimal_places=2,
        ge=0,
        title="Wartość pojazdu netto, do wyliczenia proporcji limitu"
    )

