from typing import List

from models2.dry.Adnotacje import Adnotacje
from models2.dry.DodatkowyOpis import DodatkowyOpis
from models2.dry.FaWiersz import FaWiersz
from models2.dry.Platnosc import Platnosc
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras


Fa = make_ksef_model_with_extras(
    "Fa",
    fields={
        "KodWaluty": "TKodWaluty",
        "P_1": "TDataT",
        "P_1M": "TZnakowy",
        "P_2": "TZnakowy",
        "P_6": "TDataT",
        "P_13_1": "TKwotowy",
        "P_14_1": "TKwotowy",
        "P_13_3": "TKwotowy",
        "P_14_3": "TKwotowy",
        "P_15": "TKwotowy",
        "RodzajFaktury": "TRodzajFaktury",
        "FP": "TWybor1",
        # Zagnieżdżone struktury:
        "Adnotacje": Adnotacje,
        "DodatkowyOpis": List[DodatkowyOpis],
        "FaWiersz": List[FaWiersz],
        "Platnosc": Platnosc,
    },
    field_extras={
        "KodWaluty": {"title": "Waluta faktury"},
        "P_1": {"title": "Data wystawienia"},
        "P_1M": {"title": "Miejsce wystawienia"},
        "P_2": {"title": "Numer faktury"},
        "P_6": {"title": "Data płatności"},
        "P_13_1": {"title": "Suma wartości netto (stawka 23%)"},
        "P_14_1": {"title": "Kwota podatku VAT (stawka 23%)"},
        "P_13_3": {"title": "Suma wartości netto (stawka 8%)"},
        "P_14_3": {"title": "Kwota podatku VAT (stawka 8%)"},
        "P_15": {"title": "Kwota podatku VAT (stawka 0%)"},
        "RodzajFaktury": {"title": "Rodzaj faktury"},
        "FP": {"title": "Faktura do paragonu"},
        "Adnotacje": {"title": "Adnotacje"},
        "DodatkowyOpis": {"title": "Dodatkowy opis"},
        "FaWiersz": {"title": "Fawiersz"},
        "Platnosc": {"title": "Platnosc"},
    }
)
