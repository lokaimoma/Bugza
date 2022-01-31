# Created by Kelvin_Clark on 1/31/2022, 1:20 PM
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm

from app.data import get_sync_session
from app.data.enum.roles import Role
from app.data.schema.pydantic.token import TokenData
from app.data.schema.pydantic.user import UserOut
from app.data.usecases.getters.get_user import get_user_by_username_password
from app.data.usecases.insert.insert_user import insert_user
from app.exception import UserAlreadyExistsException
from app.utils.security.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(path="/login", status_code=HTTP_200_OK, response_model=UserOut)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_sync_session)):
    user = get_user_by_username_password(session=session, username=form_data.username, password=form_data.password)
    if user is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="User doesn't exist or wrong credentials provided"
        )
    token_data = TokenData(username=user.username, user_id=user.id).dict()
    token_string = create_access_token(data=token_data)
    return UserOut(**user.__dict__, token=token_string, token_type="Bearer")


@router.post(path="/signUp", status_code=HTTP_201_CREATED, response_model=UserOut)
def sign_up_test_user(username: str = Form(...), password: str = Form(...), email: str = Form(...),
                      session: Session = Depends(get_sync_session)):
    try:
        user = insert_user(session=session, username=username, email=email, password=password, role=Role.TESTER)
        token_data = TokenData(username=user.username, user_id=user.id).dict()
        token_string = create_access_token(data=token_data)
        return UserOut(**user.__dict__, token=token_string, token_type="Bearer")
    except UserAlreadyExistsException as e:
        raise HTTPException(
            detail=e.message,
            status_code=HTTP_400_BAD_REQUEST
        )
