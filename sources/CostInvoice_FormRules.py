# AUTO-GENERATED FORM RULES
# Generated from models2/sources/CostInvoice.py

FORM_RULES = {
    "files": {
        "type": "list<TransactionFiles>",
        "required": false,
        "visibleIf": {
            "source": "EXPECTED_VALUE"
        },
        "label": "files"
    },
    "transaction_type": {
        "type": "union",
        "required": true,
        "visibleIf": {},
        "label": "Typ transakcji",
        "alias": "TypTransakcji"
    },
    "adnotacje": {
        "type": "union",
        "required": true,
        "visibleIf": {},
        "label": "Adnotcje",
        "alias": "Adnotacje"
    },
    "inv_nr": {
        "type": "str",
        "required": true,
        "visibleIf": {},
        "label": "inv_nr"
    },
    "date_posting": {
        "type": "date",
        "required": true,
        "visibleIf": {},
        "label": "Data księgowania"
    },
    "counterparty_id": {
        "type": "str",
        "required": true,
        "visibleIf": {},
        "label": "Kontrahent"
    },
    "currency": {
        "type": "CurrencyAB",
        "required": false,
        "visibleIf": {
            "source": "EXPECTED_VALUE"
        },
        "label": "Waluta",
        "alias": "Waluta",
        "options": [
            "PLN",
            "EUR",
            "USD",
            "RUB",
            "CHF",
            "GBP",
            "AUD",
            "BGN",
            "BRL",
            "CAD",
            "CLP",
            "CNY",
            "CZK",
            "DKK",
            "HKD",
            "HUF",
            "IDR",
            "ILS",
            "INR",
            "ISK",
            "JPY",
            "KRW",
            "MXN",
            "MYR",
            "NOK",
            "NZD",
            "PHP",
            "RON",
            "SEK",
            "SGD",
            "THB",
            "TRY",
            "UAH",
            "XDR",
            "ZAR"
        ]
    },
    "total_net": {
        "type": "Decimal",
        "required": true,
        "visibleIf": {},
        "label": "Razem Netto"
    },
    "total_vat": {
        "type": "Decimal",
        "required": true,
        "visibleIf": {},
        "label": "Razem VAT"
    },
    "total_gross": {
        "type": "Decimal",
        "required": true,
        "visibleIf": {},
        "label": "Razem Brutto"
    },
    "rodzaj_fv_obj": {
        "type": "union<rodzaj_fv>",
        "required": false,
        "visibleIf": {
            "source": "EXPECTED_VALUE"
        },
        "label": "Typ transakcji",
        "subRules": {
            "Podstawowa": {},
            "Zaliczkowa": {},
            "Rozliczeniowa": {},
            "Korekta": {
                "transaction_items_after": {
                    "type": "list<union<vat_category>>",
                    "required": false,
                    "visibleIf": {
                        "rodzaj_fv": "Korekta"
                    },
                    "label": "Pozycje księgowania",
                    "alias": "WierszTransakcji",
                    "subRules": {
                        "wybierz": {
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {},
                                "label": "Wybierz typ pozycji...",
                                "options": [
                                    "wybierz"
                                ]
                            }
                        },
                        "import_tow_33a": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "import_tow_33a"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "import_tow_33a_inwentarz": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "import_tow_33a_inwentarz"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "import_tow_33a_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "import_tow_33a_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "import_uslug_28b": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "import_uslug_28b"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "import_uslug_28b_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "import_uslug_28b_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "import_uslug_nie_28b": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "import_uslug_nie_28b"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "import_uslug_nie_28b_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "import_uslug_nie_28b_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "nabycie_krajowe": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "nabycie_krajowe"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            }
                        },
                        "nabycie_krajowe_inwentarz": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "nabycie_krajowe_inwentarz"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            }
                        },
                        "nabycie_krajowe_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "nabycie_krajowe_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            }
                        },
                        "nie_podlega": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "nie_podlega"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            }
                        },
                        "nie_podlega_inwentarz": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "nie_podlega_inwentarz"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            }
                        },
                        "nie_podlega_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "nie_podlega_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            }
                        },
                        "oo_kraj_towar": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "oo_kraj_towar"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "oo_kraj_towar_inwentarz": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "oo_kraj_towar_inwentarz"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "oo_kraj_towar_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "oo_kraj_towar_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "oo_kraj_usluga": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "oo_kraj_usluga"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "oo_kraj_usluga_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "oo_kraj_usluga_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "wnt": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "wnt"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "wnt_inwentarz": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "wnt_inwentarz"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        },
                        "wnt_relacja": {
                            "row_type": {
                                "type": "CostRowType",
                                "required": false,
                                "visibleIf": {},
                                "label": "Typ pozycji",
                                "options": [
                                    "DAROWIZNY",
                                    "ENERGIA_CIEPLNA",
                                    "ENERGIA_GAZ",
                                    "ENERGIA_INNA",
                                    "ENERGIA_OLEJ_OPALOWY",
                                    "ENERGIA_PALIWA_SILNIKOWE",
                                    "ENERGIA_PRAD_ELEKTRYCZNY",
                                    "ENERGIA_WODA_SCIEKI",
                                    "INNE_FINANSOWE",
                                    "INNE_OPERACYJNE",
                                    "INNE_RODZAJOWE",
                                    "KARY_GRZYWNY_MANDATY",
                                    "MATERIALY_BIUROWE",
                                    "MATERIALY_CZESCI_ZAMIENNE",
                                    "MATERIALY_PRODUKCYJNE",
                                    "ODSETKI_BANKOWE",
                                    "ODSETKI_BUDZETOWE",
                                    "ODSETKI_HANDLOWE",
                                    "PODATKI_AKCYZOWE",
                                    "PODATKI_OD_NIERUCHOMOSCI",
                                    "PODATKI_OPLATY_INNE",
                                    "PODATKI_OPLATY_RECYC_SRODOW",
                                    "PODATKI_OPLATY_SADOWE",
                                    "PODATKI_OPLATY_SKARBOWE",
                                    "PODATKI_TRANSPORTOWE",
                                    "PODROZE_SLUZBOWE_INNE",
                                    "PODROZE_SLUZBOWE_NOCLEGI",
                                    "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                                    "PODROZE_SLUZBOWE_WYZYWIENIE",
                                    "REKLAMA",
                                    "REPREZENTACJA",
                                    "SWIAD_NA_RZECZ_PRACOWNIKOW",
                                    "UBEZPIECZENIA_MAJATKOWE",
                                    "USL_OBCE_DORADCZE",
                                    "USL_OBCE_INFORMATYCZNE",
                                    "USL_OBCE_INNE",
                                    "USL_OBCE_KSIEGOWE",
                                    "USL_OBCE_LEASINGI",
                                    "USL_OBCE_NAJMY_CZYNSZE",
                                    "USL_OBCE_PRAWNE",
                                    "USL_OBCE_TELEKOMUNIKACYJNE",
                                    "USL_OBCE_TRANSPORTOWE",
                                    "WARTOSC_SPRZEDANYCH_TOWAROW",
                                    "ZALICZKI_NA_DOSTAWY",
                                    "ZAPASY_MATERIALY",
                                    "ZAPASY_TOWARY",
                                    "ZAPASY_TOWARY_W_DRODZE",
                                    "ZDARZENIA_LOSOWE"
                                ]
                            },
                            "amount_net": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Netto"
                            },
                            "amount_vat": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "VAT"
                            },
                            "amount_gross": {
                                "type": "Decimal",
                                "required": true,
                                "visibleIf": {},
                                "label": "Brutto"
                            },
                            "vat_category": {
                                "type": "literal",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "vat_category",
                                "options": [
                                    "wnt_relacja"
                                ]
                            },
                            "description": {
                                "type": "optional<str>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Opis"
                            },
                            "inventory_item_id": {
                                "type": "str",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "Kod inwent."
                            },
                            "vat_rate_doc": {
                                "type": "int",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_doc %"
                            },
                            "vat_rate_jpk": {
                                "type": "optional<int>",
                                "required": false,
                                "visibleIf": {
                                    "row_type": "EXPECTED_VALUE"
                                },
                                "label": "VAT_jpk %"
                            }
                        }
                    },
                    "options": [
                        "import_tow_33a",
                        "import_tow_33a_inwentarz",
                        "import_tow_33a_relacja",
                        "import_uslug_28b",
                        "import_uslug_28b_relacja",
                        "import_uslug_nie_28b",
                        "import_uslug_nie_28b_relacja",
                        "nabycie_krajowe",
                        "nabycie_krajowe_inwentarz",
                        "nabycie_krajowe_relacja",
                        "nie_podlega",
                        "nie_podlega_inwentarz",
                        "nie_podlega_relacja",
                        "oo_kraj_towar",
                        "oo_kraj_towar_inwentarz",
                        "oo_kraj_towar_relacja",
                        "oo_kraj_usluga",
                        "oo_kraj_usluga_relacja",
                        "wnt",
                        "wnt_inwentarz",
                        "wnt_relacja",
                        "wybierz"
                    ]
                },
                "przyczyna_korekty": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "rodzaj_fv": "Korekta"
                    },
                    "label": "Przyczyna korekty",
                    "alias": "PrzyczynaKorekty"
                },
                "typ_korekty": {
                    "type": "SkutekPodatkowyKorekty",
                    "required": false,
                    "visibleIf": {
                        "rodzaj_fv": "Korekta"
                    },
                    "label": "Typ korekty",
                    "alias": "TypKorekty",
                    "options": [
                        "W_DACIE_FA_PIERW",
                        "W_DACIE_FA_KOR",
                        "W_DACIE_INNEJ"
                    ]
                },
                "dane_fa_korygowanej": {
                    "type": "DaneFaKorygowanej",
                    "required": false,
                    "visibleIf": {
                        "rodzaj_fv": "Korekta"
                    },
                    "label": "Dane FA korygowane",
                    "alias": "DaneFAKorygowane"
                }
            }
        },
        "options": [
            "Korekta",
            "Podstawowa",
            "Rozliczeniowa",
            "Zaliczkowa"
        ]
    },
    "transaction_items": {
        "type": "list<union<vat_category>>",
        "required": false,
        "visibleIf": {
            "source": "EXPECTED_VALUE"
        },
        "label": "Pozycje księgowania",
        "subRules": {
            "wybierz": {
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {},
                    "label": "Wybierz typ pozycji...",
                    "options": [
                        "wybierz"
                    ]
                }
            },
            "import_tow_33a": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "import_tow_33a"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "import_tow_33a_inwentarz": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "import_tow_33a_inwentarz"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "import_tow_33a_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "import_tow_33a_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "import_uslug_28b": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "import_uslug_28b"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "import_uslug_28b_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "import_uslug_28b_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "import_uslug_nie_28b": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "import_uslug_nie_28b"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "import_uslug_nie_28b_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "import_uslug_nie_28b_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "nabycie_krajowe": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "nabycie_krajowe"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                }
            },
            "nabycie_krajowe_inwentarz": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "nabycie_krajowe_inwentarz"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                }
            },
            "nabycie_krajowe_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "nabycie_krajowe_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                }
            },
            "nie_podlega": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "nie_podlega"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                }
            },
            "nie_podlega_inwentarz": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "nie_podlega_inwentarz"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                }
            },
            "nie_podlega_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "nie_podlega_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                }
            },
            "oo_kraj_towar": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "oo_kraj_towar"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "oo_kraj_towar_inwentarz": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "oo_kraj_towar_inwentarz"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "oo_kraj_towar_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "oo_kraj_towar_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "oo_kraj_usluga": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "oo_kraj_usluga"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "oo_kraj_usluga_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "oo_kraj_usluga_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "wnt": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "wnt"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "wnt_inwentarz": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "wnt_inwentarz"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            },
            "wnt_relacja": {
                "row_type": {
                    "type": "CostRowType",
                    "required": false,
                    "visibleIf": {},
                    "label": "Typ pozycji",
                    "options": [
                        "DAROWIZNY",
                        "ENERGIA_CIEPLNA",
                        "ENERGIA_GAZ",
                        "ENERGIA_INNA",
                        "ENERGIA_OLEJ_OPALOWY",
                        "ENERGIA_PALIWA_SILNIKOWE",
                        "ENERGIA_PRAD_ELEKTRYCZNY",
                        "ENERGIA_WODA_SCIEKI",
                        "INNE_FINANSOWE",
                        "INNE_OPERACYJNE",
                        "INNE_RODZAJOWE",
                        "KARY_GRZYWNY_MANDATY",
                        "MATERIALY_BIUROWE",
                        "MATERIALY_CZESCI_ZAMIENNE",
                        "MATERIALY_PRODUKCYJNE",
                        "ODSETKI_BANKOWE",
                        "ODSETKI_BUDZETOWE",
                        "ODSETKI_HANDLOWE",
                        "PODATKI_AKCYZOWE",
                        "PODATKI_OD_NIERUCHOMOSCI",
                        "PODATKI_OPLATY_INNE",
                        "PODATKI_OPLATY_RECYC_SRODOW",
                        "PODATKI_OPLATY_SADOWE",
                        "PODATKI_OPLATY_SKARBOWE",
                        "PODATKI_TRANSPORTOWE",
                        "PODROZE_SLUZBOWE_INNE",
                        "PODROZE_SLUZBOWE_NOCLEGI",
                        "PODROZE_SLUZBOWE_OPLATY_DROGOWE",
                        "PODROZE_SLUZBOWE_WYZYWIENIE",
                        "REKLAMA",
                        "REPREZENTACJA",
                        "SWIAD_NA_RZECZ_PRACOWNIKOW",
                        "UBEZPIECZENIA_MAJATKOWE",
                        "USL_OBCE_DORADCZE",
                        "USL_OBCE_INFORMATYCZNE",
                        "USL_OBCE_INNE",
                        "USL_OBCE_KSIEGOWE",
                        "USL_OBCE_LEASINGI",
                        "USL_OBCE_NAJMY_CZYNSZE",
                        "USL_OBCE_PRAWNE",
                        "USL_OBCE_TELEKOMUNIKACYJNE",
                        "USL_OBCE_TRANSPORTOWE",
                        "WARTOSC_SPRZEDANYCH_TOWAROW",
                        "ZALICZKI_NA_DOSTAWY",
                        "ZAPASY_MATERIALY",
                        "ZAPASY_TOWARY",
                        "ZAPASY_TOWARY_W_DRODZE",
                        "ZDARZENIA_LOSOWE"
                    ]
                },
                "amount_net": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Netto"
                },
                "amount_vat": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "VAT"
                },
                "amount_gross": {
                    "type": "Decimal",
                    "required": true,
                    "visibleIf": {},
                    "label": "Brutto"
                },
                "vat_category": {
                    "type": "literal",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "vat_category",
                    "options": [
                        "wnt_relacja"
                    ]
                },
                "description": {
                    "type": "optional<str>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Opis"
                },
                "inventory_item_id": {
                    "type": "str",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "Kod inwent."
                },
                "vat_rate_doc": {
                    "type": "int",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_doc %"
                },
                "vat_rate_jpk": {
                    "type": "optional<int>",
                    "required": false,
                    "visibleIf": {
                        "row_type": "EXPECTED_VALUE"
                    },
                    "label": "VAT_jpk %"
                }
            }
        },
        "options": [
            "import_tow_33a",
            "import_tow_33a_inwentarz",
            "import_tow_33a_relacja",
            "import_uslug_28b",
            "import_uslug_28b_relacja",
            "import_uslug_nie_28b",
            "import_uslug_nie_28b_relacja",
            "nabycie_krajowe",
            "nabycie_krajowe_inwentarz",
            "nabycie_krajowe_relacja",
            "nie_podlega",
            "nie_podlega_inwentarz",
            "nie_podlega_relacja",
            "oo_kraj_towar",
            "oo_kraj_towar_inwentarz",
            "oo_kraj_towar_relacja",
            "oo_kraj_usluga",
            "oo_kraj_usluga_relacja",
            "wnt",
            "wnt_inwentarz",
            "wnt_relacja",
            "wybierz"
        ]
    }
}
