# Created by Kelvin_Clark on 1/31/2022, 10:04 AM
from typing import Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.data.entities.user import User
from app.data.enum.roles import Role
from app.utils.security.password_util import hash_password
from app.exception import UserAlreadyExistsException


def insert_user(session: Session, username: str, email: str, password: str, role: Optional[Role]) -> User:
    user_exists = __check_user_exits(session=session, username=username, email=email)
    if user_exists:
        raise UserAlreadyExistsException()
    password_hash = hash_password(password=password)
    new_user = User(username=username, email=email, password=password_hash, role=role)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def __check_user_exits(session: Session, username: str, email) -> bool:
    user = session.query(User).where(or_(User.username == username, User.email == email)).first()
    if user is None:
        return False
    return True
