# Created by Kelvin_Clark on 2/2/2022, 2:05 AM
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.entities.project import Project
from app.utils.constants import ROWS_PER_PAGE


async def get_projects(session: AsyncSession, page_number: int) -> List[Project]:
    query = select(Project).limit(ROWS_PER_PAGE).offset(ROWS_PER_PAGE * page_number)
    result = await session.execute(query)
    return result.scalars().all()


async def get_project_by_id(session: AsyncSession, project_id: int) -> Optional[Project]:
    query = select(Project).where(Project.id == project_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()
