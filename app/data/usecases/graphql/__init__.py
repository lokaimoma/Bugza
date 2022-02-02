# Created by Kelvin_Clark on 2/2/2022, 2:27 AM
# resolvers
from typing import List, Optional

from strawberry.types import Info

from app.data.usecases.getters.get_project import get_projects, get_project_by_id
from app.data.usecases.getters.get_ticket import get_tickets, get_ticket_by_id
from app.data.schema.gaphql.project import Project
from app.data.schema.gaphql.ticket import Ticket
from app.utils.constants import DB_SESSION_ASYNC


async def get_projects_resolver(info: Info, page_number: Optional[int] = 1) -> List[Project]:
    projects = await get_projects(page_number=page_number, session=info.context[DB_SESSION_ASYNC])
    return [Project(project=project) for project in projects]


async def get_project_by_id_resolver(project_id: int, info: Info) -> Optional[Project]:
    project = await get_project_by_id(project_id=project_id, session=info.context[DB_SESSION_ASYNC])
    if project is None:
        return None
    return Project(project=project)


async def get_tickets_resolver(info: Info, page_number: Optional[int] = 1) -> List[Ticket]:
    tickets = await get_tickets(session=info.context[DB_SESSION_ASYNC], page_number=page_number)
    return [Ticket(ticket=ticket) for ticket in tickets]
