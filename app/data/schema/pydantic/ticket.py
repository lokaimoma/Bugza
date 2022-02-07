# Created by Kelvin_Clark on 2/1/2022, 12:28 PM
from datetime import datetime

from pydantic import BaseModel

from app.data.enum.ticket_state import TicketState
from app.data.enum.ticket_type import TicketType


class TicketIn(BaseModel):
    project_id: int
    creator_id: int
    title: str
    description: str
    type: TicketType

    class Config:
        orm_mode = True


class TicketOut(TicketIn):
    id: int
    state: TicketState
    date_created: datetime


class TicketSummary(BaseModel):
    total_tickets: int = 0
    closed: int = 0
    open: int = 0
    feature_request: int = 0
    issues: int = 0


