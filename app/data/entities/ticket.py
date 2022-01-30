# Created by Kelvin_Clark on 1/30/2022, 10:21 PM
import sqlalchemy as sa

from app.data import SQLALCHEMY_BASE
from app.data.enum.ticket_type import TicketType
from app.data.enum.ticket_state import TicketState


class Ticket(SQLALCHEMY_BASE):
    __tablename__ = "tickets"
    project_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("projects.id", ondelete="CASCADE", onupdate="CASCADE"),
                                primary_key=True)
    opener_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
                               primary_key=True)
    title: str = sa.Column(sa.String, nullable=False)
    description: str = sa.Column(sa.TEXT)
    type: TicketType = sa.Column(sa.Enum(TicketType.ISSUE, TicketType.FEATURE_REQUEST), nullable=False)
    state: TicketState = sa.Column(
        sa.Enum(TicketState.OPEN, TicketState.CLOSED, TicketState.FIXED, TicketState.IMPLEMENTED), nullable=False)

    def __init__(self, project_id: int, opener_id: int, title: str, description: str, type: TicketType):
        self.project_id = project_id
        self.opener_id = opener_id
        self.title = title
        self.description = description
        self.type = type
