# Created by Kelvin_Clark on 2/1/2022, 12:53 PM
from pydantic import BaseModel


class ProjectIn(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class ProjectOut(ProjectIn):
    id: int


class ProjectInfo(BaseModel):
    open_issues: int = 0
    open_feature_requests: int = 0
    closed_tickets: int = 0


class ProjectSummary(BaseModel):
    total_projects: int = 0
    with_issues: int = 0
    without_issues: int = 0
