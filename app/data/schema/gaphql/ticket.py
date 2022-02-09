# Created by Kelvin_Clark on 2/2/2022, 1:04 AM
from typing import List

import strawberry

from app.data.enum.ticket_state import TicketState
from app.data.enum.ticket_type import TicketType
from app.data.entities.ticket import Ticket as TicketModel
from app.data.schema.gaphql.comment import Comment
from app.data.schema.gaphql.user import User
from app.data.schema.gaphql.project import Project


@strawberry.type
class Ticket:
    id: int
    project_id: int
    creator_id: int
    title: str
    description: str
    type: TicketType
    state: TicketState
    date_created: str

    instance: strawberry.Private[TicketModel]

    @strawberry.field
    def creator(self) -> User:
        return User(user=self.instance.creator)

    @strawberry.field
    def project(self) -> Project:
        return Project(project=self.instance.project)

    @strawberry.field
    def comments(self) -> List[Comment]:
        return [Comment(comment=comment) for comment in self.instance.comments]

    def __init__(self, ticket: TicketModel):
        self.id = ticket.id
        self.project_id = ticket.project_id
        self.creator_id = ticket.creator_id
        self.title = ticket.title
        self.description = ticket.description
        self.type = ticket.type
        self.state = ticket.state
        self.date_created = ticket.date_created.__str__()
        self.instance = ticket
