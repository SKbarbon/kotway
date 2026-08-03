from pydantic import BaseModel
from enum import Enum

class ClientEventType (Enum):
    INTERACTION = "interaction"

class ClientEvent (BaseModel):
    sessionId: str
    event_time: int
    event_type: ClientEventType
    event_data: dict