# Created by Kelvin_Clark on 2/2/2022, 1:00 AM
import strawberry

from app.data.entities.project import Project as ProjectModel


@strawberry.type
class Project:
    id: int
    name: str
    description: str

    def __init__(self, project: ProjectModel):
        self.id = project.id
        self.name = project.name
        self.description = project.description
