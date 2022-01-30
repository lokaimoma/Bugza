# Created by Kelvin_Clark on 1/30/2022, 10:39 PM
from enum import StrEnum


class TicketState(StrEnum):
    OPEN = "open"
    CLOSED = "closed"
    FIXED = "fixed"
    IMPLEMENTED = "implemented"
