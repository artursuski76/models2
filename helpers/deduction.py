from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

# from models2.helpers.money import Money


class Deduction(BaseModel):
    deduction_CIT: Optional[float] = Field(
        default=100,
        alias="refound_CIT"
    )

    deduction_VAT: Optional[float] = Field(
        default=100,
        alias="refound_VAT"
    )
    limit_cit: Optional[Decimal] = Field(
        default=None,
        max_digits=12, decimal_places=2,
        alias="limit_CIT"
    )
    value_for_limit_cit: Optional[Decimal] = Field(
        default=None,
        max_digits=12, decimal_places=2,
        alias="wartosc_calkowita_do_limitu_CIT"
    )
    nierozl_vat_w_cit: bool = Field(default=True, title="Nierozliczony VAT rozlicz w CIT")
