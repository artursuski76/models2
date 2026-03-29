
from typing import Optional, Union, Dict, Any

from pydantic import Field, model_serializer, ConfigDict, model_validator, BaseModel, AliasChoices

from models2.xxx.h_dane_identyfikacyjne import (OsobaFizyczna,
                                               PodatnikKrajowy,
                                               PodatnikVIES,
                                               PodatnikZagraniczny, Pracownik
                                               )
from models2.xxx.h_enums import WorldLandsEnum
from models2.abase import BasicBasic

class AddressCounterparty(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True
    )

    address_l1: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("address_l1", "AddressL1"),
        serialization_alias="AddressL1",
        title="Ulica i nr",
        max_length=100
    )
    address_l2: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("address_l2", "AddressL2"),
        serialization_alias="AddressL2",
        title="Kod i poczta",
        max_length=100
    )
    address_country: WorldLandsEnum = Field(
        WorldLandsEnum.PL,
        validation_alias=AliasChoices("address_country", "AddressCountry"),
        serialization_alias="AddressCountry",
        title="Kraj",
    )

class Counterparty(BasicBasic):
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True
    )

    model_name: str = Field(
        "Counterparty",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )

    address: AddressCounterparty = Field(
        None,
        validation_alias=AliasChoices("address", "Address"),
        serialization_alias="Address",
        title="Adres",
    )

    dane_identyfikacyjne: Union[
        OsobaFizyczna,
        PodatnikKrajowy,
        PodatnikVIES,
        PodatnikZagraniczny,
        Pracownik
    ] = Field(
        ...,
        validation_alias=AliasChoices("dane_identyfikacyjne", "DaneIdentyfikacyjne"),
        serialization_alias="DaneIdentyfikacyjne",
        title="Dane Kontrahenta"
    )

    @model_validator(mode='before')
    @classmethod
    def fix_dane_identyfikacyjne_discriminator(cls, data: Any) -> Any:
        if isinstance(data, dict):
            di = data.get("dane_identyfikacyjne") or data.get("DaneIdentyfikacyjne")
            if isinstance(di, dict) and "rodzaj_kontr" not in di and "typ_transakcji" in di:
                di["rodzaj_kontr"] = di["typ_transakcji"]
        return data




    class FormConfig:

        list_view_fields = [
            "my_id", "nazwa", "type", "tax_id", "brak_id", "rodzaj_kontr",
            "address_country", "address_l2", "address_l1",
            "status", "last_sync", "created_at"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "references"
        collection = "counterparty"