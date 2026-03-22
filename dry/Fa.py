from typing import List, Optional

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
        "P_13_2": Optional["TKwotowy"],
        "P_14_2": Optional["TKwotowy"],
        "P_13_3": Optional["TKwotowy"],
        "P_14_3": Optional["TKwotowy"],
        "P_13_4": Optional["TKwotowy"],
        "P_14_4": Optional["TKwotowy"],
        "P_13_5": Optional["TKwotowy"],
        "P_14_5": Optional["TKwotowy"],
        "P_13_6": Optional["TKwotowy"],
        "P_13_7": Optional["TKwotowy"],
        "P_15": Optional["TKwotowy"],
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
        "P_13_1": {"title": "Netto 23%", "order": 10},
        "P_14_1": {"title": "VAT 23%", "order": 11},
        "P_13_2": {"title": "Netto 22%", "order": 12},
        "P_14_2": {"title": "VAT 22%", "order": 13},
        "P_13_3": {"title": "Netto 8%/7%", "order": 14},
        "P_14_3": {"title": "VAT 8%/7%", "order": 15},
        "P_13_4": {"title": "Netto 5%", "order": 16},
        "P_14_4": {"title": "VAT 5%", "order": 17},
        "P_13_5": {"title": "Netto 4%/3%", "order": 18},
        "P_14_5": {"title": "VAT 4%/3%", "order": 19},
        "P_13_6": {"title": "Netto 0%", "order": 20},
        "P_13_7": {"title": "Zwolnione", "order": 21},
        "P_15": {"title": "Suma VAT", "order": 22},
        "RodzajFaktury": {"title": "Rodzaj faktury"},
        "FP": {"title": "Faktura do paragonu"},
        "Adnotacje": {"title": "Adnotacje"},
        "DodatkowyOpis": {"title": "Dodatkowy opis"},
        "FaWiersz": {"title": "Fawiersz"},
        "Platnosc": {"title": "Platnosc"},
    }
)
