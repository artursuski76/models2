from typing import List, Optional, Annotated, Literal, Union
from datetime import datetime, date
from pydantic import BaseModel, Field, RootModel, ConfigDict, field_validator

from models2.abase import BasicBasic

# Wspólne typy i walidatory
TKwota2 = Annotated[float, Field(ge=0)] # Kwoty dodatnie
TKwota2Nieujemna = Annotated[float, Field(ge=0)]
TKwota2Dowolna = float

# Typy tekstowe z regexami (uproszczone na podstawie znanych schematów JPK)
TNip = Annotated[str, Field(pattern=r"^[1-9](\d{9})$")]
TPesel = Annotated[str, Field(pattern=r"^\d{11}$")]
TRegon = Annotated[str, Field(pattern=r"^\d{9,14}$")]
TData = date
TDateTime = datetime
TMiesiac = Annotated[int, Field(ge=1, le=12)]
TRok = Annotated[int, Field(ge=2026, le=2099)]  # XSD: minInclusive 2026
TDataT = Annotated[date, Field(ge=date(2006, 1, 1))]  # Data transakcji
TDataTP = Annotated[date, Field(ge=date(2016, 1, 1))]  # Data płatności
TWybor1 = Literal[1]  # Wartość boolean jako 1

# --- Definicje (na podstawie schemat-2.json) ---

class TKodFormularza(RootModel):
    root: Literal["JPK_VAT"]

class TKodFormularzaVAT7(RootModel):
    root: Literal["VAT-7"]

class TDowoduSprzedazy(RootModel):
    root: Literal["RO", "WEW", "FP"]

class TDowoduZakupu(RootModel):
    root: Literal["MK", "VAT_RR", "WEW"]

