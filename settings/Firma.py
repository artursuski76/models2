from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic


class Firma(BasicBasic):
    __auto_id__ = False

    model_name: str = Field(
        "Firma",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        default="Settings:Firma",
        title="Unikalny ID, np.: Settings:Firma",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        json_schema_extra={"exclude_from_form": True}
    )
    nip: str = Field(None, title="NIP",)
    nazwa: str = Field(None, title="Nazwa firmy",)
    regon: str = Field(None, title="Regon",)
    krs: str = Field(None, title="KRS",)
    bdo: str = Field(None, title="BDO",)
    adr_kod_kraju: str = Field(None, title="Kod kraju",)
    adr_ulica_nr_domu: str = Field(None, title="Ulica i nr",)
    adr_kod_i_poczta: str = Field(None, title="Kod i poczta",)
    dek_imie: str = Field(None, title="Imię na deklaracji US",)
    dek_nazwisko: str = Field(None, title="Nazwisko na deklaracji US",)
    dek_tel: str = Field(None, title="Telefon na deklaracji US",)
    dek_email: str = Field(None, title="Email na deklaracji US",)
    dek_kod_us: str = Field(None, title="Kod US",)
    dek_nazwa_us: str = Field(None, title="Nazwa US",)
    fa_miejscowosc: str = Field(None, title="Miejscowość na fakturze",)
    fa_informacje: str = Field(None, title="Informacje o firmie",)
    fa_tel: str = Field(None, title="Telefon na fakturze",)
    fa_email: str = Field(None, title="Email na fakturze",)



    class FormConfig:
        prefill_initial_data = True

        list_view_fields = [
            "id", "name", "status", "tax_id", "currency",
            "date_created", "open_date", "tags",
            "last_sync", "my_id", "sync_status"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "settings"
        collection = "firma"