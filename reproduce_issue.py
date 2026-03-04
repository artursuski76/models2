from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class Twybor1(Enum):
    VALUE_1 = 1

@dataclass(kw_only=True)
class Tpodmiot2:
    nip: Optional[str] = field(default=None)
    brak_id: Optional[Twybor1] = field(default=None)
    nazwa: Optional[str] = field(default=None)

# Próba 1: brak_id jako string "1" (tak jak w OsobaFizyczna)
try:
    print("Próba 1: brak_id='1'")
    p1 = Tpodmiot2(brak_id="1", nazwa="Test")
    print("Sukces P1")
except Exception as e:
    print(f"Błąd P1: {e}")

# Próba 2: brak_id jako int 1
try:
    print("\nPróba 2: brak_id=1")
    p2 = Tpodmiot2(brak_id=1, nazwa="Test")
    print("Sukces P2")
except Exception as e:
    print(f"Błąd P2: {e}")

# Próba 3: nip jako int (np. 1234567890)
try:
    print("\nPróba 3: nip=1234567890")
    p3 = Tpodmiot2(nip=1234567890, nazwa="Test")
    print("Sukces P3")
except Exception as e:
    print(f"Błąd P3: {e}")

try:
    from xsdata.models.datatype import XmlDateTime
    from datetime import date, datetime

    print("\nPróba 5 (XmlDateTime) z datetime.now():")
    try:
        dt = datetime.now()
        xdt = XmlDateTime(dt)
        print(f"Sukces P5: {xdt}")
    except Exception as e:
        print(f"Błąd P5: {e}")

    print("\nPróba 6 (XmlDateTime) z date.today():")
    try:
        d = date.today()
        xdt = XmlDateTime(d)
        print(f"Sukces P6: {xdt}")
    except Exception as e:
        print(f"Błąd P6: {e}")

    print("\nPróba 7 (XmlDateTime) z stringiem '2024-01-01':")
    try:
        s = "2024-01-01"
        xdt = XmlDateTime(s)
        print(f"Sukces P7: {xdt}")
    except Exception as e:
        print(f"Błąd P7: {e}")

except ImportError:
    print("\nxsdata nie jest zainstalowana.")
