# Created by Kelvin_Clark on 1/31/2022, 12:16 PM
import os
from datetime import datetime, timedelta
from typing import Union

from jose import jwt, JWTError

from app.utils.constants import SECRET_KEY_ENV_KEY

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 3600
SECRET_KEY = os.environ[SECRET_KEY_ENV_KEY]


def create_access_token(data: dict) -> str:
    data_ = data.copy()
    expiry_time = datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    data_.update({"exp": expiry_time})
    token = jwt.encode(data_, key=SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_token_data(token: str) -> Union[dict, bool]:
    """
    Returns the content of a JWT string if the token is valid
    otherwise returns a bool of value False.
    :param token: JWT token string
    :return: Token content if token is valid.
    """
    try:
        return jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return False



