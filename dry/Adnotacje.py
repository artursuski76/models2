from typing import List, Optional
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

Zwolnienie = make_ksef_model_with_extras(
    "Zwolnienie",
    fields={
        "P_19": Optional["TWybor1"],
        "P_19A": Optional["TZnakowy"],
        "P_19B": Optional["TZnakowy"],
        "P_19C": Optional["TZnakowy"],
        "P_19N": Optional["TWybor1"],
    }
)

NowySrodekTransportu = make_ksef_model_with_extras(
    "NowySrodekTransportu",
    fields={
        "P_22A": "TDataT",
        "P_NrWierszaNST": "TNaturalny",
        "P_22BMK": Optional["TZnakowy"],
        "P_22BMD": Optional["TZnakowy"],
        "P_22BK": Optional["TZnakowy"],
        "P_22BNR": Optional["TZnakowy"],
        "P_22BRP": Optional["TZnakowy"],
        "P_22B": Optional["TZnakowy"],
        "P_22B1": Optional["TZnakowy"],
        "P_22B2": Optional["TZnakowy"],
        "P_22B3": Optional["TZnakowy"],
        "P_22B4": Optional["TZnakowy"],
        "P_22BT": Optional["TZnakowy"],
        "P_22C": Optional["TZnakowy"],
        "P_22C1": Optional["TZnakowy"],
        "P_22D": Optional["TZnakowy"],
        "P_22D1": Optional["TZnakowy"],
    }
)

NoweSrodkiTransportu = make_ksef_model_with_extras(
    "NoweSrodkiTransportu",
    fields={
        "P_22": Optional["TWybor1"],
        "P_42_5": Optional["TWybor1_2"],
        "NowySrodekTransportu": Optional[List[NowySrodekTransportu]],
        "P_22N": Optional["TWybor1"],
    }
)

PMarzy = make_ksef_model_with_extras(
    "PMarzy",
    fields={
        "P_PMarzy": Optional["TWybor1"],
        "P_PMarzy_2": Optional["TWybor1"],
        "P_PMarzy_3_1": Optional["TWybor1"],
        "P_PMarzy_3_2": Optional["TWybor1"],
        "P_PMarzy_3_3": Optional["TWybor1"],
        "P_PMarzyN": Optional["TWybor1"],
    }
)

Adnotacje = make_ksef_model_with_extras(
    "Adnotacje",
    fields={
        "P_16": "TWybor1_2",
        "P_17": "TWybor1_2",
        "P_18": "TWybor1_2",
        "P_18A": "TWybor1_2",
        "Zwolnienie": Zwolnienie,
        "NoweSrodkiTransportu": NoweSrodkiTransportu,
        "P_23": "TWybor1_2",
        "PMarzy": PMarzy,
    }
)