from enum import Enum


class Query_type(Enum):
    COMPUTE = 0
    LIST = 1

class Query_Status(Enum):
    TO_BE_SENT = 0
    SCHEDULED = 1
    DONE = 2

class Query:
    def __init__(self, type : Query_type, value = None ) -> None:
        self.type = type
        self.value = value
        self.status = Query_Status.TO_BE_SENT
        self.result = None