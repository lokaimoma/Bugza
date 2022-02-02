# Created by Kelvin_Clark on 1/30/2022, 9:52 PM
import os
from typing import Optional, Generator, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext import declarative
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from app.utils.constants import *

SYNC_DATABASE_URL = os.environ[SYNC_DATABASE_URL_KEY]
ASYNC_DATABASE_URL = os.environ[ASYNC_DATABASE_URL_KEY]

SQLALCHEMY_BASE = declarative.declarative_base()
__sync_engine: Optional[MockConnection] = None
__async_engine: Optional[AsyncEngine] = None
__sync_session_maker: Optional[sessionmaker] = None
__async_session_maker: Optional[sessionmaker] = None


def __create_sync_engine():
    global __sync_engine
    if __sync_engine is not None:
        return
    __sync_engine = create_engine(url=SYNC_DATABASE_URL, echo=False)
    import app.data.entities.__all_entities__
    global SQLALCHEMY_BASE
    SQLALCHEMY_BASE.metadata.create_all(__sync_engine)


async def __create_async_engine():
    global __async_engine
    if __async_engine is not None:
        return
    __async_engine = create_async_engine(url=ASYNC_DATABASE_URL, echo=False)
    import app.data.entities.__all_entities__
    global SQLALCHEMY_BASE
    async with __async_engine.begin() as conn:
        await conn.run_sync(SQLALCHEMY_BASE.metadata.create_all)


def get_sync_session() -> Generator[Session, None, None]:
    global __sync_engine
    global __sync_session_maker
    if __sync_engine is None:
        __create_sync_engine()
    if __sync_session_maker is None:
        __sync_session_maker = sessionmaker(bind=__sync_engine, expire_on_commit=False)
    session = __sync_session_maker()
    try:
        yield session
    finally:
        session.close()


def get_sync_session_unmanaged() -> Session:
    """
    Returns a synchronous SQLAlchemy session. Users
    of this function have to close the session manually.
    :return: Session
    """
    global __sync_engine
    global __sync_session_maker
    if __sync_engine is None:
        __create_sync_engine()
    if __sync_session_maker is None:
        __sync_session_maker = sessionmaker(bind=__sync_engine, expire_on_commit=False)
    return __sync_session_maker()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    global __async_engine
    global __async_session_maker
    if __async_engine is None:
        await __create_async_engine()
    if __async_session_maker is None:
        __async_session_maker = sessionmaker(bind=__async_engine, class_=AsyncSession, expire_on_commit=False)
    session = __async_session_maker()
    try:
        yield session
    finally:
        await session.close()


def get_async_session_unmanaged() -> AsyncSession:
    """
        Returns am asynchronous SQLAlchemy session. Users
        of this function have to close the session manually.
        Remember to await the call for close on the session.
        :return: AsyncSession
        """
    global __async_engine
    global __async_session_maker
    if __async_engine is None:
        await __create_async_engine()
    if __async_session_maker is None:
        __async_session_maker = sessionmaker(bind=__async_engine, class_=AsyncSession, expire_on_commit=False)
    return __async_session_maker()
