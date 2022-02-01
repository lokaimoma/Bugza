# Created by Kelvin_Clark on 1/31/2022, 3:45 PM
from typing import Generator, AsyncGenerator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext.asyncio import AsyncConnection, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

TEST_DATABASE_URL_SYNC = "sqlite:///./sql_app.db"
TEST_DATABASE_URL_ASYNC = "sqlite+aiosqlite:///./sql_app.db"

__sync_engine: MockConnection = create_engine(url=TEST_DATABASE_URL_SYNC, echo=False,
                                              connect_args={"check_same_thread": False})
__async_engine: AsyncConnection = create_async_engine(url=TEST_DATABASE_URL_ASYNC, echo=False,
                                                      connect_args={"check_same_thread": False})
__sync_session_maker: sessionmaker = sessionmaker(bind=__sync_engine, expire_on_commit=False)
__async_session_maker: sessionmaker = sessionmaker(bind=__async_engine, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(autouse=True)
def init_tables():
    import app.data.entities.__all_entities__
    from app.data import SQLALCHEMY_BASE
    SQLALCHEMY_BASE.metadata.drop_all(bind=__sync_engine)
    SQLALCHEMY_BASE.metadata.create_all(bind=__sync_engine)


def get_sync_session() -> Generator[Session, None, None]:
    session = __sync_session_maker()
    try:
        yield session
    finally:
        session.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    session = __async_session_maker()
    try:
        yield session
    finally:
        await session.close()