# Created by Kelvin_Clark on 2/2/2022, 1:04 AM
from typing import List, Optional

import strawberry
from strawberry.types import Info

from app.data.entities.ticket import Ticket as TicketModel
from app.data.schema.gaphql.user import User
from app.data.schema.gaphql.project import Project
from app.data.usecases.getters.get_user import get_user_by_id
from app.utils.constants import DB_SESSION_SYNC


@strawberry.type
class Ticket:
    id: int
    project_id: int
    creator_id: int
    title: str
    description: str
    type: str
    state: str
    date_created: str

    @strawberry.field
    def creator(self, info: Info) -> Optional[User]:
        user = get_user_by_id(session=info.context[DB_SESSION_SYNC], user_id=self.creator_id)
        if not user:
            return None
        return User(user=user)

    @strawberry.field
    def project(self) -> Project:
        return Project(project=self.instance.project)

    def __init__(self, ticket: TicketModel):
        self.id = ticket.id
        self.project_id = ticket.project_id
        self.creator_id = ticket.creator_id
        self.title = ticket.title
        self.description = ticket.description
        self.type = ticket.type.value
        self.state = ticket.state.value
        self.date_created = ticket.date_created.__str__()
