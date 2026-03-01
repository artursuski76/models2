# from datetime import date
#
# from pydantic import BaseModel, model_validator
#
# from models2.references.SrodekTransportu.VehicleUsageType import VehicleUsageType
#
#
# class TaxRuleUsagePeriod(BaseModel):
#     valid_from: date
#     usage_type: VehicleUsageType
#
#     @model_validator(mode="after")
#     def validate_usage_type(self):
#         if self.usage_type not in VehicleUsageType:
#             raise ValueError(f"Nieprawidłowy typ użytkowania: {self.usage_type}")
#         return self