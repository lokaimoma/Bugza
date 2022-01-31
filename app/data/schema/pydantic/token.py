# Created by Kelvin_Clark on 1/31/2022, 12:42 PM
from pydantic import BaseModel


class TokenData(BaseModel):
    username: str
    user_id: int
