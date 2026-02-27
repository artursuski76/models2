# AUTO-GENERATED FORM RULES
# Generated from models2/sources/CostInvoice.py

FORM_RULES = {
    "transaction_items_after": { "type": "list<union<vat_category>>", "required": False, "visibleIf": {'rodzaj_fv': 'EXPECTED_VALUE'}, "label": "Pozycje księgowania", "alias": "WierszTransakcji" },
    "przyczyna_korekty": { "type": "str", "required": False, "visibleIf": {'rodzaj_fv': 'EXPECTED_VALUE'}, "label": "Przyczyna korekty", "alias": "PrzyczynaKorekty" },
    "typ_korekty": { "type": "SkutekPodatkowyKorekty", "required": False, "visibleIf": {'rodzaj_fv': 'EXPECTED_VALUE'}, "label": "Typ korekty", "alias": "TypKorekty", "options": ['W_DACIE_FA_PIERW', 'W_DACIE_FA_KOR', 'W_DACIE_INNEJ'] },
    "dane_fa_korygowanej": { "type": "DaneFaKorygowanej", "required": False, "visibleIf": {'rodzaj_fv': 'EXPECTED_VALUE'}, "label": "Dane FA korygowane", "alias": "DaneFAKorygowane" },
}
