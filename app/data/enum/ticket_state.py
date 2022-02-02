# Created by Kelvin_Clark on 1/30/2022, 10:39 PM
from enum import Enum
import strawberry


@strawberry.enum
class TicketState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    FIXED = "fixed"
    IMPLEMENTED = "implemented"
