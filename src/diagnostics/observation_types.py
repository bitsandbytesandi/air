from enum import Enum


class ObservationType(str, Enum):
    EVENT = "event"
    METRIC = "metric"
    TRACE = "trace"
    ERROR = "error"
    STATE = "state"
