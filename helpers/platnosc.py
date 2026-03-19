from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel

class FormaPlatnosci(str, Enum):
    _1 = "Gotówka"
    _2 = "Karta"
    _3 = "Bon"
    _4 = "Czek"
    _5 = "Kredyt"
    _6 = "Przelew"
    _7 = "Mobilna"

class RachunekBankowy(BaseModel):
    rb_nr: str
    rb_nazwa_banku: str
    rb_opis: str

class Platnosc(BaseModel):
    termin_platnosci: Optional[date]
    forma_platnosci: FormaPlatnosci
    rachunek_bankowy: RachunekBankowy
    zaplacono: bool

