# Created by Kelvin_Clark on 1/30/2022, 9:59 PM
from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.data import SQLALCHEMY_BASE
from app.data.entities.ticket import Ticket
from app.data.enum.roles import Role


class User(SQLALCHEMY_BASE):
    __tablename__ = "users"
    id: int = sa.Column(sa.BIGINT().with_variant(type_=sa.Integer, dialect_name="sqlite"), primary_key=True,
                        autoincrement=True)
    username: str = sa.Column(sa.String(length=255), nullable=False, unique=True)
    email: str = sa.Column(sa.String(length=255), nullable=False, unique=True)
    password: str = sa.Column(sa.TEXT, nullable=False)
    role: Role = sa.Column(sa.Enum(Role), default=Role.TESTER)
    tickets: List[Ticket] = relationship("Ticket", backref="creator")

    def __init__(self, username: str, email: str, password: str, role: Role = Role.TESTER):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
