# Created by Kelvin_Clark on 1/31/2022, 12:59 PM
from typing import Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.data.entities.user import User


def get_user_by_username_id(session: Session, username: str, user_id: int) -> Optional[User]:
    return session.query(User).where(and_(User.username == username, User.id == user_id)).first()
