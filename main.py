# Created by Kelvin_Clark on 1/31/2022, 3:17 PM
import asyncio

import uvicorn
from fastapi import Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette.websockets import WebSocket, WebSocketDisconnect

from app import create_app
from app.connection_manager import connection_manager
from app.data import get_sync_session
from app.data.schema.pydantic.comment import CommentIn, CommentOut
from app.data.usecases.insert.insert_comment import insert_comment

app = create_app()


@app.websocket(path="/ws/comment")
async def _ticket_comment_ws_route(websocket: WebSocket, channel: str, session: Session = Depends(get_sync_session)):
    await connection_manager.connect(channel=channel, websocket=websocket)
    try:
        while True:
            payload = await websocket.receive_json()
            comment_data = CommentIn(**payload)
            comment = insert_comment(comment=comment_data, session=session)
            asyncio.ensure_future(
                connection_manager.broadcast_to_channel(f"ticket_{comment.ticket_id}_comments_channel",
                                                        CommentOut(**comment.__dict__).json())
            )
    except WebSocketDisconnect:
        await connection_manager.disconnect(channel=channel, websocket=websocket)
    except (TypeError, ValidationError):
        await websocket.send_json({"error": "Invalid comment payload. Check CommentIn schema."})


if __name__ == "__main__":
    import os
    from app.utils.constants import MODE_ENV_KEY, PRODUCTION_MODE, DEVELOPMENT_MODE

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=False if os.environ.get(MODE_ENV_KEY, DEVELOPMENT_MODE) == PRODUCTION_MODE else True,
        reload_dirs=[".", "./app"]
    )
