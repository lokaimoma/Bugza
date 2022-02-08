# Created by Kelvin_Clark on 1/31/2022, 12:40 PM
from typing import Union

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status

from app.data import get_sync_session
from app.data.enum.roles import Role
from app.data.schema.pydantic.user import UserOut
from app.data.usecases.getters.get_user import get_user_by_username_id
from app.utils.security.jwt import get_token_data

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_schema), session: Session = Depends(get_sync_session)) -> UserOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data: Union[dict, bool] = get_token_data(token=token)
    if not token_data:
        raise credentials_exception
    user = get_user_by_username_id(session=session, username=token_data["username"], user_id=token_data["user_id"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User no found"
        )
    return user


def get_admin_system_user(current_user: UserOut = Depends(get_current_user)) -> UserOut:
    if (current_user.role == Role.ADMIN) or (current_user.role == Role.SYSTEM_USER):
        return current_user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Account not an admin or system user account"
    )
