from enum import Enum

class VehicleCostType(str, Enum):
    CAPITAL = "capital"       # Limit 100k/225k (Rata kapitałowa)
    OPERATIONAL = "operational" # Limit 75% (Paliwo, serwis, myjnia)
    FINANCIAL = "financial"     # 100% CIT (Odsetki, prowizje)
    NONE = "none"               # Pozostałe (100% CIT / zgodnie z ustawieniami ogólnymi)

# Mapa mapująca Twoje rodzaje wydatków na typy kosztów pojazdu
EXPENSE_TYPE_TO_VEHICLE_LOGIC = {
    # --- OPERATIONAL (Limit 75% CIT przy użytku mieszanym) ---
    "energia_paliwa_silnikowe": VehicleCostType.OPERATIONAL,
    "materialy_czesci_zamienne": VehicleCostType.OPERATIONAL,
    "podroze_sluzbowe_oplaty_drogowe": VehicleCostType.OPERATIONAL,
    "usl_obce_transportowe": VehicleCostType.OPERATIONAL, # Jeśli dotyczy np. lawety dla auta firmowego
    "podatki_transportowe": VehicleCostType.OPERATIONAL,  # Podatek od środków transp. (jeśli dotyczy osobówek)
    
    # --- CAPITAL (Limit kwotowy 100k / 225k) ---
    "usl_obce_leasingi": VehicleCostType.CAPITAL, # Zakładamy, że tu księgujesz część kapitałową
    
    # --- FINANCIAL (Zawsze 100% CIT, bez limitu 100k i bez 75%) ---
    "odsetki_handlowe": VehicleCostType.FINANCIAL, # Tutaj powinny trafiać odsetki z raty leasingowej
    "usl_obce_bankowe": VehicleCostType.FINANCIAL, # Prowizje bankowe/leasingowe
    "inne_finansowe": VehicleCostType.FINANCIAL,

    # --- NONE (Standardowe koszty, brak specyficznej logiki pojazdowej) ---
    "darowizny": VehicleCostType.NONE,
    "energia_cieplna": VehicleCostType.NONE,
    "energia_gaz": VehicleCostType.NONE,
    "energia_inna": VehicleCostType.NONE,
    "energia_olej_opalowy": VehicleCostType.NONE,
    "energia_prad_elektryczny": VehicleCostType.NONE, # Uwaga: jeśli ładujesz elektryka w biurze, to może być OPERATIONAL!
    "energia_woda_scieki": VehicleCostType.NONE,
    "inne_operacyjne": VehicleCostType.NONE,
    "inne_rodzajowe": VehicleCostType.NONE,
    "kary_grzywny_mandaty": VehicleCostType.NONE, # Pamiętaj: mandaty to zawsze NKUP (0% CIT)
    "materialy_biurowe": VehicleCostType.NONE,
    "materialy_produkcyjne": VehicleCostType.NONE,
    "odsetki_bankowe": VehicleCostType.NONE,
    "odsetki_budzetowe": VehicleCostType.NONE, # Zawsze NKUP
    "podatki_akcyzowe": VehicleCostType.NONE,
    "podatki_od_nieruchomosci": VehicleCostType.NONE,
    "podatki_oplaty_inne": VehicleCostType.NONE,
    "podatki_oplaty_recyc_srodow": VehicleCostType.NONE,
    "podatki_oplaty_sadowe": VehicleCostType.NONE,
    "podatki_oplaty_skarbowe": VehicleCostType.NONE,
    "podroze_sluzbowe_inne": VehicleCostType.NONE,
    "podroze_sluzbowe_noclegi": VehicleCostType.NONE,
    "podroze_sluzbowe_wyzywienie": VehicleCostType.NONE,
    "reklama": VehicleCostType.NONE,
    "reprezentacja": VehicleCostType.NONE, # Zawsze NKUP
    "swiad_na_rzecz_pracownikow": VehicleCostType.NONE,
    "ubezpieczenia_majatkowe": VehicleCostType.NONE, # Uwaga: ubezpieczenie AC też ma limit 100k/150k!
    "usl_obce_doradcze": VehicleCostType.NONE,
    "usl_obce_informatyczne": VehicleCostType.NONE,
    "usl_obce_inne": VehicleCostType.NONE,
    "usl_obce_ksiegowe": VehicleCostType.NONE,
    "usl_obce_najmy_czynsze": VehicleCostType.NONE,
    "usl_obce_prawne": VehicleCostType.NONE,
    "usl_obce_telekomunikacyjne": VehicleCostType.NONE,
    "wartosc_sprzedanych_towarow": VehicleCostType.NONE,
    "zaliczki_na_dostawy": VehicleCostType.NONE,
    "zapasy_materialy": VehicleCostType.NONE,
    "zapasy_towary": VehicleCostType.NONE,
    "zapasy_towary_w_drodze": VehicleCostType.NONE,
    "zdarzenia_losowe": VehicleCostType.NONE,
}