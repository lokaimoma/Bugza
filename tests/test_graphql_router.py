# Created by Kelvin_Clark on 2/2/2022, 11:32 AM
import pytest
from httpx import AsyncClient
from starlette.status import HTTP_200_OK

from app.utils.constants import TEST_BASE_URL, TEST_GRAPHQL_PATH


@pytest.mark.anyio
async def test_get_all_projects_no_project(graphql_app):
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
            query GET_PROJECTS {
                projects {
                    id
                    name
                    description
                }
            }
        """
        request_body = {
            "query": query,
            "operationName": "GET_PROJECTS",
            "variables": {}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        json = response.json()
        assert "data" in json
        assert "projects" in json["data"]


@pytest.mark.anyio
async def test_get_all_projects(project, graphql_app):
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
                    query GET_PROJECTS {
                        projects {
                            id
                            name
                            description
                        }
                    }
                """
        request_body = {
            "query": query,
            "operationName": "GET_PROJECTS",
            "variables": {}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        assert len(response.json()["data"]["projects"]) == 1
        assert response.json()["data"]["projects"][0]["name"] == project.name


@pytest.mark.anyio
async def test_get_project_by_id_no_project(graphql_app):
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
            query GET_PROJECT($project_id: Int!) {
                project(projectId: $project_id) {
                    id
                    name
                    description
                }
            }
        """
        request_body = {
            "query": query,
            "operationName": "GET_PROJECT",
            "variables": {"project_id": 1}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        json = response.json()
        assert "data" in json
        assert "project" in json["data"]
        assert json["data"]["project"] is None


@pytest.mark.anyio
async def test_get_project_by_id_(project, graphql_app):
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
            query GET_PROJECT($project_id: Int!) {
                project(projectId: $project_id) {
                    id
                    name
                    description
                }
            }
        """
        request_body = {
            "query": query,
            "operationName": "GET_PROJECT",
            "variables": {"project_id": project.id}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        json = response.json()
        assert "data" in json
        assert "project" in json["data"]
        assert json["data"]["project"] is not None
        assert json["data"]["project"]["id"] == project.id


@pytest.mark.anyio
async def test_get_all_tickets_no_ticket(graphql_app):
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
            query GET_TICKETS {
                tickets {
                    id
                    projectId
                    creatorId
                    title
                    description
                    type
                    state
                }
            }
        """
        request_body = {
            "query": query,
            "operationName": "GET_TICKETS",
            "variables": {}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        json = response.json()
        assert "data" in json
        assert "tickets" in json["data"]
        assert len(json["data"]["tickets"]) == 0


@pytest.mark.anyio
async def test_get_all_tickets(ticket_user, graphql_app):
    ticket = ticket_user[0]
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
            query GET_TICKETS {
                tickets {
                    id
                    projectId
                    creatorId
                    title
                    description
                    type
                    state
                }
            }
        """
        request_body = {
            "query": query,
            "operationName": "GET_TICKETS",
            "variables": {}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        json = response.json()
        assert "data" in json
        assert "tickets" in json["data"]
        assert len(json["data"]["tickets"]) == 1
        assert json["data"]["tickets"][0]["id"] == ticket.id


@pytest.mark.anyio
async def test_get_ticket_by_id_no_ticket(graphql_app):
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
            query GET_TICKET($ticket_id: Int!) {
                ticket(ticketId: $ticket_id) {
                    id
                    projectId
                    creatorId
                    title
                    description
                    type
                    state
                }
            }
        """
        request_body = {
            "query": query,
            "operationName": "GET_TICKET",
            "variables": {"ticket_id": 1}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        json = response.json()
        assert "data" in json
        assert "ticket" in json["data"]
        assert json["data"]["ticket"] is None


@pytest.mark.anyio
async def test_get_ticket_by_id(ticket_user, graphql_app):
    ticket = ticket_user[0]
    async with AsyncClient(app=graphql_app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        query = """
            query GET_TICKET($ticket_id: Int!) {
                ticket(ticketId: $ticket_id) {
                    id
                    projectId
                    creatorId
                    title
                    description
                    type
                    state
                }
            }
        """
        request_body = {
            "query": query,
            "operationName": "GET_TICKET",
            "variables": {"ticket_id": ticket.id}
        }
        response = await ac.post(url=TEST_GRAPHQL_PATH, json=request_body)
        assert response.status_code == HTTP_200_OK
        json = response.json()
        assert "data" in json
        assert "ticket" in json["data"]
        assert json["data"]["ticket"] is not None
        assert json["data"]["ticket"]["id"] == ticket.id
