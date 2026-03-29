from __future__ import annotations

import secrets
from datetime import datetime, date, timezone
from typing import List
from typing import Optional, Union, Dict, Any

from pydantic import AliasChoices
from pydantic import Field, model_serializer, ConfigDict, model_validator

from models2.abase import BasicBasic
from models2.enums import SourceInvoiceSource, SaleKsefStatus, SourceInvoiceStatus
from models2.xxx.h_dane_identyfikacyjne import (OsobaFizyczna,
                                                PodatnikKrajowy,
                                                PodatnikVIES,
                                                PodatnikZagraniczny
                                                )
from models2.xxx.h_files import TransactionFiles


class SaleInvoiceBasic(BasicBasic):

    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True,
        title="Formularz Dodawania Sale Invoice"
    )





    my_id: str = Field(  # Zmieniono z UUID na str
        default_factory=lambda: secrets.token_urlsafe(16),
        json_schema_extra={"exclude_from_form": True}
    )



    source: SourceInvoiceSource = Field(
        SourceInvoiceSource.MANUAL,
        title="Zródło",
        json_schema_extra={"exclude_from_form": True}
    )

    counter: int = Field(
        default=0,
        json_schema_extra={"exclude_from_form": True}
    )

    # Pozostawiamy prefix/postfix, jeśli nadal mogą być używane,
    # ale dla formatu FA/counter możemy je zignorować lub nadpisać.
    prefix: str = Field(
        default="FA/",
        validation_alias=AliasChoices("Prefix", "prefix"),
        serialization_alias="Prefix",
        json_schema_extra={"exclude_from_form": True}

    )

    inv_nr: str = Field(
        default="",
        validation_alias=AliasChoices("inv_nr", "InvNr", "NumerFaktury"),
        serialization_alias="inv_nr",
        title="Numer faktury (fizyczny)",
        json_schema_extra={"exclude_from_form": True}
    )

    @model_validator(mode="after")
    def fill_inv_nr(self) -> "SaleInvoiceBasic":
        # Zawsze generujemy numer na podstawie prefix i counter
        # Dzięki temu inv_nr zawsze będzie zsynchronizowany z counter
        self.inv_nr = f"{self.prefix}{self.counter}"
        return self

    date_posting: date = Field(
        default_factory=lambda: date.today(),
        title="Data wystawienia",
        json_schema_extra={"exclude_from_form": True}
    )





    ksef_ref: Optional[str] = Field(
        None,
        validation_alias=AliasChoices( "KsefRef", "ksef_ref" ),
        serialization_alias="KsefRef",
        json_schema_extra={"exclude_from_form": True}
    )

    wyslij_do_ksef: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("WyslijDoKsef", "wyslij_do_ksef"),
        serialization_alias="WyslijDoKsef",
        json_schema_extra={"exclude_from_form": True}
    )

    ksef_status: SaleKsefStatus = Field(
        SaleKsefStatus.NOT_SENT,
        validation_alias=AliasChoices( "KsefStatus", "ksef_status" ),
        serialization_alias="KsefStatus",
        json_schema_extra={"exclude_from_form": True}
    )

    ksef_session_ref: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("KsefSessionRef", "ksef_session_ref"),
        serialization_alias="KsefSessionRef",
        json_schema_extra={"exclude_from_form": True}
    )

    ksef_invoice_ref: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("KsefInvoiceRef", "ksef_invoice_ref"),
        serialization_alias="KsefInvoiceRef",
        json_schema_extra={"exclude_from_form": True}
    )

    ksef_sent_at: Optional[datetime] = Field(
        None,
        validation_alias=AliasChoices("KsefSentAt", "ksef_sent_at"),
        serialization_alias="KsefSentAt",
        json_schema_extra={"exclude_from_form": True}
    )

    errors: List[dict] = Field(
        default_factory=list,
        validation_alias=AliasChoices("errors", "Bledy"),
        serialization_alias="errors",
        json_schema_extra={"exclude_from_form": True}
    )

    ksef_json_file: TransactionFiles | None = Field(
        default=None,
        validation_alias=AliasChoices( "KsefJsonFile", "ksef_json_file" ),
        serialization_alias="KsefJsonFile",
        json_schema_extra={"exclude_from_form": True}
    )
    ksef_xml_file: TransactionFiles | None = Field(
        default=None,
        validation_alias=AliasChoices( "KsefXmlFile", "ksef_xml_file" ),
        serialization_alias="KsefXmlFile",
        json_schema_extra={"exclude_from_form": True}
    )

    ksef_json: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("KsefJson", "ksef_json"),
        serialization_alias="KsefJson",
        json_schema_extra={"exclude_from_form": True}
    )

    accounting_status: SourceInvoiceStatus = Field(
        SourceInvoiceStatus.DRAFT,
        validation_alias=AliasChoices( "StatusKonta", "accounting_status" ),
        serialization_alias="StatusKonta",
        json_schema_extra={"exclude_from_form": True}
    )

    original_payload_ref: Optional[str] = Field(
        None,
        title="Oryg Payload Ref",
        json_schema_extra = {"exclude_from_form": True}

    )

    ksef_status_code: Optional[str] = Field(
        None,
        title="Status KSeF",
        json_schema_extra={
            "exclude_from_form": True
        }
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),  # Dodaj import timezone z datetime
        json_schema_extra={"exclude_from_form": True}
    )

