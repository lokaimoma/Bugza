# Created by Kelvin_Clark on 2/1/2022, 1:40 PM
from sqlalchemy.orm import Session

from app.data.entities.project import Project
from app.data.schema.pydantic.project import ProjectIn


def insert_project(session: Session, project: ProjectIn) -> Project:
    project = Project(name=project.name, description=project.description)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project
