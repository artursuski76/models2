# Counterparty.py

from typing import Optional, Union, Dict, Any

from pydantic import Field, model_serializer, ConfigDict, model_validator, BaseModel, AliasChoices

from models2.abase import BasicBasic
from models2.xxx.h_dane_identyfikacyjne import (OsobaFizyczna,
                                                PodatnikKrajowy,
                                                PodatnikVIES,
                                                PodatnikZagraniczny, Pracownik
                                                )
from models2.xxx.h_enums import WorldLandsEnum


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
        discriminator='rodzaj_kontr',
        validation_alias=AliasChoices("dane_identyfikacyjne", "DaneIdentyfikacyjne"),
        serialization_alias="DaneIdentyfikacyjne",
        title="Dane Kontrahenta"
    )

    @model_validator(mode="before")
    @classmethod
    def fix_dane_identyfikacyjne(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # 1. Pobieramy dane_identyfikacyjne (może być pod różnymi nazwami)
            dane = data.get("dane_identyfikacyjne") or data.get("DaneIdentyfikacyjne")
            
            # 2. Pobieramy rodzaj/typ transakcji z głównego poziomu lub zagnieżdżonego
            rodzaj = (
                data.get("rodzaj_kontr") or 
                data.get("typ_transakcji") or 
                (isinstance(dane, dict) and (dane.get("rodzaj_kontr") or dane.get("typ_transakcji")))
            )

            # 3. Jeśli nie ma klucza dane_identyfikacyjne, a mamy rodzaj, 
            # to prawdopodobnie mamy płaski input, który musimy "zwinąć"
            if dane is None and rodzaj:
                # Pydantic nie mapuje automatycznie płaskich pól na zagnieżdżony model w trybie before.
                # Aby uniknąć błędu brakującego pola 'dane_identyfikacyjne', 
                # tworzymy słownik i kopiujemy tam dane, które mogą do niego należeć.
                # W tym modelu dane_identyfikacyjne są kluczowe.
                dane = {**data}
                data["dane_identyfikacyjne"] = dane

            # 4. Zapewniamy obecność dyskryminatora rodzaj_kontr w słowniku dane_identyfikacyjne
            if isinstance(dane, dict) and rodzaj:
                dane["rodzaj_kontr"] = rodzaj
                
        return data

    @model_serializer(mode="wrap")
    def serialize_flat(self, handler) -> Dict[str, Any]:
        # Pobieramy standardowy słownik (wywołując oryginalny serializer)
        data = handler(self)

        # Wyciągamy dane identyfikacyjne
        dane_ident = data.pop("dane_identyfikacyjne", {})

        # Łączymy główny słownik z polami z dane_identyfikacyjne
        # Uwaga: Jeśli klucze się powtórzą, dane_ident nadpiszą te z poziomu głównego
        return {**data, **dane_ident}




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