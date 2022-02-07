# Created by Kelvin_Clark on 2/2/2022, 2:05 AM
from typing import List, Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.entities.project import Project
from app.data.schema.pydantic.project import ProjectSummary
from app.utils.constants import ROWS_PER_PAGE


async def get_projects(session: AsyncSession, page_number: int) -> List[Project]:
    query = select(Project).limit(ROWS_PER_PAGE).offset(ROWS_PER_PAGE * page_number)
    result = await session.execute(query)
    return result.scalars().all()


async def get_project_by_id(session: AsyncSession, project_id: int) -> Optional[Project]:
    query = select(Project).where(Project.id == project_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_latest_projects(session: AsyncSession, count: Optional[int] = 5) -> List[Project]:
    query = select(Project).limit(count).order_by(Project.id.desc())
    result = await session.execute(query)
    return result.scalars().all()


async def get_projects_summary(session: AsyncSession) -> ProjectSummary:
    query = select(func.count(Project.id))
    project_count = await session.execute(query)
    project_count = project_count.scalar_one()
    from app.data.entities.ticket import Ticket
    query = select(func.count(Project.id)).where(Ticket.project_id == Project.id)
    with_issues = await session.execute(query)
    with_issues = with_issues.scalar_one()
    return ProjectSummary(total_projects=project_count,
                          with_issues=with_issues,
                          without_issues=project_count - with_issues)
