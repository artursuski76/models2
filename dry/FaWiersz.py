from typing import Optional
from utils_inne.make_ksef_model_with_extras import make_ksef_model_with_extras

FaWiersz = make_ksef_model_with_extras(
    "FaWiersz",
    fields={
        "NrWierszaFa": "TNaturalny",
        "UU_ID": Optional["TZnakowy50"],
        "P_6A": Optional["TDataT"],
        "P_7": Optional["TZnakowy512"],
        "Indeks": Optional["TZnakowy50"],
        "GTIN": Optional["TZnakowy20"],
        "PKWiU": Optional["TZnakowy50"],
        "CN": Optional["TZnakowy50"],
        "PKOB": Optional["TZnakowy50"],
        "P_8A": Optional["TZnakowy"],
        "P_8B": Optional["TIlosci"],
        "P_9A": Optional["TKwotowy2"],
        "P_9B": Optional["TKwotowy2"],
        "P_10": Optional["TKwotowy2"],
        "P_11": Optional["TKwotowy"],
        "P_11A": Optional["TKwotowy"],
        "P_11Vat": Optional["TKwotowy"],
        "P_12": Optional["TStawkaPodatku"],
        "P_12_XII": Optional["TProcentowy"],
        "P_12_Zal_15": Optional["TWybor1"],
        "KwotaAkcyzy": Optional["TKwotowy"],
        "GTU": Optional["TGTU"],
        "Procedura": Optional["TOznaczenieProcedury"],
        "KursWaluty": Optional["TIlosci"],
        "StanPrzed": Optional["TWybor1"],
    }
)