# Created by Kelvin_Clark on 1/30/2022, 10:21 PM
from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.data import SQLALCHEMY_BASE
from app.data.entities.comments import Comment
from app.data.entities.project import Project
from app.data.entities.user import User
from app.data.enum.ticket_type import TicketType
from app.data.enum.ticket_state import TicketState


class Ticket(SQLALCHEMY_BASE):
    __tablename__ = "tickets"
    id: int = sa.Column(sa.BIGINT().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True)
    project_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("projects.id", ondelete="CASCADE", onupdate="CASCADE"))
    creator_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))
    title: str = sa.Column(sa.String(255), nullable=False)
    description: str = sa.Column(sa.TEXT)
    type: TicketType = sa.Column(sa.Enum(TicketType), nullable=False)
    state: TicketState = sa.Column(sa.Enum(TicketState), nullable=False)
    project: Project = relationship("Project", uselist=False)
    creator: User = relationship("User", uselist=False, backref="tickets")
    comments: List[Comment] = relationship("Comment", backref="ticket")

    def __init__(self, project_id: int, creator_id: int, title: str, description: str, ticket_type: TicketType,
                 ticket_state: TicketState):
        self.project_id = project_id
        self.creator_id = creator_id
        self.title = title
        self.description = description
        self.type = ticket_type
        self.state = ticket_state
