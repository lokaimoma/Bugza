# Created by Kelvin_Clark on 2/1/2022, 12:50 PM
import pytest
from httpx import AsyncClient

from app.utils.constants import TEST_BASE_URL


# @pytest.mark.anyio
# async def test_insert_ticket_no_user(app):
#     async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
#         ac: AsyncClient
#         ticket = {
#             "project_id": ,
#             "creator_id": int,
#             "title": str,
#             "description": str,
#             "type": TicketType,
#             "state": TicketState,
#         }
