from datetime import datetime
from decimal import Decimal
from typing import Literal, Annotated
from pydantic import conint, StringConstraints

TKodKraju = Annotated[str, StringConstraints(min_length=2, max_length=2, pattern=r"[A-Z]{2}")]
TNrNIP = Annotated[str, StringConstraints(pattern=r"\d{10}")]
TKodyKrajowUE = Literal["AT", "BE", "BG", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "EL", "HR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "XI"]
TKodWaluty = Literal["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "UYI", "UYU", "UYW", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XCG", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"]
TKodFormularza = Literal["FA"]
TKwotowy = Decimal
TKwotowy2 = Decimal
TNaturalny = conint(ge=1)
TZnakowy = Annotated[str, StringConstraints(min_length=1, max_length=256)]
TZnakowy2 = Annotated[str, StringConstraints(min_length=0, max_length=256)]
TZnakowy20 = Annotated[str, StringConstraints(min_length=1, max_length=20)]
TZnakowy50 = Annotated[str, StringConstraints(min_length=1, max_length=50)]
TZnakowy512 = Annotated[str, StringConstraints(min_length=1, max_length=512)]
BrakID_Literal1 = Literal[1]
TNumerKSeF = Annotated[str, StringConstraints(pattern=r"([1-9]((\\d[1-9])|([1-9]\\d))\\d{7}|M\\d{9}|[A-Z]{3}\\d{7})-(20[2-9][0-9]|2[1-9][0-9]{2}|[3-9][0-9]{3})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])-([0-9A-F]{6})-?([0-9A-F]{6})-([0-9A-F]{2})")]
TIlosci = Decimal
TData = datetime
TDataT = datetime
TDataU = datetime
TDataCzas = datetime
TNrVatUE = Annotated[str, StringConstraints(pattern=r"(\\d|[A-Z]|\\+|\\*){1,12}")]
TNIPIdWew = Annotated[str, StringConstraints(pattern=r"[1-9]((\d[1-9])|([1-9]\d))\d{7}-\d{5}")]
TNrRB = Annotated[str, StringConstraints(min_length=10, max_length=34)]
SWIFT_Type = Annotated[str, StringConstraints(pattern=r"[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3}){0,1}")]
TFormaPlatnosci = Literal[1, "1", 2, "2", 3, "3", 4, "4", 5, "5", 6, "6", 7, "7"]
TLadunek = Literal[1, "1", 2, "2", 3, "3", 4, "4", 5, "5", 6, "6", 7, "7", 8, "8", 9, "9", 10, "10", 11, "11", 12, "12", 13, "13", 14, "14", 15, "15", 16, "16", 17, "17", 18, "18", 19, "19", 20, "20"]
TProcentowy = Decimal
TRachunekWlasnyBanku = Literal[1, "1", 2, "2", 3, "3"]
TStatusInfoPodatnika = Literal[1, "1", 2, "2", 3, "3", 4, "4"]
TRolaPodmiotuUpowaznionego = Literal[1, "1", 2, "2", 3, "3"]
TRolaPodmiotu3 = Literal[1, "1", 2, "2", 3, "3", 4, "4", 5, "5", 6, "6", 7, "7", 8, "8", 9, "9", 10, "10", 11, "11"]
TNumerTelefonu = Annotated[str, StringConstraints(max_length=16)] # fallback for tns:TZnakowy
TRodzajFaktury = Literal["VAT", "KOR", "ZAL", "ROZ", "UPR", "KOR_ZAL", "KOR_ROZ"]
TTypKorekty = Literal[1, "1", 2, "2", 3, "3"]
TStawkaPodatku = Literal[23, "23", 22, "22", 8, "8", 7, "7", 5, "5", 4, "4", 3, "3", "0 KR", "0 WDT", "0 EX", "zw", "oo", "np I", "np II"]
TOznaczenieProcedury = Literal["WSTO_EE", "IED", "TT_D", "I_42", "I_63", "B_SPV", "B_SPV_DOSTAWA", "B_MPV_PROWIZJA"]
TOznaczenieProceduryZ = Literal["WSTO_EE", "IED", "TT_D", "B_SPV", "B_SPV_DOSTAWA", "B_MPV_PROWIZJA"]
TGTU = Literal["GTU_01", "GTU_02", "GTU_03", "GTU_04", "GTU_05", "GTU_06", "GTU_07", "GTU_08", "GTU_09", "GTU_10", "GTU_11", "GTU_12", "GTU_13"]
TGLN = Annotated[str, StringConstraints(min_length=1, max_length=13)]
TRodzajTransportu = Literal[1, "1", 2, "2", 3, "3", 4, "4", 5, "5", 7, "7", 8, "8"]
TTekstowy = Annotated[str, StringConstraints(min_length=1, max_length=3500)]
TNrKRS = Annotated[str, StringConstraints(pattern=r"\d{10}")]
TNrREGON = Annotated[str, StringConstraints(pattern=r"\d{9}|\d{14}")]
TZnakowy9 = Annotated[str, StringConstraints(min_length=1, max_length=9)]
TWybor1_2 = Literal[1, "1", 2, "2"]
TWybor1 = Literal[1, "1"]

