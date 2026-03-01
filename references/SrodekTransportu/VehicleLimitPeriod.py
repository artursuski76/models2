from decimal import Decimal
from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

from models2.references.SrodekTransportu.VehicleType import VehicleType
from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType
from models2.references.SrodekTransportu.VatDeductionBasis import VatDeductionBasis

class VehicleLimitPeriod(BaseModel):
    valid_from: date
    limit_type: str = Field(..., description="limit_sam_osobowy | nie_podlega")
    limit_value: Optional[Decimal] = Field(
        None, description="Wartość limitu, np. 150000 lub 225000"
    )