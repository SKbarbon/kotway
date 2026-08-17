from pydantic import BaseModel
from enum import Enum


class HeadEventName (Enum):
    ADD_ELEM = "add_elem"
    REMVOVE_ELEM = "remove_elem"
    UPDATE_ELEM = "update_elem"


class HeadEvent (BaseModel):
    event_name: HeadEventName
    data: dict


class HeadEventDataAddElem (BaseModel):
    element_name: str
    element_uuid: str

class HeadEventDataRemElem (BaseModel):
    """The data of removing a head element event."""
    element_uuid: str

class HeadEventDataUpdateElem (BaseModel):
    element_uuid: str
    props: dict