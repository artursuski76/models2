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
    nip: str = Field(title="NIP",)
    nazwa: str = Field(title="Nazwa firmy",)
    regon: Optional[str] = Field(title="Regon",)
    krs: Optional[str] = Field(title="KRS",)
    adr_ulica_nr_domu: str = Field(title="Ulica i nr",)
    adr_kod_i_poczta: str = Field(title="Kod i poczta",)
    dek_imie: str = Field(title="Imię na deklaracji US",)
    dek_nazwisko: str = Field(title="Nazwisko na deklaracji US",)
    dek_tel: str = Field(title="Telefon na deklaracji US",)
    dek_email: str = Field(title="Email na deklaracji US",)
    dek_kod_us: str = Field(title="Kod US",)
    dek_nazwa_us: str = Field(title="Nazwa US",)



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