import uuid

def generate_custom_my_id() -> str:
    return str(uuid.uuid4())[:18]