# Created by Kelvin_Clark on 2/2/2022, 1:34 AM
import strawberry

from app.data.enum.roles import Role
from app.data.entities.user import User as UserModel


@strawberry.type
class User:
    id: int
    username: str
    email: str
    role: Role

    def __init__(self, user: UserModel):
        self.id = user.id
        self.username = user.username
        self.email = user.email
        self.role = user.role
