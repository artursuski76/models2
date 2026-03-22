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
    },
    field_extras={
        "KwotaZaplatyCzesciowej": {"title": "Kwota wpłaty częściowej", "order": 1},
        "DataZaplatyCzesciowej": {"title": "Data wpłaty częściowej", "order": 2},
        "FormaPlatnosci": {"title": "Forma płatności (częściowej)", "order": 3},
        "PlatnoscInna": {"title": "Inna forma płatności", "order": 4},
        "OpisPlatnosci": {"title": "Opis innej formy płatności", "order": 5},
    }
)

TerminOpis = make_ksef_model_with_extras(
    "TerminOpis",
    fields={
        "Ilosc": "TNaturalny",
        "Jednostka": "TZnakowy50",
        "ZdarzeniePoczatkowe": "TZnakowy",
    },
    field_extras={
        "Ilosc": {"title": "Liczba (ilość jednostek czasu)", "order": 1},
        "Jednostka": {"title": "Jednostka czasu (np. dni, miesiące)", "order": 2},
        "ZdarzeniePoczatkowe": {"title": "Zdarzenie rozpoczynające bieg terminu", "order": 3},
    }
)

TerminPlatnosci = make_ksef_model_with_extras(
    "TerminPlatnosci",
    fields={
        "Termin": Optional["TData"],
        "TerminOpis": Optional[TerminOpis],
    },
    field_extras={
        "Termin": {"title": "Data terminu płatności", "order": 1},
        "TerminOpis": {"title": "Opisowy termin płatności (np. 14 dni od dostawy)", "order": 2},
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
    },
    field_extras={
        "NrRB": {"title": "Numer rachunku bankowego (IBAN/NRB)", "order": 1},
        "SWIFT": {"title": "Kod SWIFT/BIC", "order": 2},
        "RachunekWlasnyBanku": {"title": "Rachunek własny banku (1-tak, 2-nie)", "order": 3},
        "NazwaBanku": {"title": "Nazwa banku", "order": 4},
        "OpisRachunku": {"title": "Opis rachunku", "order": 5},
    }
)

Skonto = make_ksef_model_with_extras(
    "Skonto",
    fields={
        "WarunkiSkonta": "TZnakowy",
        "WysokoscSkonta": "TZnakowy",
    },
    field_extras={
        "WarunkiSkonta": {"title": "Warunki przyznania skonta", "order": 1},
        "WysokoscSkonta": {"title": "Wysokość skonta (kwota lub %)", "order": 2},
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
    },
    field_extras={
        "Zaplacono": {"title": "Faktura zapłacona w całości (1-tak)", "order": 1},
        "DataZaplaty": {"title": "Data dokonania zapłaty", "order": 2},
        "ZnacznikZaplatyCzesciowej": {"title": "Czy zapłacono częściowo? (1-tak, 2-nie)", "order": 3},
        "ZaplataCzesciowa": {"title": "Szczegóły wpłat częściowych", "order": 4},
        "TerminPlatnosci": {"title": "Terminy płatności", "order": 5},
        "FormaPlatnosci": {"title": "Forma płatności", "order": 6},
        "PlatnoscInna": {"title": "Inna forma płatności (1-tak)", "order": 7},
        "OpisPlatnosci": {"title": "Opis innej formy płatności", "order": 8},
        "RachunekBankowy": {"title": "Numery rachunków bankowych sprzedawcy", "order": 9},
        "RachunekBankowyFaktora": {"title": "Rachunki bankowe faktora", "order": 10},
        "Skonto": {"title": "Warunki skonta", "order": 11},
        "LinkDoPlatnosci": {"title": "Link do płatności online", "order": 12},
        "IPKSeF": {"title": "Identyfikator płatności KSeF", "order": 13},
    }
)