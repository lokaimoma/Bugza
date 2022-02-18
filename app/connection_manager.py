# Created by Kelvin_Clark on 2/17/2022, 3:07 PM
from typing import List

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect


class ConnectionManager:
    active_connections: dict[str, List[WebSocket]] = {}

    def __init__(self):
        pass

    async def connect(self, channel: str, web_socket: WebSocket):
        await web_socket.accept()
        self.active_connections[channel] = self.active_connections.get(channel, []).append(web_socket)

    async def disconnect(self, channel: str, web_socket: WebSocket):
        for socket in self.active_connections.get(channel, []):
            if socket.client.port == web_socket.client.port:
                self.active_connections[channel].remove(web_socket)

    async def broadcast_to_channel(self, channel: str, json_data: dict):
        for web_socket in self.active_connections.get(channel, []):
            try:
                await web_socket.send(json_data)
            except WebSocketDisconnect:
                await self.disconnect(channel=channel, web_socket=web_socket)


connection_manager = ConnectionManager()
