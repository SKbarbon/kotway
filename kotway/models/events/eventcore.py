from pydantic import BaseModel, Field
from enum import Enum
import uuid, time

class EventType (Enum):
    PAGE_EVENT = "page_event"
    CONTROL_EVENT = "control_event"
    PING_EVENT = "ping_event"
    """Can be used by custom adapters to ask for a ping from the client."""

class EventCore (BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_time: int = Field(default_factory=lambda: int(time.time() * 1000))
    event_type: EventType
    data: dict