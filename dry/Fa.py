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
    }
)