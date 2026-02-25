import uuid

def generate_custom_id() -> str:
    return uuid.uuid4().hex