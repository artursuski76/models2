from typing import List, Optional
from pydantic import BaseModel, Field
from .single_types import TWybor1, TWybor1_2, TDataT, TNaturalny, TZnakowy




class Zwolnienie(BaseModel):
    P_19: Optional["TWybor1"] = Field(
        None, title="Dostawa towarów/usług zwolniona z VAT"
    )
    P_19A: Optional["TZnakowy"] = Field(
        None, title="Przepis ustawy / akt wydany na podstawie ustawy (zwolnienie)"
    )
    P_19B: Optional["TZnakowy"] = Field(
        None, title="Przepis dyrektywy 2006/112/WE (zwolnienie)"
    )
    P_19C: Optional["TZnakowy"] = Field(
        None, title="Inna podstawa prawna zwolnienia"
    )
    P_19N: Optional["TWybor1"] = Field(
        None, title="Brak zwolnienia (pole techniczne)"
    )


class NowySrodekTransportu(BaseModel):
    P_22A: "TDataT" = Field(..., title="Data dopuszczenia do użytku")
    P_NrWierszaNST: "TNaturalny" = Field(..., title="Numer wiersza środka transportu")

    P_22BMK: Optional["TZnakowy"] = Field(None, title="Marka")
    P_22BMD: Optional["TZnakowy"] = Field(None, title="Model")
    P_22BK: Optional["TZnakowy"] = Field(None, title="Kolor")
    P_22BNR: Optional["TZnakowy"] = Field(None, title="Numer fabryczny/identyfikacyjny")
    P_22BRP: Optional["TZnakowy"] = Field(None, title="Rok produkcji")
    P_22B: Optional["TZnakowy"] = Field(None, title="Przebieg (pojazdy lądowe)")
    P_22B1: Optional["TZnakowy"] = Field(None, title="Liczba godzin roboczych (statki/samoloty)")
    P_22B2: Optional["TZnakowy"] = Field(None, title="Pojemność silnika / Wyporność")
    P_22B3: Optional["TZnakowy"] = Field(None, title="Moc silnika")
    P_22B4: Optional["TZnakowy"] = Field(None, title="Masa startowa (samoloty)")
    P_22BT: Optional["TZnakowy"] = Field(None, title="Typ środka transportu")
    P_22C: Optional["TZnakowy"] = Field(None, title="Kraj pochodzenia")
    P_22C1: Optional["TZnakowy"] = Field(None, title="Kraj przeznaczenia")
    P_22D: Optional["TZnakowy"] = Field(None, title="Uwagi dodatkowe")
    P_22D1: Optional["TZnakowy"] = Field(None, title="Informacje techniczne")


class NoweSrodkiTransportu(BaseModel):
    P_22: Optional["TWybor1"] = Field(
        None, title="Wewnątrzwspólnotowa dostawa nowych środków transportu"
    )
    P_42_5: Optional["TWybor1_2"] = Field(
        None, title="Transport przez nabywcę (art. 42 ust. 5)"
    )
    NowySrodekTransportu: Optional[List[NowySrodekTransportu]] = Field(
        None, title="Lista nowych środków transportu"
    )
    P_22N: Optional["TWybor1"] = Field(
        None, title="Brak dostawy nowych środków transportu"
    )


class PMarzy(BaseModel):
    P_PMarzy: Optional["TWybor1"] = Field(
        None, title="Procedura marży - biura turystyczne"
    )
    P_PMarzy_2: Optional["TWybor1"] = Field(
        None, title="Procedura marży - towary używane"
    )
    P_PMarzy_3_1: Optional["TWybor1"] = Field(
        None, title="Procedura marży - dzieła sztuki"
    )
    P_PMarzy_3_2: Optional["TWybor1"] = Field(
        None, title="Procedura marży - przedmioty kolekcjonerskie"
    )
    P_PMarzy_3_3: Optional["TWybor1"] = Field(
        None, title="Procedura marży - antyki"
    )
    P_PMarzyN: Optional["TWybor1"] = Field(
        None, title="Brak procedury marży"
    )


class Adnotacje(BaseModel):
    P_16: "TWybor1_2" = Field(..., title="Metoda kasowa (1-tak, 2-nie)")
    P_17: "TWybor1_2" = Field(..., title="Samofakturowanie (1-tak, 2-nie)")
    P_18: "TWybor1_2" = Field(..., title="Odwrotne obciążenie (1-tak, 2-nie)")
    P_18A: "TWybor1_2" = Field(..., title="Mechanizm podzielonej płatności (1-tak, 2-nie)")

    Zwolnienie: Zwolnienie = Field(..., title="Szczegóły zwolnienia z VAT")
    NoweSrodkiTransportu: NoweSrodkiTransportu = Field(..., title="Sekcja nowych środków transportu")

    P_23: "TWybor1_2" = Field(..., title="Faktura uproszczona (1-tak, 2-nie)")
    PMarzy: PMarzy = Field(..., title="Szczegóły procedury marży")

