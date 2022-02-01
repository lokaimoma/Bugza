# Created by Kelvin_Clark on 2/1/2022, 12:50 PM
import pytest
from httpx import AsyncClient
from starlette.status import HTTP_201_CREATED

from app.data.enum.ticket_state import TicketState
from app.data.enum.ticket_type import TicketType
from app.utils.constants import TEST_BASE_URL


@pytest.mark.anyio
async def test_insert_ticket(project, test_user, app):
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        ac.headers.update({"Authorization": f"Bearer {test_user['token']}"})
        ticket = {
            "project_id": project.id,
            "creator_id": test_user["id"],
            "title": "Delete project",
            "description": "This is a terrible project. Delete immediately before we(DEADSEC) hack and delete it",
            "type": TicketType.ISSUE
        }
        response = await ac.post(url="/ticket/create", json=ticket)
        assert response.status_code == HTTP_201_CREATED
        assert "id" in response.json()
        assert response.json()["state"] == TicketState.OPEN
