from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel

class FormaPlatnosci(str, Enum):
    GOTOWKA = "Gotówka"
    KARTA = "Karta"
    BON = "Bon"
    CZEK = "Czek"
    KREDYT = "Kredyt"
    PRZELEW = "Przelew"
    MOBILNA = "Mobilna"

class RachunekBankowy(str, Enum):
    nr_rb: str
    nazwa_banku: str
    opis_rachunku: str

class Platnosc(BaseModel):
    termin_platnosci: Optional[date]
    forma_platnosci: FormaPlatnosci
    rachunek_bankowy: RachunekBankowy
    zaplacono: bool

