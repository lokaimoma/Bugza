# Created by Kelvin_Clark on 2/1/2022, 2:16 PM
from app.utils.security.jwt import create_access_token, get_token_data


def test_create_token():
    data = {"payload": "User data"}
    token = create_access_token(data=data)
    assert token is not None


def test_verify_token():
    data = {"payload": "User data"}
    token = create_access_token(data=data)
    token_data = get_token_data(token=token)
    assert token_data is not None
    assert token_data.keys().__contains__("payload")
    assert token_data["payload"] == data["payload"]


def test_tempered_token():
    data = {"payload": "User data"}
    token = create_access_token(data=data)
    token = token[:len(token) - 5]
    token = token.upper()
    token += "helloTempered"
    token_data = get_token_data(token)
    assert token_data is False
