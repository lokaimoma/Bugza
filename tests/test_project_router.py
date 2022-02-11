# Created by Kelvin_Clark on 2/1/2022, 1:53 PM
import pytest
from httpx import AsyncClient
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_200_OK

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


@pytest.mark.anyio
async def test_get_all_projects(ticket_user, app):
    user = ticket_user[1]
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        ac.headers = {**ac.headers, "Authorization": f"Bearer {user['token']}"}
        response = await ac.get("/project/")
        json = response.json()
        assert response.status_code == HTTP_200_OK
        assert len(json) > 0
        assert "id" in json[0]
        assert "description" in json[0]
        assert "name" in json[0]


@pytest.mark.anyio
async def test_get_latest(ticket_user, app):
    user = ticket_user[1]
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        ac.headers = {**ac.headers, "Authorization": f"Bearer {user['token']}"}
        response = await ac.get("/project/latest")
        json = response.json()
        assert response.status_code == HTTP_200_OK
        assert len(json) <= 10
        assert "id" in json[0]
        assert "description" in json[0]
        assert "name" in json[0]


@pytest.mark.anyio
async def test_get_project_stats(ticket_user, app):
    user = ticket_user[1]
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        ac.headers = {**ac.headers, "Authorization": f"Bearer {user['token']}"}
        response = await ac.get(f"/project/stats?project_id={ticket_user[0].project_id}")
        json = response.json()
        assert response.status_code == HTTP_200_OK
        assert "open_issues" in json
        assert "open_feature_requests" in json
        assert "closed_tickets" in json
        assert json["open_issues"] == 1


@pytest.mark.anyio
async def test_get_project_summary(ticket_user, app):
    user = ticket_user[1]
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        ac.headers = {**ac.headers, "Authorization": f"Bearer {user['token']}"}
        response = await ac.get("/project/summary")
        json = response.json()
        assert response.status_code == HTTP_200_OK
        assert "total_projects" in json
        assert json["total_projects"] == 1
        assert json["with_issues"] == 1
        assert json["without_issues"] == 0