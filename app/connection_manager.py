# Created by Kelvin_Clark on 2/17/2022, 3:07 PM
from typing import List

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect


class ConnectionManager:
    active_connections: dict = {}

    def __init__(self):
        pass

    async def connect(self, channel: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[channel] = self.active_connections.get(channel, [])
        self.active_connections[channel].append(websocket)

    async def disconnect(self, channel: str, websocket: WebSocket):
        for socket in self.active_connections.get(channel, []):
            if socket.client.port == websocket.client.port:
                self.active_connections[channel].remove(websocket)

    async def broadcast_to_channel(self, channel: str, json_data: dict):
        for web_socket in self.active_connections.get(channel, []):
            try:
                await web_socket.send_json(data=json_data)
            except (WebSocketDisconnect, RuntimeError):
                await self.disconnect(channel=channel, websocket=web_socket)


connection_manager = ConnectionManager()
