from ..models import InteractionEvent, ElementPropType, EventCore, EventType, ObjectFit
from ..custom_collections.sizeunit import SizeUnit
from ..models.events.controlevent import ControlEvent, ControlEventName, ControlEventDataUpdateProps

import uuid, threading
from enum import Enum

class Control:
    def __init__(self, width: SizeUnit = None, height: SizeUnit = None, object_fit: ObjectFit=None):
        self.__unannounced_events: list[EventCore] = [] # Events to be sent on .update()

        self.page = None
        self.view = None
        self.parent: Control = None

        self.uuid = str(uuid.uuid4())

        self.current_props: dict[ElementPropType, dict] = {
            ElementPropType.PROP: {},
            ElementPropType.STYLE: {}
        }
        self.interaction_handlers: dict[str, any] = {}

        self.width = width
        self.height = height
    
    def update (self):
        """Push an update event for the control's props."""
        if self.page == None: raise Exception("Control must be added to View first.")

        # Update Props
        update_event = ControlEventDataUpdateProps(
            props=self.current_props
        )
        self._add_control_event(ControlEventName.UPDATE_PROPS, update_event.model_dump())

        # Push unannounced events.
        for ue in self.__unannounced_events:
            self.page.add_event (ue)
        self.__unannounced_events.clear()

    # == api utils ==

    def _get_control_name (self) -> str:
        return str(type(self).__name__)

    def _set_prop_value (self, prop_type: ElementPropType, prop_name: str, value):
        self.current_props[prop_type][prop_name] = value

    def _get_prop_value (self, prop_type: ElementPropType, prop_name: str):
        return self.current_props[prop_type][prop_name]

    def _set_interaction_handler (self, interaction_name: str, handler_function):
        self.interaction_handlers[interaction_name] = handler_function

    def _get_interaction_handler (self, interaction_name: str):
        return self.interaction_handlers[interaction_name]

    def _add_control_event (self, event_name: ControlEventName, event_data: dict):
        """Announce a control event in the page cache."""
        ce = ControlEvent(
            control_uuid=self.uuid,
            event_name=event_name,
            data=event_data
        )
        event = EventCore(
            event_type=EventType.CONTROL_EVENT,
            data=ce.model_dump()
        )
        self.__unannounced_events.append(event)

    def _on_client_interaction (self, e: InteractionEvent):
        e.control = self
        iname = e.interaction_name
        if iname in self.interaction_handlers and self.interaction_handlers[iname] != None:
            threading.Thread(target=self.interaction_handlers[iname],
                             daemon=True, args=[e]).start()

    # Default props
    @property
    def width (self) -> float:
        """The control width number"""
        return self._get_prop_value(ElementPropType.STYLE, "width")

    @width.setter
    def width (self, value: SizeUnit):
        self._set_prop_value(ElementPropType.STYLE, "width", str(value))

    @property
    def height (self) -> float:
        """The control height number"""
        return self._get_prop_value(ElementPropType.STYLE, "height")

    @height.setter
    def height (self, value: SizeUnit):
        self._set_prop_value(ElementPropType.STYLE, "height", str(value))

    @property
    def object_fit (self):
        """used to specify how an element should be resized to fit its container."""
        return self._get_prop_value(ElementPropType.STYLE, "object-fit")

    @object_fit.setter
    def object_fit (self, value: ObjectFit):
        self._set_prop_value(ElementPropType.STYLE, "object-fit", value)