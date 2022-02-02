# Created by Kelvin_Clark on 2/2/2022, 2:47 AM
from strawberry.extensions import Extension

from app.utils.constants import DB_SESSION_ASYNC, DB_SESSION_SYNC
from app.data import get_async_session_unmanaged, get_sync_session_unmanaged


class SQLAlchemySessionExtension(Extension):
    async def on_request_start(self):
        self.execution_context.context[DB_SESSION_SYNC] = get_sync_session_unmanaged()
        self.execution_context.context[DB_SESSION_ASYNC] = await get_async_session_unmanaged()

    async def on_request_end(self):
        self.execution_context.context[DB_SESSION_SYNC].close()
        await self.execution_context.context[DB_SESSION_ASYNC].close()
