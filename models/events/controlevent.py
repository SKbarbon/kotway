from ..properties.elementproptype import ElementPropType
from pydantic import BaseModel
from enum import Enum

class ControlEventName (Enum):
    UPDATE_PROPS = "update_props"
    ADD_CHILD = "add_child"
    REMOVE_CHILD = "remove_child"
    SET_INTERACTION_EVENT = "set_interaction_event"
    EXECUTE_TRIGGER = "execute_trigger"
    REMOVE_PROP = "remove_prop"

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


class ControlEventDataExecuteTrigger (BaseModel):
    trigger_name: str
    data: dict


class ControlEventDataSetInteractionEv (BaseModel):
    interaction_name: str
    active: bool


class ControlEventDataRemoveProp (BaseModel):
    prop_type: str
    prop_name: str