#
# from typing import List, Optional
# from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras
#
# Zwolnienie = make_ksef_model_with_extras(
#     "Zwolnienie",
#     fields={
#         "P_19": Optional["TWybor1"],
#         "P_19A": Optional["TZnakowy"],
#         "P_19B": Optional["TZnakowy"],
#         "P_19C": Optional["TZnakowy"],
#         "P_19N": Optional["TWybor1"],
#     },
#     field_extras={
#         "P_19": {"title": "Dostawa towarów/usług zwolniona z VAT"},
#         "P_19A": {"title": "Przepis ustawy / akt wydany na podstawie ustawy (zwolnienie)"},
#         "P_19B": {"title": "Przepis dyrektywy 2006/112/WE (zwolnienie)"},
#         "P_19C": {"title": "Inna podstawa prawna zwolnienia"},
#         "P_19N": {"title": "Brak zwolnienia (pole techniczne)"},
#     }
# )
#
# NowySrodekTransportu = make_ksef_model_with_extras(
#     "NowySrodekTransportu",
#     fields={
#         "P_22A": "TDataT",
#         "P_NrWierszaNST": "TNaturalny",
#         "P_22BMK": Optional["TZnakowy"],
#         "P_22BMD": Optional["TZnakowy"],
#         "P_22BK": Optional["TZnakowy"],
#         "P_22BNR": Optional["TZnakowy"],
#         "P_22BRP": Optional["TZnakowy"],
#         "P_22B": Optional["TZnakowy"],
#         "P_22B1": Optional["TZnakowy"],
#         "P_22B2": Optional["TZnakowy"],
#         "P_22B3": Optional["TZnakowy"],
#         "P_22B4": Optional["TZnakowy"],
#         "P_22BT": Optional["TZnakowy"],
#         "P_22C": Optional["TZnakowy"],
#         "P_22C1": Optional["TZnakowy"],
#         "P_22D": Optional["TZnakowy"],
#         "P_22D1": Optional["TZnakowy"],
#     },
#     field_extras={
#         "P_22A": {"title": "Data dopuszczenia do użytku"},
#         "P_NrWierszaNST": {"title": "Numer wiersza środka transportu"},
#         "P_22BMK": {"title": "Marka"},
#         "P_22BMD": {"title": "Model"},
#         "P_22BK": {"title": "Kolor"},
#         "P_22BNR": {"title": "Numer fabryczny/identyfikacyjny"},
#         "P_22BRP": {"title": "Rok produkcji"},
#         "P_22B": {"title": "Przebieg (pojazdy lądowe)"},
#         "P_22B1": {"title": "Liczba godzin roboczych (statki/samoloty)"},
#         "P_22B2": {"title": "Pojemność silnika / Wyporność"},
#         "P_22B3": {"title": "Moc silnika"},
#         "P_22B4": {"title": "Masa startowa (samoloty)"},
#         "P_22BT": {"title": "Typ środka transportu"},
#         "P_22C": {"title": "Kraj pochodzenia"},
#         "P_22C1": {"title": "Kraj przeznaczenia"},
#         "P_22D": {"title": "Uwagi dodatkowe"},
#         "P_22D1": {"title": "Informacje techniczne"},
#     }
# )
#
# NoweSrodkiTransportu = make_ksef_model_with_extras(
#     "NoweSrodkiTransportu",
#     fields={
#         "P_22": Optional["TWybor1"],
#         "P_42_5": Optional["TWybor1_2"],
#         "NowySrodekTransportu": Optional[List[NowySrodekTransportu]],
#         "P_22N": Optional["TWybor1"],
#     },
#     field_extras={
#         "P_22": {"title": "Wewnątrzwspólnotowa dostawa nowych środków transportu"},
#         "P_42_5": {"title": "Transport przez nabywcę (art. 42 ust. 5)"},
#         "NowySrodekTransportu": {"title": "Lista nowych środków transportu"},
#         "P_22N": {"title": "Brak dostawy nowych środków transportu"},
#     }
# )
#
# PMarzy = make_ksef_model_with_extras(
#     "PMarzy",
#     fields={
#         "P_PMarzy": Optional["TWybor1"],
#         "P_PMarzy_2": Optional["TWybor1"],
#         "P_PMarzy_3_1": Optional["TWybor1"],
#         "P_PMarzy_3_2": Optional["TWybor1"],
#         "P_PMarzy_3_3": Optional["TWybor1"],
#         "P_PMarzyN": Optional["TWybor1"],
#     },
#     field_extras={
#         "P_PMarzy": {"title": "Procedura marży - biura turystyczne"},
#         "P_PMarzy_2": {"title": "Procedura marży - towary używane"},
#         "P_PMarzy_3_1": {"title": "Procedura marży - dzieła sztuki"},
#         "P_PMarzy_3_2": {"title": "Procedura marży - przedmioty kolekcjonerskie"},
#         "P_PMarzy_3_3": {"title": "Procedura marży - antyki"},
#         "P_PMarzyN": {"title": "Brak procedury marży"},
#     }
# )
#
# Adnotacje = make_ksef_model_with_extras(
#     "Adnotacje",
#     fields={
#         "P_16": "TWybor1_2",
#         "P_17": "TWybor1_2",
#         "P_18": "TWybor1_2",
#         "P_18A": "TWybor1_2",
#         "Zwolnienie": Zwolnienie,
#         "NoweSrodkiTransportu": NoweSrodkiTransportu,
#         "P_23": "TWybor1_2",
#         "PMarzy": PMarzy,
#     },
#     field_extras={
#         "P_16": {"title": "Metoda kasowa (1-tak, 2-nie)"},
#         "P_17": {"title": "Samofakturowanie (1-tak, 2-nie)"},
#         "P_18": {"title": "Odwrotne obciążenie (1-tak, 2-nie)"},
#         "P_18A": {"title": "Mechanizm podzielonej płatności (1-tak, 2-nie)"},
#         "Zwolnienie": {"title": "Szczegóły zwolnienia z VAT"},
#         "NoweSrodkiTransportu": {"title": "Sekcja nowych środków transportu"},
#         "P_23": {"title": "Faktura uproszczona (1-tak, 2-nie)"},
#         "PMarzy": {"title": "Szczegóły procedury marży"},
#     }
# )