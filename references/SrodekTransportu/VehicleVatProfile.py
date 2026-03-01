# from decimal import Decimal
#
# from pydantic import BaseModel, Field, model_validator
#
# from models2.references.SrodekTransportu.VatDeductionBasis import VatDeductionBasis
#
#
# # class VehicleVatProfile(BaseModel):
#
#     # vat_deduction_basis: VatDeductionBasis = Field(
#     #     default=VatDeductionBasis.MIXED_USE_50
#     # )
#     #
#     # vat_deduction_percentage: Decimal = Field(
#     #     default=Decimal("50.00"),
#     #     max_digits=5,
#     #     decimal_places=2
#     # )
#     #
#     # vat_26_submitted: bool = False
#     # vat_mileage_log_kept: bool = False
#     # vat_structural_full_right: bool = False
#     #
#     # vat_correction_period_years: int = 5  # standard 5 lat dla środków trwałych
#
#     # =====================================================
#     # WALIDATORY
#     # =====================================================
#
#     @model_validator(mode="after")
#     def validate_vat_logic(self):
#
#         # 0% VAT
#         if self.deduction_basis == VatDeductionBasis.NONE:
#             if self.deduction_percentage != Decimal("0.00"):
#                 raise ValueError("Przy braku prawa do odliczenia VAT procent musi wynosić 0%.")
#
#         # 50% VAT
#         if self.deduction_basis == VatDeductionBasis.MIXED_USE_50:
#             if self.deduction_percentage != Decimal("50.00"):
#                 raise ValueError("Przy użytku mieszanym VAT musi wynosić 50%.")
#
#         # 100% VAT – działalność
#         if self.deduction_basis == VatDeductionBasis.BUSINESS_WITH_LOGBOOK:
#             if not self.vat_26_submitted:
#                 raise ValueError("100% VAT wymaga złożenia VAT-26.")
#             if not self.mileage_log_kept:
#                 raise ValueError("100% VAT wymaga ewidencji przebiegu.")
#             if self.deduction_percentage != Decimal("100.00"):
#                 raise ValueError("Pełne odliczenie wymaga 100%.")
#
#         # 100% konstrukcyjnie
#         if self.deduction_basis == VatDeductionBasis.STRUCTURAL_FULL:
#             if not self.structural_full_right:
#                 raise ValueError("Brak potwierdzenia konstrukcyjnego prawa do 100% VAT.")
#             if self.deduction_percentage != Decimal("100.00"):
#                 raise ValueError("Pełne odliczenie wymaga 100%.")
#
#         return self