from typing import List, Optional
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

ZaplataCzesciowa = make_ksef_model_with_extras(
    "ZaplataCzesciowa",
    fields={
        "KwotaZaplatyCzesciowej": "TKwotowy",
        "DataZaplatyCzesciowej": "TData",
        "FormaPlatnosci": Optional["TFormaPlatnosci"],
        "PlatnoscInna": Optional["TWybor1"],
        "OpisPlatnosci": Optional["TZnakowy"],
    }
)

TerminOpis = make_ksef_model_with_extras(
    "TerminOpis",
    fields={
        "Ilosc": "TNaturalny",
        "Jednostka": "TZnakowy50",
        "ZdarzeniePoczatkowe": "TZnakowy",
    }
)

TerminPlatnosci = make_ksef_model_with_extras(
    "TerminPlatnosci",
    fields={
        "Termin": Optional["TData"],
        "TerminOpis": Optional[TerminOpis],
    }
)

TRachunekBankowy = make_ksef_model_with_extras(
    "TRachunekBankowy",
    fields={
        "NrRB": "TNrRB",
        "SWIFT": Optional["SWIFT_Type"],
        "RachunekWlasnyBanku": Optional["TRachunekWlasnyBanku"],
        "NazwaBanku": Optional["TZnakowy"],
        "OpisRachunku": Optional["TZnakowy"],
    }
)

Skonto = make_ksef_model_with_extras(
    "Skonto",
    fields={
        "WarunkiSkonta": "TZnakowy",
        "WysokoscSkonta": "TZnakowy",
    }
)

Platnosc = make_ksef_model_with_extras(
    "Platnosc",
    fields={
        "Zaplacono": Optional["TWybor1"],
        "DataZaplaty": Optional["TData"],
        "ZnacznikZaplatyCzesciowej": Optional["TWybor1_2"],
        "ZaplataCzesciowa": Optional[List[ZaplataCzesciowa]],
        "TerminPlatnosci": Optional[List[TerminPlatnosci]],
        "FormaPlatnosci": Optional["TFormaPlatnosci"],
        "PlatnoscInna": Optional["TWybor1"],
        "OpisPlatnosci": Optional["TZnakowy"],
        "RachunekBankowy": Optional[List[TRachunekBankowy]],
        "RachunekBankowyFaktora": Optional[List[TRachunekBankowy]],
        "Skonto": Optional[Skonto],
        "LinkDoPlatnosci": Optional["TZnakowy512"],
        "IPKSeF": Optional["TZnakowy20"],
    }
)