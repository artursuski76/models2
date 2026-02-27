# generate_form_rules_with_conditions.py
import os
import sys
import importlib.util
from pydantic import BaseModel
from typing import get_type_hints, Optional, Union, Literal, Annotated, get_origin, get_args
from enum import Enum

TEMPLATE = '''# AUTO-GENERATED FORM RULES
# Generated from {model_file}

FORM_RULES = {{
{fields}
}}
'''


def type_to_str(tp):
    """Konwertuje typ Pythona na string dla prostego formularza"""
    origin = get_origin(tp)
    args = get_args(tp)

    if origin is Annotated:
        # Wyciągamy bazowy typ z Annotated i sprawdzamy czy ma discriminator
        base_type = args[0]
        for metadata in args[1:]:
            if hasattr(metadata, 'discriminator'):
                return f"union<{metadata.discriminator}>"
        return type_to_str(base_type)

    if origin is Union:
        # Sprawdzamy czy to Optional (Union[T, None])
        if type(None) in args:
            non_none_args = [a for a in args if a is not type(None)]
            if len(non_none_args) == 1:
                return f"optional<{type_to_str(non_none_args[0])}>"
            return "optional<mixed>"
        return "union"

    if origin is list or tp is list:
        if args:
            return f"list<{type_to_str(args[0])}>"
        return "list"

    if origin is dict or tp is dict:
        return "dict"

    if origin is Literal:
        return "literal"

    # typy proste
    if hasattr(tp, "__name__"):
        return tp.__name__
    
    return str(tp)


def generate_form_rules(model_cls):
    fields_lines = []
    # Używamy include_extras=True aby dostać Annotated
    try:
        hints = get_type_hints(model_cls, include_extras=True)
    except Exception:
        hints = {}

    # Pydantic V2: model_fields
    model_fields = getattr(model_cls, "model_fields", {})
    if not model_fields:
        # fallback for Pydantic V1 if still needed
        model_fields = getattr(model_cls, "__fields__", {})

    # Szukamy dyskryminatora lub pierwszego Enuma/Literala jako pole sterujące widocznością
    parent_field_name = None
    for name, field in model_fields.items():
        hint = hints.get(name, getattr(field, "annotation", None))
        origin = get_origin(hint)
        if (isinstance(hint, type) and issubclass(hint, Enum)) or origin is Literal:
            parent_field_name = name
            break

    for name, field in model_fields.items():
        # Sprawdzamy czy pole ma być wykluczone z formularza
        # Pydantic V2: field.json_schema_extra
        extra = getattr(field, "json_schema_extra", {}) or {}
        if extra.get("exclude_from_form"):
            continue

        hint = hints.get(name, getattr(field, "annotation", None))
        field_type = type_to_str(hint)
        
        # Pydantic V2: field.is_required()
        if hasattr(field, "is_required"):
            required = field.is_required()
        else:
            required = getattr(field, "required", True)

        label = getattr(field, "title", None) or name
        alias = getattr(field, "alias", None)
        if alias == name:
            alias = None
        
        visible_if = {}
        # heurystyka: jeśli pole nie jest wymagane i mamy parent_field, dodajemy placeholder widoczności
        if not required and parent_field_name and name != parent_field_name:
            visible_if = {parent_field_name: "EXPECTED_VALUE"}

        # jeśli typ jest Enum lub Literal → wyciągamy opcje
        options = None
        if isinstance(hint, type) and issubclass(hint, Enum):
            options = [e.name for e in hint]
        elif get_origin(hint) is Literal:
            options = list(get_args(hint))

        option_str = f', "options": {options}' if options else ''
        alias_str = f', "alias": "{alias}"' if alias else ''
        label_str = f', "label": "{label}"'

        fields_lines.append(
            f'    "{name}": {{ "type": "{field_type}", "required": {required}, "visibleIf": {visible_if}{label_str}{alias_str}{option_str} }},'
        )
    return "\n".join(fields_lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_form_rules_with_conditions.py <path_to_model.py>")
        sys.exit(1)

    model_path = sys.argv[1]
    if not os.path.isfile(model_path):
        print(f"File not found: {model_path}")
        sys.exit(1)

    # Ustawienie PYTHONPATH
    current_dir = os.getcwd()
    if current_dir not in sys.path:
        sys.path.append(current_dir)
    parent_dir = os.path.dirname(current_dir)
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)

    module_name = os.path.splitext(os.path.basename(model_path))[0]
    
    try:
        spec = importlib.util.spec_from_file_location(module_name, model_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"Error loading module {model_path}: {e}")
        # Próba importu alternatywnego
        try:
            # Heurystyka: jeśli plik jest w sources/CostInvoice.py, spróbuj models2.sources.CostInvoice
            rel_path = os.path.relpath(model_path, os.getcwd())
            parts = rel_path.removesuffix(".py").split(os.sep)
            if parts[0] in ["sources", "basic", "helpers"]:
                import_name = "models2." + ".".join(parts)
            else:
                import_name = ".".join(parts)
            
            print(f"Attempting alternative import: {import_name}")
            module = importlib.import_module(import_name)
        except Exception as e2:
            print(f"Failed alternative import: {e2}")
            sys.exit(1)

    # Szukamy klas dziedziczących po BaseModel
    models = [getattr(module, attr) for attr in dir(module)
              if isinstance(getattr(module, attr), type)
              and issubclass(getattr(module, attr), BaseModel)
              and getattr(module, attr) != BaseModel]

    if not models:
        print("No Pydantic models found in the file.")
        sys.exit(1)

    # Tworzymy plik FormRules dla każdej klasy
    for model_cls in models:
        fields_str = generate_form_rules(model_cls)
        content = TEMPLATE.format(model_file=model_path, fields=fields_str)

        # Ścieżka docelowa
        dir_path = os.path.dirname(model_path)
        form_rules_file = os.path.join(dir_path, f"{model_cls.__name__}_FormRules.py")
        with open(form_rules_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"FormRules with conditions generated: {form_rules_file}")


if __name__ == "__main__":
    main()
