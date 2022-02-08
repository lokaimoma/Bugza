# Created by Kelvin_Clark on 2/1/2022, 1:43 PM
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.api.dependencies.oauth import get_admin_system_user, get_current_user
from app.data import get_sync_session, get_async_session
from app.data.schema.pydantic.project import ProjectOut, ProjectIn, ProjectSummary
from app.data.schema.pydantic.user import UserOut
from app.data.usecases.getters.get_project import get_latest_projects, get_projects_summary, get_projects
from app.data.usecases.insert.insert_project import insert_project

router = APIRouter(prefix="/project", tags=["Projects"])


@router.post("/add", response_model=ProjectOut, status_code=HTTP_201_CREATED)
async def create_project(project: ProjectIn, session: Session = Depends(get_sync_session),
                         _: UserOut = Depends(get_admin_system_user)):
    project = insert_project(session=session, project=project)
    return project


@router.get("/", response_model=List[ProjectOut])
async def get_projects__(page_number: Optional[int] = 0, session: AsyncSession = Depends(get_async_session)):
    projects = await get_projects(session=session, page_number=page_number)
    return projects


@router.get("/latest", response_model=List[ProjectOut])
async def _get_latest_projects(count: Optional[int] = None, _: UserOut = Depends(get_current_user),
                               session: AsyncSession = Depends(get_async_session)):
    projects = await get_latest_projects(session=session, count=count)
    return projects


@router.get("/summary", response_model=ProjectSummary)
async def _get_project_summary(_: UserOut = Depends(get_current_user),
                               session: AsyncSession = Depends(get_async_session)):
    summary = await get_projects_summary(session=session)
    return summary