# stare dane kontrahenta

    # c_rodzaj_kontr: Optional[str] = Field(
    #     None,
    #     validation_alias=AliasChoices("RodzajKontr", "p2_rodzaj_kontr", "c_rodzaj_kontr"),
    #     serialization_alias="RodzajKontr",
    #     title="Rodzaj kontrahenta",
    #     max_length=50,
    #     json_schema_extra={"exclude_from_form": True}
    # )
    #
    # c_nazwa: Optional[str] = Field(
    #     None,
    #     validation_alias=AliasChoices("Nazwa", "p2_nazwa", "c_nazwa"),
    #     serialization_alias="Nazwa",
    #     title="Pełna nazwa Kontrahenta",
    #     max_length=200,
    #     json_schema_extra={"exclude_from_form": True}
    # )
    # c_nip: Optional[str] = Field(
    #     None,
    #     validation_alias=AliasChoices("NIP", "p2_nip", "c_nip"),
    #     serialization_alias="NIP",
    #     title="NIP",
    #     min_length=10,
    #     max_length=10,
    #     pattern=r'^\d{10}$|^brak$',
    #     json_schema_extra={"exclude_from_form": True}
    # )
    # c_kod_ue: Optional[EuropeLandsEnum] = Field(
    #     None,
    #     validation_alias=AliasChoices("KodUE", "c_kod_ue", "p2_kod_ue"),
    #     serialization_alias="KodUE",
    #     title="VIESS – kod UE",
    #     json_schema_extra={"exclude_from_form": True}
    # )
    # c_nr_vat_ue: Optional[str] = Field(
    #     None,
    #     validation_alias=AliasChoices("NrVatUE", "c_nr_vat_ue", "p2_nr_vat_ue"),
    #     serialization_alias="NrVatUE",
    #     title="VIESS – nr identyfikacyjny bez kodu kraju",
    #     json_schema_extra={"exclude_from_form": True}
    # )
    #
    # c_kod_kraju: Optional[WorldLandsEnum] = Field(
    #     None,
    #     validation_alias=AliasChoices("KodKraju", "c_kod_kraju", "p2_kod_kraju"),
    #     serialization_alias="KodKraju",
    #     title="EKSPORT – kod kraju",
    #     json_schema_extra={"exclude_from_form": True}
    # )
    # c_tax_id: Optional[str] = Field(
    #     None,
    #     validation_alias=AliasChoices("NrID", "c_tax_id", "p2_tax_id"),
    #     serialization_alias="NrID",
    #     title="EKSPORT – Numer podatkowy",
    #     json_schema_extra={"exclude_from_form": True}
    # )




# NOWE DANE IDENTYFIKACYJNE KONTRAHENTA
    dane_identyfikacyjne: Union[
        OsobaFizyczna,
        PodatnikKrajowy,
        PodatnikVIES,
        PodatnikZagraniczny
    ] = Field(
        ...,
        discriminator='rodzaj_kontr',
        alias="DaneIdentyfikacyjne",
        title="Dane Kontrahenta"
    )

    @model_validator(mode="before")
    @classmethod
    def wrap_dane_identyfikacyjne(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # Jeśli dane_identyfikacyjne nie ma w słowniku, a jest rodzaj_kontr,
            # to próbujemy "zwinąć" płaskie pola do dane_identyfikacyjne.
            if "dane_identyfikacyjne" not in data and "DaneIdentyfikacyjne" not in data:
                if "rodzaj_kontr" in data:
                    # Pola, które mogą należeć do dane_identyfikacyjne
                    # Możemy po prostu przekazać cały słownik jako dane_identyfikacyjne,
                    # Pydantic wybierze to co potrzebuje dla konkretnego modelu z Union.
                    data["dane_identyfikacyjne"] = data.copy()
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

