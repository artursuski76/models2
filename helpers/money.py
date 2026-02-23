from typing import Annotated  # Dodano Annotated

from pydantic import BeforeValidator, PlainSerializer, \
    WithJsonSchema

from models2.helpers.to_grosze import to_grosze

# JUNI, GPT, to stara definicja jednostki pienieznej w groszach,
# juz nie bedziemy stosowac w calej aplikacji, bo przelicznikii sprawiaja bledy.

# Money = Annotated[
#     int,
#     BeforeValidator(to_grosze),
#     PlainSerializer(lambda v: float(v / 100), return_type=float, when_used='json'),
#     WithJsonSchema({"type": "number", "format": "decimal"})
# ]