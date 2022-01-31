# Created by Kelvin_Clark on 1/31/2022, 6:04 PM
import pytest
from httpx import AsyncClient
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST

from app.utils.constants import TEST_BASE_URL


@pytest.mark.anyio
async def test_login_no_user(app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient  # Just to get type hints in ide
        form_data = {"username": "Fake User", "password": "123123"}
        response = await ac.post(url="/auth/login", data=form_data)
        assert response.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.anyio
async def test_user_login_user_already_registered(test_user, app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        form_data = {"username": test_user["username"], "password": "synergy"}
        response = await ac.post(url="/auth/login", data=form_data)
        assert response.status_code == HTTP_200_OK
        json: dict = response.json()
        assert "token" in json
        assert "password" not in json
        assert json["token"] is not None
        assert json["username"] == form_data["username"]


@pytest.mark.anyio
async def test_user_register(app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        form_data = {"username": "alpha3030", "password": "h3ll0M0t0", "email": "alpha@moto.com"}
        response = await ac.post(url="/auth/signUp", data=form_data)
        assert response.status_code == HTTP_201_CREATED
        json: dict = response.json()
        assert json["username"] == "alpha3030"
        assert "password" not in json
        assert "token" in json
        assert "token_type" in json
        assert json["token"] is not None


@pytest.mark.anyio
async def test_user_register_duplicate(test_user, app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        form_data = {"username": "BetaTester", "password": "synergy", "email": "hello@hello.com"}
        response = await ac.post(url="/auth/signUp", data=form_data)
        assert response.status_code == HTTP_400_BAD_REQUEST
