# Created by Kelvin_Clark on 1/31/2022, 12:10 PM
from typing import Optional

from pydantic import BaseModel

from app.data.enum.roles import Role


class UserIn(BaseModel):
    username: str
    email: str
    password: str
    role: Optional[Role] = Role.TESTER

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: Role
    token: Optional[str]
    token_type: Optional[str]

    class Config:
        orm_mode = True