class TNaglowekKodFormularza(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    value: TKodFormularza = Field(validation_alias="value", serialization_alias="#text")
    kod_systemowy: Literal["JPK_V7M (3)"] = Field(
        validation_alias="kodSystemowy",
        serialization_alias="@kodSystemowy"
    )
    wersja_schemy: Literal["1-0E"] = Field(
        validation_alias="wersjaSchemy",
        serialization_alias="@wersjaSchemy"
    )

class TNaglowekCelZlozenia(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    value: int = Field(validation_alias="value", serialization_alias="#text")
    poz: Literal["P_7"] = Field(serialization_alias="@poz")

class TNaglowek(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    kod_formularza: TNaglowekKodFormularza = Field(
        validation_alias="KodFormularza",
        serialization_alias="KodFormularza"
    )
    wariant_formularza: Literal[3] = Field(
        validation_alias="WariantFormularza",
        serialization_alias="WariantFormularza"
    )
    data_wytworzenia_jpk: TDateTime = Field(
        validation_alias="DataWytworzeniaJPK",
        serialization_alias="DataWytworzeniaJPK"
    )
    nazwa_systemu: Optional[str] = Field(
        None,
        validation_alias="NazwaSystemu",
        serialization_alias="NazwaSystemu",
        max_length=240
    )
    cel_zlozenia: TNaglowekCelZlozenia = Field(
        validation_alias="CelZlozenia",
        serialization_alias="CelZlozenia"
    )
    kod_urzedu: str = Field(
        validation_alias="KodUrzedu",
        serialization_alias="KodUrzedu"
    )
    rok: TRok = Field(
        validation_alias="Rok",
        serialization_alias="Rok"
    )
    miesiac: TMiesiac = Field(
        validation_alias="Miesiac",
        serialization_alias="Miesiac"
    )

class JPKNaglowek(TNaglowek):
    pass

# --- Podmiot ---

class TIdentyfikatorOsobyFizycznej2(BaseModel):
    nip: TNip
    imiePierwsze: str
    nazwisko: str
    dataUrodzenia: TData

class TPodmiotDowolnyBezAdresuOsobaFizyczna(TIdentyfikatorOsobyFizycznej2):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    email: str = Field(validation_alias="Email", serialization_alias="Email")
    telefon: Optional[str] = Field(
        None,
        validation_alias="Telefon",
        serialization_alias="Telefon",
        max_length=16
    )

class TIdentyfikatorOsobyNiefizycznej(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    nip: TNip = Field(validation_alias="NIP", serialization_alias="NIP")
    pelna_nazwa: str = Field(
        validation_alias="PelnaNazwa",
        serialization_alias="PelnaNazwa",
        max_length=240
    )

class TPodmiotDowolnyBezAdresuOsobaNiefizyczna(TIdentyfikatorOsobyNiefizycznej):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    email: str = Field(validation_alias="Email", serialization_alias="Email")
    telefon: Optional[str] = Field(
        None,
        validation_alias="Telefon",
        serialization_alias="Telefon",
        max_length=16
    )

class TPodmiotDowolnyBezAdresu(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    osoba_fizyczna: Optional[TPodmiotDowolnyBezAdresuOsobaFizyczna] = Field(
        None,
        validation_alias="OsobaFizyczna",
        serialization_alias="OsobaFizyczna"
    )
    osoba_niefizyczna: Optional[TPodmiotDowolnyBezAdresuOsobaNiefizyczna] = Field(
        None,
        validation_alias="OsobaNiefizyczna",
        serialization_alias="OsobaNiefizyczna"
    )

class JPKPodmiot1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    # XSD: choice - tylko jedno z pól
    osoba_fizyczna: Optional[TPodmiotDowolnyBezAdresuOsobaFizyczna] = Field(
        None,
        validation_alias="OsobaFizyczna",
        serialization_alias="OsobaFizyczna"
    )
    osoba_niefizyczna: Optional[TPodmiotDowolnyBezAdresuOsobaNiefizyczna] = Field(
        None,
        validation_alias="OsobaNiefizyczna",
        serialization_alias="OsobaNiefizyczna"
    )
    rola: Literal["Podatnik"] = Field(
        serialization_alias="@rola"
    )

    @field_validator("osoba_fizyczna", "osoba_niefizyczna")
    @classmethod
    def validate_choice(cls, v, info):
        # Sprawdzenie że tylko jedno pole jest wypełnione (choice)
        values = info.data
        filled = sum([
            values.get("osoba_fizyczna") is not None,
            values.get("osoba_niefizyczna") is not None
        ])
        if filled != 1:
            raise ValueError("Dokładnie jedno z pól OsobaFizyczna lub OsobaNiefizyczna musi być wypełnione")
        return v

# --- Deklaracja ---

class JPKDeklaracjaNaglowekKodFormularzaDekl(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    value: TKodFormularzaVAT7 = Field(validation_alias="value", serialization_alias="#text")
    kod_systemowy: Literal["VAT-7 (23)"] = Field(
        validation_alias="kodSystemowy",
        serialization_alias="@kodSystemowy"
    )
    kod_podatku: Literal["VAT"] = Field(
        validation_alias="kodPodatku",
        serialization_alias="@kodPodatku"
    )
    rodzaj_zobowiazania: Literal["Z"] = Field(
        validation_alias="rodzajZobowiazania",
        serialization_alias="@rodzajZobowiazania"
    )
    wersja_schemy: Literal["1-0E"] = Field(
        validation_alias="wersjaSchemy",
        serialization_alias="@wersjaSchemy"
    )

class JPKDeklaracjaNaglowek(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    kod_formularza_dekl: JPKDeklaracjaNaglowekKodFormularzaDekl = Field(
        validation_alias="KodFormularzaDekl",
        serialization_alias="KodFormularzaDekl"
    )
    wariant_formularza_dekl: Literal[23] = Field(
        validation_alias="WariantFormularzaDekl",
        serialization_alias="WariantFormularzaDekl"
    )

class JPKDeklaracjaPozycjeSzczegolowe(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    # Wszystkie pola opcjonalne zgodnie z XSD minOccurs="0", z wyjątkiem P_38 i P_51
    p_10: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_10", serialization_alias="P_10")
    p_11: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_11", serialization_alias="P_11")
    p_12: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_12", serialization_alias="P_12")
    p_13: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_13", serialization_alias="P_13")
    p_14: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_14", serialization_alias="P_14")
    p_15: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_15", serialization_alias="P_15")
    p_16: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_16", serialization_alias="P_16")
    p_17: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_17", serialization_alias="P_17")
    p_18: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_18", serialization_alias="P_18")
    p_19: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_19", serialization_alias="P_19")
    p_20: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_20", serialization_alias="P_20")
    p_21: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_21", serialization_alias="P_21")
    p_22: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_22", serialization_alias="P_22")
    p_23: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_23", serialization_alias="P_23")
    p_24: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_24", serialization_alias="P_24")
    p_25: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_25", serialization_alias="P_25")
    p_26: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_26", serialization_alias="P_26")
    p_27: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_27", serialization_alias="P_27")
    p_28: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_28", serialization_alias="P_28")
    p_29: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_29", serialization_alias="P_29")
    p_30: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_30", serialization_alias="P_30")
    p_31: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_31", serialization_alias="P_31")
    p_32: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_32", serialization_alias="P_32")
    p_33: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_33", serialization_alias="P_33")
    p_34: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_34", serialization_alias="P_34")
    p_35: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_35", serialization_alias="P_35")
    p_36: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_36", serialization_alias="P_36")
    p_360: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_360", serialization_alias="P_360")
    p_37: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_37", serialization_alias="P_37")
    p_38: TKwota2Dowolna = Field(validation_alias="P_38", serialization_alias="P_38")  # Wymagane
    p_39: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_39", serialization_alias="P_39")
    p_40: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_40", serialization_alias="P_40")
    p_41: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_41", serialization_alias="P_41")
    p_42: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_42", serialization_alias="P_42")
    p_43: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_43", serialization_alias="P_43")
    p_44: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_44", serialization_alias="P_44")
    p_45: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_45", serialization_alias="P_45")
    # P_46: maxInclusive 0
    p_46: Optional[Annotated[float, Field(le=0)]] = Field(None, validation_alias="P_46", serialization_alias="P_46")
    p_47: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_47", serialization_alias="P_47")
    p_48: Optional[TKwota2Dowolna] = Field(None, validation_alias="P_48", serialization_alias="P_48")
    p_49: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_49", serialization_alias="P_49")
    p_50: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_50", serialization_alias="P_50")
    p_51: TKwota2Nieujemna = Field(validation_alias="P_51", serialization_alias="P_51")  # Wymagane
    p_52: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_52", serialization_alias="P_52")
    p_53: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_53", serialization_alias="P_53")
    p_54: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_54", serialization_alias="P_54")
    p_540: Optional[TWybor1] = Field(None, validation_alias="P_540", serialization_alias="P_540")
    p_55: Optional[TWybor1] = Field(None, validation_alias="P_55", serialization_alias="P_55")
    p_56: Optional[TWybor1] = Field(None, validation_alias="P_56", serialization_alias="P_56")
    p_560: Optional[TWybor1] = Field(None, validation_alias="P_560", serialization_alias="P_560")
    p_58: Optional[TWybor1] = Field(None, validation_alias="P_58", serialization_alias="P_58")
    p_59: Optional[TWybor1] = Field(None, validation_alias="P_59", serialization_alias="P_59")
    p_60: Optional[Annotated[float, Field(gt=0)]] = Field(None, validation_alias="P_60", serialization_alias="P_60")
    p_61: Optional[str] = Field(None, validation_alias="P_61", serialization_alias="P_61")
    p_62: Optional[TKwota2Nieujemna] = Field(None, validation_alias="P_62", serialization_alias="P_62")
    p_63: Optional[TWybor1] = Field(None, validation_alias="P_63", serialization_alias="P_63")
    p_64: Optional[TWybor1] = Field(None, validation_alias="P_64", serialization_alias="P_64")
    p_65: Optional[TWybor1] = Field(None, validation_alias="P_65", serialization_alias="P_65")
    p_66: Optional[TWybor1] = Field(None, validation_alias="P_66", serialization_alias="P_66")
    p_660: Optional[TWybor1] = Field(None, validation_alias="P_660", serialization_alias="P_660")
    p_67: Optional[TWybor1] = Field(None, validation_alias="P_67", serialization_alias="P_67")
    # P_68 i P_69: maxInclusive 0
    p_68: Optional[Annotated[float, Field(le=0)]] = Field(None, validation_alias="P_68", serialization_alias="P_68")
    p_69: Optional[Annotated[float, Field(le=0)]] = Field(None, validation_alias="P_69", serialization_alias="P_69")
    p_ordzu: Optional[str] = Field(None, validation_alias="P_ORDZU", serialization_alias="P_ORDZU")

class JPKDeklaracja(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    naglowek: JPKDeklaracjaNaglowek = Field(
        validation_alias="Naglowek",
        serialization_alias="Naglowek"
    )
    pozycje_szczegolowe: JPKDeklaracjaPozycjeSzczegolowe = Field(
        validation_alias="PozycjeSzczegolowe",
        serialization_alias="PozycjeSzczegolowe"
    )
    # Pouczenia: wartość 1 (minExclusive 0, maxExclusive 2, fractionDigits 0)
    pouczenia: Literal[1] = Field(
        validation_alias="Pouczenia",
        serialization_alias="Pouczenia"
    )

# --- Ewidencja ---

class JPKEwidencjaSprzedazWiersz(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    lp_sprzedazy: int = Field(validation_alias="LpSprzedazy", serialization_alias="LpSprzedazy")
    kod_kraju_nadania_tin: Optional[str] = Field(None, validation_alias="KodKrajuNadaniaTIN", serialization_alias="KodKrajuNadaniaTIN")
    nr_kontrahenta: str = Field(validation_alias="NrKontrahenta", serialization_alias="NrKontrahenta")
    nazwa_kontrahenta: str = Field(validation_alias="NazwaKontrahenta", serialization_alias="NazwaKontrahenta", max_length=512)
    dowod_sprzedazy: str = Field(validation_alias="DowodSprzedazy", serialization_alias="DowodSprzedazy", max_length=256)
    data_wystawienia: TDataT = Field(validation_alias="DataWystawienia", serialization_alias="DataWystawienia")
    data_sprzedazy: Optional[TDataT] = Field(None, validation_alias="DataSprzedazy", serialization_alias="DataSprzedazy")

    # XSD: choice - tylko jedno z pól NrKSeF, OFF, BFK, DI
    nr_ksef: Optional[str] = Field(None, validation_alias="NrKSeF", serialization_alias="NrKSeF")
    off: Optional[TWybor1] = Field(None, validation_alias="OFF", serialization_alias="OFF")
    bfk: Optional[TWybor1] = Field(None, validation_alias="BFK", serialization_alias="BFK")
    di: Optional[TWybor1] = Field(None, validation_alias="DI", serialization_alias="DI")

    typ_dokumentu: Optional[TDowoduSprzedazy] = Field(None, validation_alias="TypDokumentu", serialization_alias="TypDokumentu")

    # Pola GTU (opcjonalne)
    gtu_01: Optional[TWybor1] = Field(None, validation_alias="GTU_01", serialization_alias="GTU_01")
    gtu_02: Optional[TWybor1] = Field(None, validation_alias="GTU_02", serialization_alias="GTU_02")
    gtu_03: Optional[TWybor1] = Field(None, validation_alias="GTU_03", serialization_alias="GTU_03")
    gtu_04: Optional[TWybor1] = Field(None, validation_alias="GTU_04", serialization_alias="GTU_04")
    gtu_05: Optional[TWybor1] = Field(None, validation_alias="GTU_05", serialization_alias="GTU_05")
    gtu_06: Optional[TWybor1] = Field(None, validation_alias="GTU_06", serialization_alias="GTU_06")
    gtu_07: Optional[TWybor1] = Field(None, validation_alias="GTU_07", serialization_alias="GTU_07")
    gtu_08: Optional[TWybor1] = Field(None, validation_alias="GTU_08", serialization_alias="GTU_08")
    gtu_09: Optional[TWybor1] = Field(None, validation_alias="GTU_09", serialization_alias="GTU_09")
    gtu_10: Optional[TWybor1] = Field(None, validation_alias="GTU_10", serialization_alias="GTU_10")
    gtu_11: Optional[TWybor1] = Field(None, validation_alias="GTU_11", serialization_alias="GTU_11")
    gtu_12: Optional[TWybor1] = Field(None, validation_alias="GTU_12", serialization_alias="GTU_12")
    gtu_13: Optional[TWybor1] = Field(None, validation_alias="GTU_13", serialization_alias="GTU_13")

    # Procedury (opcjonalne)
    wsto_ee: Optional[TWybor1] = Field(None, validation_alias="WSTO_EE", serialization_alias="WSTO_EE")
    ied: Optional[TWybor1] = Field(None, validation_alias="IED", serialization_alias="IED")
    tp: Optional[TWybor1] = Field(None, validation_alias="TP", serialization_alias="TP")
    tt_wnt: Optional[TWybor1] = Field(None, validation_alias="TT_WNT", serialization_alias="TT_WNT")
    tt_d: Optional[TWybor1] = Field(None, validation_alias="TT_D", serialization_alias="TT_D")
    mr_t: Optional[TWybor1] = Field(None, validation_alias="MR_T", serialization_alias="MR_T")
    mr_uz: Optional[TWybor1] = Field(None, validation_alias="MR_UZ", serialization_alias="MR_UZ")
    i_42: Optional[TWybor1] = Field(None, validation_alias="I_42", serialization_alias="I_42")
    i_63: Optional[TWybor1] = Field(None, validation_alias="I_63", serialization_alias="I_63")
    b_spv: Optional[TWybor1] = Field(None, validation_alias="B_SPV", serialization_alias="B_SPV")
    b_spv_dostawa: Optional[TWybor1] = Field(None, validation_alias="B_SPV_DOSTAWA", serialization_alias="B_SPV_DOSTAWA")
    b_mpv_prowizja: Optional[TWybor1] = Field(None, validation_alias="B_MPV_PROWIZJA", serialization_alias="B_MPV_PROWIZJA")

    # Korekta (opcjonalna sequence w XSD)
    korekta_podstawy_opodt: Optional[TWybor1] = Field(None, validation_alias="KorektaPodstawyOpodt", serialization_alias="KorektaPodstawyOpodt")
    termin_platnosci: Optional[TDataTP] = Field(None, validation_alias="TerminPlatnosci", serialization_alias="TerminPlatnosci")
    data_zaplaty: Optional[TDataTP] = Field(None, validation_alias="DataZaplaty", serialization_alias="DataZaplaty")

    # Kwoty - wszystkie opcjonalne
    k_10: Optional[float] = Field(None, validation_alias="K_10", serialization_alias="K_10")
    k_11: Optional[float] = Field(None, validation_alias="K_11", serialization_alias="K_11")
    k_12: Optional[float] = Field(None, validation_alias="K_12", serialization_alias="K_12")
    k_13: Optional[float] = Field(None, validation_alias="K_13", serialization_alias="K_13")
    k_14: Optional[float] = Field(None, validation_alias="K_14", serialization_alias="K_14")
    k_15: Optional[float] = Field(None, validation_alias="K_15", serialization_alias="K_15")
    k_16: Optional[float] = Field(None, validation_alias="K_16", serialization_alias="K_16")
    k_17: Optional[float] = Field(None, validation_alias="K_17", serialization_alias="K_17")
    k_18: Optional[float] = Field(None, validation_alias="K_18", serialization_alias="K_18")
    k_19: Optional[float] = Field(None, validation_alias="K_19", serialization_alias="K_19")
    k_20: Optional[float] = Field(None, validation_alias="K_20", serialization_alias="K_20")
    k_21: Optional[float] = Field(None, validation_alias="K_21", serialization_alias="K_21")
    k_22: Optional[float] = Field(None, validation_alias="K_22", serialization_alias="K_22")
    k_23: Optional[float] = Field(None, validation_alias="K_23", serialization_alias="K_23")
    k_24: Optional[float] = Field(None, validation_alias="K_24", serialization_alias="K_24")
    k_25: Optional[float] = Field(None, validation_alias="K_25", serialization_alias="K_25")
    k_26: Optional[float] = Field(None, validation_alias="K_26", serialization_alias="K_26")
    k_27: Optional[float] = Field(None, validation_alias="K_27", serialization_alias="K_27")
    k_28: Optional[float] = Field(None, validation_alias="K_28", serialization_alias="K_28")
    k_29: Optional[float] = Field(None, validation_alias="K_29", serialization_alias="K_29")
    k_30: Optional[float] = Field(None, validation_alias="K_30", serialization_alias="K_30")
    k_31: Optional[float] = Field(None, validation_alias="K_31", serialization_alias="K_31")
    k_32: Optional[float] = Field(None, validation_alias="K_32", serialization_alias="K_32")
    k_33: Optional[float] = Field(None, validation_alias="K_33", serialization_alias="K_33")
    k_34: Optional[float] = Field(None, validation_alias="K_34", serialization_alias="K_34")
    k_35: Optional[float] = Field(None, validation_alias="K_35", serialization_alias="K_35")
    k_36: Optional[float] = Field(None, validation_alias="K_36", serialization_alias="K_36")
    k_360: Optional[float] = Field(None, validation_alias="K_360", serialization_alias="K_360")
    sprzedaz_vat_marza: Optional[float] = Field(None, validation_alias="SprzedazVAT_Marza", serialization_alias="SprzedazVAT_Marza")

    @field_validator("nr_ksef", "off", "bfk", "di")
    @classmethod
    def validate_choice_ksef(cls, v, info):
        # Sprawdzenie że tylko jedno pole z choice jest wypełnione
        values = info.data
        filled = sum([
            values.get("nr_ksef") is not None,
            values.get("off") is not None,
            values.get("bfk") is not None,
            values.get("di") is not None
        ])
        if filled != 1:
            raise ValueError("Dokładnie jedno z pól NrKSeF, OFF, BFK, DI musi być wypełnione")
        return v

class JPKEwidencjaSprzedazCtrl(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    liczba_wierszy_sprzedazy: int = Field(validation_alias="LiczbaWierszySprzedazy", serialization_alias="LiczbaWierszySprzedazy")
    podatek_nalezny: float = Field(validation_alias="PodatekNalezny", serialization_alias="PodatekNalezny")

class JPKEwidencjaZakupWiersz(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    lp_zakupu: int = Field(validation_alias="LpZakupu", serialization_alias="LpZakupu")
    kod_kraju_nadania_tin: Optional[str] = Field(None, validation_alias="KodKrajuNadaniaTIN", serialization_alias="KodKrajuNadaniaTIN")
    nr_dostawcy: str = Field(validation_alias="NrDostawcy", serialization_alias="NrDostawcy")
    nazwa_dostawcy: str = Field(validation_alias="NazwaDostawcy", serialization_alias="NazwaDostawcy", max_length=512)
    dowod_zakupu: str = Field(validation_alias="DowodZakupu", serialization_alias="DowodZakupu", max_length=256)
    data_zakupu: TDataT = Field(validation_alias="DataZakupu", serialization_alias="DataZakupu")
    data_wplywu: Optional[TDataT] = Field(None, validation_alias="DataWplywu", serialization_alias="DataWplywu")

    # XSD: choice - tylko jedno z pól NrKSeF, OFF, BFK, DI
    nr_ksef: Optional[str] = Field(None, validation_alias="NrKSeF", serialization_alias="NrKSeF")
    off: Optional[TWybor1] = Field(None, validation_alias="OFF", serialization_alias="OFF")
    bfk: Optional[TWybor1] = Field(None, validation_alias="BFK", serialization_alias="BFK")
    di: Optional[TWybor1] = Field(None, validation_alias="DI", serialization_alias="DI")

    dokument_zakupu: Optional[TDowoduZakupu] = Field(None, validation_alias="DokumentZakupu", serialization_alias="DokumentZakupu")
    imp: Optional[TWybor1] = Field(None, validation_alias="IMP", serialization_alias="IMP")

    # Kwoty - opcjonalne sequences w XSD
    k_40: Optional[float] = Field(None, validation_alias="K_40", serialization_alias="K_40")
    k_41: Optional[float] = Field(None, validation_alias="K_41", serialization_alias="K_41")
    k_42: Optional[float] = Field(None, validation_alias="K_42", serialization_alias="K_42")
    k_43: Optional[float] = Field(None, validation_alias="K_43", serialization_alias="K_43")
    k_44: Optional[float] = Field(None, validation_alias="K_44", serialization_alias="K_44")
    k_45: Optional[float] = Field(None, validation_alias="K_45", serialization_alias="K_45")
    k_46: Optional[float] = Field(None, validation_alias="K_46", serialization_alias="K_46")
    k_47: Optional[float] = Field(None, validation_alias="K_47", serialization_alias="K_47")
    zakup_vat_marza: Optional[float] = Field(None, validation_alias="ZakupVAT_Marza", serialization_alias="ZakupVAT_Marza")

    @field_validator("nr_ksef", "off", "bfk", "di")
    @classmethod
    def validate_choice_ksef(cls, v, info):
        # Sprawdzenie że tylko jedno pole z choice jest wypełnione
        values = info.data
        filled = sum([
            values.get("nr_ksef") is not None,
            values.get("off") is not None,
            values.get("bfk") is not None,
            values.get("di") is not None
        ])
        if filled != 1:
            raise ValueError("Dokładnie jedno z pól NrKSeF, OFF, BFK, DI musi być wypełnione")
        return v

class JPKEwidencjaZakupCtrl(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    liczba_wierszy_zakupow: int = Field(validation_alias="LiczbaWierszyZakupow", serialization_alias="LiczbaWierszyZakupow")
    podatek_naliczony: float = Field(validation_alias="PodatekNaliczony", serialization_alias="PodatekNaliczony")

class JPKEwidencja(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    sprzedaz_wiersz: List[JPKEwidencjaSprzedazWiersz] = Field(
        default_factory=list,
        validation_alias="SprzedazWiersz",
        serialization_alias="SprzedazWiersz"
    )
    sprzedaz_ctrl: JPKEwidencjaSprzedazCtrl = Field(
        validation_alias="SprzedazCtrl",
        serialization_alias="SprzedazCtrl"
    )
    zakup_wiersz: List[JPKEwidencjaZakupWiersz] = Field(
        default_factory=list,
        validation_alias="ZakupWiersz",
        serialization_alias="ZakupWiersz"
    )
    zakup_ctrl: JPKEwidencjaZakupCtrl = Field(
        validation_alias="ZakupCtrl",
        serialization_alias="ZakupCtrl"
    )

class JPK(BaseModel):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    naglowek: JPKNaglowek = Field(
        validation_alias="Naglowek",
        serialization_alias="Naglowek"
    )
    podmiot1: JPKPodmiot1 = Field(
        validation_alias="Podmiot1",
        serialization_alias="Podmiot1"
    )
    deklaracja: Optional[JPKDeklaracja] = Field(
        None,
        validation_alias="Deklaracja",
        serialization_alias="Deklaracja"
    )
    ewidencja: Optional[JPKEwidencja] = Field(
        None,
        validation_alias="Ewidencja",
        serialization_alias="Ewidencja"
    )

class JpkVat7M3(BasicBasic):
    model_config = ConfigDict(populate_by_name=True, serialize_by_alias=True)

    model_name: str = Field(
        "JpkVat7M3",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    jpk: JPK = Field(
        validation_alias="JPK",
        serialization_alias="JPK"
    )

    class FormConfig:
        page_title = "JpkVat7M3"
        header = "Lista JpkVat7M3"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "company_id",
            "company_uuid"
        ]
        default_sort_field = "company_uuid"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "projections"
        collection = "jpk_vat7"
