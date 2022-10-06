from enum import Enum
from unittest import result


class Query_type(Enum):
    COMPUTE_FIBO = 0
    LIST = 1,
    LIST_END = 2

    def __str__(self):
        if self.value == 0:
            return "fibo"
        if self.value == 1:
            return "list"
        if self.value == 2:
            return "list end"

class Query_Status(Enum):
    TO_BE_SENT = 0
    SCHEDULED = 1
    DONE = 2

    def __str__(self):
        if self.value == 0:
            return "to be sent"
        if self.value == 1:
            return "scheduled"
        if self.value == 2:
            return "done"

class Query:
    def __init__(self, type : Query_type, value = None ) -> None:
        self.type = type
        self.value = value
        self.status = Query_Status.TO_BE_SENT
        self.result = None
    def __str__(self):
        res = '[{0}] {1}'.format(self.status, self.type)
        if self.value != None:
            res += " " + str(self.value)
        if self.result != None:
            res += ' (result {0})'.format(self.result)
        return res