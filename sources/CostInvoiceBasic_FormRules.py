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
    }
}
