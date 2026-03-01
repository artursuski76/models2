from decimal import Decimal
from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator

from models2.enums import CostRowType
# from models2.helpers.money import Money


class TransactionRowBase(BaseModel):
    # cost_account: str = Field(title="Konto")
    row_type: CostRowType = Field(
        CostRowType,
        title="Typ pozycji"
    )
    amount_net: Decimal = Field(..., max_digits=12, decimal_places=2, title="Netto")
    amount_vat: Decimal = Field(..., max_digits=12, decimal_places=2, title="VAT")
    amount_gross: Decimal = Field(..., max_digits=12, decimal_places=2, title="Brutto")

    quantity: Optional[Decimal] = Field(None, title="Ilość")
    uom: Optional[str] = Field(None, title="Jednostka miary")
    unit_price_net: Optional[Decimal] = Field(None, title="Cena jedn. netto")
    inventory_item_id: Optional[str] = Field(None, title="Kod inwent.", alias="inventory_ref")


class Wybierz(BaseModel):
    vat_category: Literal["wybierz"] = Field("wybierz", title="Wybierz typ pozycji...")

class ImportTow33a(TransactionRowBase):
    vat_category: Literal["import_tow_33a"] = "import_tow_33a"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportTow33aInwentarz(TransactionRowBase):
    vat_category: Literal["import_tow_33a_inwentarz"] = "import_tow_33a_inwentarz"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportTow33aRelacja(TransactionRowBase):
    vat_category: Literal["import_tow_33a_relacja"] = "import_tow_33a_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslug28B(TransactionRowBase):
    vat_category: Literal["import_uslug_28b"] = "import_uslug_28b"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )


    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslug28BRelacja(TransactionRowBase):
    vat_category: Literal["import_uslug_28b_relacja"] = "import_uslug_28b_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslugNie28B(TransactionRowBase):
    vat_category: Literal["import_uslug_nie_28b"] = "import_uslug_nie_28b"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslugNie28BRelacja(TransactionRowBase):
    vat_category: Literal["import_uslug_nie_28b_relacja"] = "import_uslug_nie_28b_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class NabycieKrajowe(TransactionRowBase):
    vat_category: Literal["nabycie_krajowe"] = "nabycie_krajowe"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=23, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23 ')
        return v



class NabycieKrajoweInwentarz(TransactionRowBase):
    vat_category: Literal["nabycie_krajowe_inwentarz"] = "nabycie_krajowe_inwentarz"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )

    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=23, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23 ')
        return v



class NabycieKrajoweRelacja(TransactionRowBase):
    vat_category: Literal["nabycie_krajowe_relacja"] = "nabycie_krajowe_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=23, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23 ')
        return v



class NiePodlega(TransactionRowBase):
    vat_category: Literal["nie_podlega"] = "nie_podlega"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v



class NiePodlegaInwentarz(TransactionRowBase):
    vat_category: Literal["nie_podlega_inwentarz"] = "nie_podlega_inwentarz"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v



class NiePodlegaRelacja(TransactionRowBase):
    vat_category: Literal["nie_podlega_relacja"] = "nie_podlega_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v



class OOKrajTowar(TransactionRowBase):
    vat_category: Literal["oo_kraj_towar"] = "oo_kraj_towar"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )


    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajTowarInwentarz(TransactionRowBase):
    vat_category: Literal["oo_kraj_towar_inwentarz"] = "oo_kraj_towar_inwentarz"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajTowarRelacja(TransactionRowBase):
    vat_category: Literal["oo_kraj_towar_relacja"] = "oo_kraj_towar_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajUsluga(TransactionRowBase):
    vat_category: Literal["oo_kraj_usluga"] = "oo_kraj_usluga"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajUslugaRelacja(TransactionRowBase):
    vat_category: Literal["oo_kraj_usluga_relacja"] = "oo_kraj_usluga_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class WNT(TransactionRowBase):
    vat_category: Literal["wnt"] = "wnt"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )


    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class WNTInwentarz(TransactionRowBase):
    vat_category: Literal["wnt_inwentarz"] = "wnt_inwentarz"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class WNTRelacja(TransactionRowBase):
    vat_category: Literal["wnt_relacja"] = "wnt_relacja"
    description: Optional[str] = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

