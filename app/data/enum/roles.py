# Created by Kelvin_Clark on 1/30/2022, 9:54 PM
from enum import Enum
import strawberry


@strawberry.enum
class Role(str, Enum):
    ADMIN = "admin"
    SYSTEM_USER = "system_user"
    DEVELOPER = "developer"
    TESTER = "tester"
