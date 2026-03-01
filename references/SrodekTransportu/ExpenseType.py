from enum import Enum


class ExpenseType(str, Enum):
    FINANCIAL = "finansowy"
    CAPITAL = "kapitalowy"
    EXPLOITATION = "eksploatacyjny"