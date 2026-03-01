from enum import Enum

class IncomeTaxForm(str, Enum):
    OWNED = "owned"
    LEASE = "lease"
    RENT = "rent"