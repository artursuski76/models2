from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, AliasChoices

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
