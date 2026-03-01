from enum import Enum

class IncomeTaxForm(str, Enum):
    OWNED = "posiadanie"
    LEASE_FINANCE = "leasing_finansowy"
    LEASE_OPERATING = "leasing_operacyjny"
    RENT = "najem"