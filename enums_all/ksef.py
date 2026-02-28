from enum import Enum


class KSeFStatus(str, Enum):
    NOT_SENT = "not_sent"
    SENT = "sent"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    ERROR = "error"

    @classmethod
    def get_status_choices(cls):
        return [(status.value, status.value.capitalize()) for status in cls]