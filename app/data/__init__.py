# Created by Kelvin_Clark on 1/30/2022, 9:52 PM
import os
from typing import Optional, Generator

from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext import declarative
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from app.utils.constants import *

mode = os.environ[MODE_KEY]
if mode != PROD_MODE or mode != DEV_MODE:
    raise ValueError(f"The mode variable must hold a value of either {PROD_MODE} or {DEV_MODE}")

SYNC_DATABASE_URL = os.environ[DEV_SYNC_DATABASE_KEY] if mode == DEV_MODE else os.environ[PROD_SYNC_DATABASE_KEY]
ASYNC_DATABASE_URL = os.environ[DEV_ASYNC_DATABASE_KEY] if mode == DEV_MODE else os.environ[PROD_ASYNC_DATABASE_KEY]

SQLALCHEMY_BASE = declarative.declarative_base()
__sync_engine: Optional[MockConnection]
__async_engine: Optional[AsyncEngine]
__sync_session_maker: Optional[sessionmaker]
__async_session_maker: Optional[sessionmaker]


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


async def get_async_session() -> Generator[AsyncSession, None, None]:
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
