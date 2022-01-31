# Created by Kelvin_Clark on 1/30/2022, 9:52 PM
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

__app: Optional[FastAPI] = None


def create_app() -> FastAPI:
    global __app
    if __app is not None:
        return __app
    __app = FastAPI(title="Bugza", description="Backend System of Bugza - A bug tracking system")
    from app.api.router.auth import router as auth_router
    __app.include_router(auth_router)
    return __app