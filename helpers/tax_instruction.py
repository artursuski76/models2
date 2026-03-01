from datetime import date
from enum import Enum
from typing import List, Optional
from decimal import Decimal
from pydantic import BaseModel, Field




class CostTypeForTaxInstruction(str, Enum):
    VEHICLE_CAPITAL = "vehicle_capital"  # Proporcja (limit 100k/225k)
    VEHICLE_OPERATIONAL = "vehicle_operational"  # Procent (75%)
    VEHICLE_FINANCIAL = "vehicle_financial"  # 100% CIT
    NONE = "none"  # Standard


class TaxInstruction(BaseModel):
    valid_from: date
    valid_to: Optional[date] = None

    # Kluczowe pole decydujące o algorytmie w Pythonie
    vehicle_cost_type: VehicleCostType = VehicleCostType.BUSINESS_ONLY

    # Parametry bazowe
    deduction_vat: Decimal = Field(default=Decimal("100"))
    deduction_cit: Decimal = Field(default=Decimal("100"))
    nierozl_vat_w_cit: bool = True

    # Parametry dla CAPITAL
    limit_cit: Optional[Decimal] = None
    total_value_for_limit_cit: Optional[Decimal] = None