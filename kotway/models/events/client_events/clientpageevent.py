from pydantic import BaseModel
from enum import Enum

class ClientPageEventName (Enum):
    UNHANDLED_ROUTE = "unhandled_route"

class ClientPageEvent (BaseModel):
    event_name: ClientPageEventName
    data: dict


class ClientPageEventUnhandeldRoute (BaseModel):
    route: str