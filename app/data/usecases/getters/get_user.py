# Created by Kelvin_Clark on 1/31/2022, 12:59 PM
from typing import Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.data.entities.user import User
from app.utils.security.password_util import verify_password_hash


def get_user_by_username_id(session: Session, username: str, user_id: int) -> Optional[User]:
    return session.query(User).where(and_(User.username == username, User.id == user_id)).first()


def get_user_by_username_password(session: Session, username: str, password: str) -> Optional[User]:
    user = session.query(User).where(User.username == username).first()
    if user is None:
        return None
    if verify_password_hash(password=password, password_hash=user.password):
        return user
    return None
