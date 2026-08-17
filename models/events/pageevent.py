from pydantic import BaseModel
from enum import Enum

class PageEventName (Enum):
    ADD_VIEW = "add_view"
    PRESENT_VIEW = "present_view"
    REMOVE_VIEW = "remove_view"
    HEAD_EVENT = "head_event"

class PageEvent (BaseModel):
    event_name: PageEventName
    data: dict


class PageEventDefineView (BaseModel):
    view_route: str
    view_uuid: str

class PageEventPresentView (BaseModel):
    view_route: str