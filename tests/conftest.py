# Created by Kelvin_Clark on 1/31/2022, 3:41 PM
import asyncio

import pytest
from httpx import AsyncClient

from app.utils.constants import TEST_BASE_URL
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
