# Created by Kelvin_Clark on 1/31/2022, 3:41 PM
import asyncio

import pytest
from httpx import AsyncClient

from app.data.entities.project import Project
from app.data.entities.ticket import Ticket
from app.data.entities.user import User
from app.data.enum.roles import Role
from app.data.enum.ticket_state import TicketState
from app.data.enum.ticket_type import TicketType
from app.data.schema.pydantic.user import UserOut
from app.utils.constants import TEST_BASE_URL
from app.utils.security.jwt import create_access_token
from tests.database import init_tables
from app import create_app
from app.data import get_async_session, get_sync_session
from tests.database import get_async_session as get_async_session_, get_sync_session as get_sync_session_


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def app():
    app = create_app()
    app.dependency_overrides[get_async_session] = get_async_session_
    app.dependency_overrides[get_sync_session] = get_sync_session_
    yield app


@pytest.fixture
@pytest.mark.anyio
async def test_user(app) -> dict:
    async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
        ac: AsyncClient
        form_data = {"username": "BetaTester", "password": "synergy", "email": "hello@hello.com"}
        response = await ac.post(url="/auth/signUp", data=form_data)
        return response.json()


@pytest.fixture
def admin_user() -> UserOut:
    user = User(username="admin", email="admin@bugza.com", password="", role=Role.ADMIN)
    session = next(get_sync_session_())
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    token = create_access_token(data={"username": user.username, "user_id": user.id})
    user_out = UserOut(username=user.username, role=user.role, email=user.email, id=user.id,
                       token=token, token_type="Bearer")
    return user_out


@pytest.fixture
def project() -> Project:
    project = Project(name="CTOS", description="Sorry you don't like Watch Dogs. Can't describe it.")
    session = next(get_sync_session_())
    session.add(project)
    session.commit()
    session.refresh(project)
    session.close()
    return project


@pytest.fixture
def ticket_user(project, test_user) -> tuple[Ticket, dict]:
    test_user: dict
    ticket = Ticket(project_id=project.id, creator_id=test_user["id"], title="sample title",
                    description="sample description", ticket_state=TicketState.OPEN, ticket_type=TicketType.ISSUE)
    session = next(get_sync_session_())
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    session.close()
    return ticket, test_user
