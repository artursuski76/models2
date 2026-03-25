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

class RachunekBankowy(BaseModel):
    rb_nr: str
    rb_nazwa_banku: str
    rb_opis: str

class Platnosc(BaseModel):
    termin_platnosci: Optional[date]
    forma_platnosci: FormaPlatnosci
    rachunek_bankowy: RachunekBankowy
    zaplacono: bool

