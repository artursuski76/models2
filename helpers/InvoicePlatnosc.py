from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from models2.helpers.platnosc import FormaPlatnosci


class InvoicePlatnosc(BaseModel):


    platnosc_termin: Optional[date] = Field(
        None,
        title="Termin płatności",
    )
    platnosc_forma: Optional[FormaPlatnosci] = Field(
        FormaPlatnosci.PRZELEW,
        title="Forma płatności",
        json_schema_extra={"type": "string"}
    )

    zaplacono: Optional[bool] = Field(
        None
    )
    rb_nr: Optional[str] = Field(
        None,
        title="Nr rachunku bankowego",
    )
    rb_nazwa_banku: Optional[str] = Field(
        None,
        title="Nazwa banku",
    )
    rb_opis: Optional[str] = Field(
        default="Rachunek bieżący",
        title="Opis rachunku",
    )