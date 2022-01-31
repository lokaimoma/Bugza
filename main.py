# Created by Kelvin_Clark on 1/31/2022, 3:17 PM
import uvicorn

from app import create_app

app = create_app()

if __name__ == "__main__":
    import os
    from app.utils.constants import MODE_ENV_KEY, PRODUCTION_MODE, DEVELOPMENT_MODE

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=False if os.environ.get(MODE_ENV_KEY, DEVELOPMENT_MODE) == PRODUCTION_MODE else True,
        reload_dirs=[".", "./app"]
    )
