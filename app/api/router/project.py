# Created by Kelvin_Clark on 2/1/2022, 1:43 PM
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.api.dependencies.oauth import get_admin_system_user
from app.data import get_sync_session
from app.data.schema.pydantic.project import ProjectOut, ProjectIn
from app.data.schema.pydantic.user import UserOut
from app.data.usecases.insert.insert_project import insert_project

router = APIRouter(prefix="/project", tags=["Projects"])


@router.post("/add", response_model=ProjectOut, status_code=HTTP_201_CREATED)
async def create_project(project: ProjectIn, session: Session = Depends(get_sync_session),
                         _: UserOut = Depends(get_admin_system_user)):
    project = insert_project(session=session, project=project)
    return project
