from pydantic import BaseModel
from enum import Enum

class ClientEventType (Enum):
    INTERACTION = "interaction"
    CLIENT_PAGE = "client_page"
    PONG = "pong"
    """A responed for ping events."""

class ClientEvent (BaseModel):
    sessionId: str
    event_time: int
    event_type: ClientEventType
    event_data: dict