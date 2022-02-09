# Created by Kelvin_Clark on 2/2/2022, 2:58 AM
from typing import List, Optional

import strawberry

from app.data.schema.gaphql.project import Project
from app.data.schema.gaphql.comment import Comment
from app.data.schema.gaphql.ticket import Ticket
from app.data.usecases.graphql import (
    get_projects_resolver,
    get_project_by_id_resolver,
    get_tickets_resolver,
    get_ticket_by_id_resolver,
    get_comments_by_ticket_id_resolver,
    get_tickets_by_project_id_
)


@strawberry.type
class Query:
    projects: List[Project] = strawberry.field(resolver=get_projects_resolver)
    project: Optional[Project] = strawberry.field(resolver=get_project_by_id_resolver)
    tickets: List[Ticket] = strawberry.field(resolver=get_tickets_resolver)
    tickets_by_project_id: List[Ticket] = strawberry.field(resolver=get_tickets_by_project_id_)
    ticket: Optional[Ticket] = strawberry.field(resolver=get_ticket_by_id_resolver)
    comments: List[Comment] = strawberry.field(resolver=get_comments_by_ticket_id_resolver)
