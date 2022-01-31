# Created by Kelvin_Clark on 1/31/2022, 6:04 PM
import pytest
from httpx import AsyncClient
from starlette.status import HTTP_401_UNAUTHORIZED

from app.utils.constants import TEST_BASE_URL


@pytest.mark.anyio
async def test_login_no_user(app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        form_data = {"username": "Fake User", "password": "123123"}
        response = await ac.post(url="/auth/login", data=form_data)
        print(response.__dict__)
        assert response.status_code == HTTP_401_UNAUTHORIZED
