class OsobaFizyczna(BaseModel):
    rodzaj_kontr: "osoba_fizyczna"
    brak_id: "1"

class PodatnikKrajowy(BaseModel):
    rodzaj_kontr: "podatnik_krajowy"
    nip: str

class PodatnikZagraniczny(BaseModel):
    rodzaj_kontr: "podatnik_zagraniczny"
    kod_kraju: WorldLandsEnum
    tax_id: str
