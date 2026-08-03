from ..properties.elementproptype import ElementPropType
from pydantic import BaseModel
from enum import Enum

class ControlEventName (Enum):
    UPDATE_PROPS = "update_props"
    ADD_CHILD = "add_child"
    REMOVE_CHILD = "remove_child"

class ControlEvent (BaseModel):
    control_uuid: str
    event_name: ControlEventName
    data: dict


class ControlEventDataUpdateProps (BaseModel):
    props: dict[ElementPropType, dict]


class ControlEventDataAddControl (BaseModel):
    """The event data for adding a child control"""
    control_name: str
    control_uuid: str
    props: dict


class ControlEventDataRemoveChild (BaseModel):
    control_uuid: str