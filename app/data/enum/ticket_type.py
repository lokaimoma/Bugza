# Created by Kelvin_Clark on 1/30/2022, 10:27 PM
from enum import Enum


class TicketType(str, Enum):
    ISSUE = "issue"
    FEATURE_REQUEST = "feature_request"

