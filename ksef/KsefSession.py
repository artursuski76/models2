from models2.abase import BasicBasic

class KsefSession(BasicBasic):
    sessionReferenceNumber: str
    status: str

    class Couchbase:
        bucket = "Accounting"
        scope = "services"
        collection = "ksef_session"