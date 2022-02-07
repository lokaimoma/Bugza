# Created by Kelvin_Clark on 1/30/2022, 9:52 PM
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

__app: Optional[FastAPI] = None

origins = [
    "http://localhost:3000",
]


def create_app() -> FastAPI:
    global __app
    if __app is not None:
        return __app
    __app = FastAPI(title="Bugza", description="Backend System of Bugza - A bug tracking system")
    __app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"])
    from app.api.router.auth import router as auth_router
    from app.api.router.project import router as project_router
    from app.api.router.ticket import router as ticket_router
    from app.api.router.graphql import router as graphql_router
    __app.include_router(auth_router)
    __app.include_router(project_router)
    __app.include_router(ticket_router)
    __app.include_router(graphql_router)
    return __app
