# Created by Kelvin_Clark on 1/30/2022, 10:21 PM
import sqlalchemy as sa

from app.data import SQLALCHEMY_BASE
from app.data.enum.ticket_type import TicketType
from app.data.enum.ticket_state import TicketState


class Ticket(SQLALCHEMY_BASE):
    __tablename__ = "tickets"
    id: int = sa.Column(sa.BIGINT().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True)
    project_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("projects.id", ondelete="CASCADE", onupdate="CASCADE"))
    opener_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))
    title: str = sa.Column(sa.String(255), nullable=False)
    description: str = sa.Column(sa.TEXT)
    type: TicketType = sa.Column(sa.Enum(TicketType), nullable=False)
    state: TicketState = sa.Column(sa.Enum(TicketState), nullable=False)

    def __init__(self, project_id: int, opener_id: int, title: str, description: str, ticket_type: TicketType,
                 ticket_state: TicketState):
        self.project_id = project_id
        self.opener_id = opener_id
        self.title = title
        self.description = description
        self.type = ticket_type
        self.state = ticket_state
