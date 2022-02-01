# Created by Kelvin_Clark on 2/1/2022, 1:53 PM
import pytest
from httpx import AsyncClient
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED

from app.utils.constants import TEST_BASE_URL


@pytest.mark.anyio
async def test_insert_project_no_user(app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        project = {"name": "Bloom", "description": "A project to harvest human data."}
        response = await ac.post(url="/project/add", json=project)
        assert response.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.anyio
async def test_insert_project_test_user(test_user, app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        ac.headers = {**ac.headers, "Authorization": f"Bearer {test_user['token']}"}
        project = {"name": "Bloom", "description": "A project to harvest human data."}
        response = await ac.post(url="/project/add", json=project)
        assert response.status_code == HTTP_401_UNAUTHORIZED
        assert response.json()["detail"] == "Account not an admin or system user account"


@pytest.mark.anyio
async def test_insert_project_admin(admin_user, app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        ac.headers = {**ac.headers, "Authorization": f"Bearer {admin_user.token}"}
        project = {"name": "Bloom", "description": "A project to harvest human data."}
        response = await ac.post(url="/project/add", json=project)
        assert response.status_code == HTTP_201_CREATED
        json = response.json()
        assert "id" in json
        assert json["id"] is not None
        assert json["name"] == project["name"]
