# Created by Kelvin_Clark on 1/31/2022, 10:25 AM
from typing import Optional


class BugzaException(Exception):
    message: str


class UserAlreadyExistsException(BugzaException):
    message = "A user already exists with the provided credentials"
