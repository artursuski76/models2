from enum import Enum


class ApiloTkoenKategoriePoz(str, Enum):
    POZYCJA_MAGAZYNOWA = "pozycja_magazynowa"
    WNIP = "wartosci_niematerialne_i_prawne"
    PRODUKT_WLASNY = "produkt_wlasny"
    PRODUKT = "produkt"
    USLUGA = "usluga"