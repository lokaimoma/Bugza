# Created by Kelvin_Clark on 2/2/2022, 2:27 AM
# resolvers
from typing import List, Optional

from strawberry.types import Info

from app.data.usecases.getters.get_project import get_projects
from app.data.schema.gaphql.project import Project
from app.utils.constants import DB_SESSION_ASYNC


async def get_projects_resolver(info: Info, page_number: Optional[int] = 1) -> List[Project]:
    projects = await get_projects(page_number=page_number, session=info.context[DB_SESSION_ASYNC])
    return [Project(project=project) for project in projects]


