# Created by Kelvin_Clark on 1/30/2022, 10:15 PM
import sqlalchemy as sa

from app.data import SQLALCHEMY_BASE


class Project(SQLALCHEMY_BASE):
    __tablename__ = "projects"
    id: int = sa.Column(sa.BIGINT, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(255), nullable=False)
    description: str = sa.Column(sa.TEXT)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
