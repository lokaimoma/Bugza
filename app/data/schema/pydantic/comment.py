# Created by Kelvin_Clark on 2/1/2022, 10:58 PM
from datetime import datetime

from pydantic import BaseModel


class CommentIn(BaseModel):
    user_id: int
    ticket_id: int
    text: str

    class Config:
        orm_mode = True


class CommentOut(CommentIn):
    id: int
    date_created: datetime


class CommentCount(BaseModel):
    total: int = 0
