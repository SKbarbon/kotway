from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...page import Page
from collections.abc import Callable

from ...models import *
from ...custom_collections.sizeunit import SizeUnit, UnitType
from ...custom_collections.color import Color
from ...models.events.controlevent import *
from ...models.properties.linestyle import LineStyle
from ...utils.execute_target import execute_target

import uuid, threading
from enum import Enum

class Control:
    def __init__(self, width: SizeUnit = None, height: SizeUnit = None, object_fit: ObjectFit=None,
                 padding: SizeUnit | int = None, margin: SizeUnit | int = None,
                 background_color: Color = None, border_radius: SizeUnit | int = None,
                 border_style: LineStyle = None, color: Color = None,
                 cursor: Cursor | str = None, overflow: Overflow = None,
                 position: Position = None, top: SizeUnit = None,
                 right: SizeUnit | int = None,
                bottom: SizeUnit | int = None,
                left: SizeUnit | int = None,
                outline_style: LineStyle = None,
                font_size: SizeUnit | int = None,
                text_align: Alignment = None,

                on_click: Callable[[InteractionEvent], None] = None):
        self.__unannounced_events: list[EventCore] = [] # Events to be sent on .update()

        self.page: Page = None
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
        self.object_fit = object_fit
        self.padding = padding
        self.margin = margin
        self.background_color = background_color
        self.border_radius = border_radius
        self.border_style = border_style
        self.color = color
        self.cursor = cursor
        self.overflow = overflow
        self.position = position
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.outline_style = outline_style
        self.font_size = font_size
        self.text_align = text_align

        self.on_click = on_click
    
    def update (self):
        """Push an update event for the control's props."""
        if self.page == None: raise Exception("Control must be added to View first.")

        # Update Props
        update_event = ControlEventDataUpdateProps(
            props=self.current_props
        )
        self._add_control_event(ControlEventName.UPDATE_PROPS, update_event.model_dump())

        # Push unannounced events.
        for ue in self.__unannounced_events.copy():
            self.send_unannounced_event_inevitably(ue)

    # == api utils ==
    def send_unannounced_event_inevitably (self, ue: EventCore):
        """Sends a stored unannounced event, then remove it from the list."""
        self.page.add_event(ue)
        self.__unannounced_events.remove(ue)

    def _get_control_name (self) -> str:
        return str(type(self).__name__)

    def _set_prop_value (self, prop_type: ElementPropType, prop_name: str, value):
        if value == None:
            if prop_name in self.current_props[prop_type]:
                del self.current_props[prop_type][prop_name]
            self._add_control_event(
                event_name=ControlEventName.REMOVE_PROP,
                event_data=ControlEventDataRemoveProp(
                    prop_type=prop_type,
                    prop_name=prop_name
                ).model_dump()
            )
        else:
            self.current_props[prop_type][prop_name] = value

    def _get_prop_value (self, prop_type: ElementPropType, prop_name: str):
        if prop_name not in self.current_props[prop_type]:
            return None
        return self.current_props[prop_type][prop_name]

    def _set_interaction_handler (self, interaction_name: str, handler_function, custom_interaction: bool = False):
        self.interaction_handlers[interaction_name] = handler_function

        if not custom_interaction:
            self._add_control_event(
                event_name=ControlEventName.SET_INTERACTION_EVENT,
                event_data=ControlEventDataSetInteractionEv(
                    interaction_name=interaction_name,
                    active=(True if handler_function != None else False)
                ).model_dump()
            )

    def _get_interaction_handler (self, interaction_name: str):
        return self.interaction_handlers[interaction_name]

    def _execute_trigger (self, trigger_name: str, trigger_data: dict):
        """Fire a control trigger method on the client side."""
        if self.page == None: raise Exception("Control must be added to View first.")
        exec_trigger_event = ControlEventDataExecuteTrigger(
            trigger_name=trigger_name,
            data=trigger_data
        )
        ev = self._add_control_event(ControlEventName.EXECUTE_TRIGGER,
                                event_data=exec_trigger_event.model_dump())
        self.send_unannounced_event_inevitably(ev)

    def _add_control_event (self, event_name: ControlEventName, event_data: dict):
        """Cache a control event to be announced.
        
        Returns the created event model."""
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
        return event

    def _on_client_interaction (self, e: InteractionEvent):
        e.control = self
        iname = e.interaction_name
        if iname in self.interaction_handlers and self.interaction_handlers[iname] != None:
            execute_target(target=self.interaction_handlers[iname], args=[e])

    # == Default props ==

    @property
    def width (self) -> str:
        """The control width number"""
        return self._get_prop_value(ElementPropType.STYLE, "width")

    @width.setter
    def width (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "width", value)

    @property
    def height (self) -> str:
        """The control height number"""
        return self._get_prop_value(ElementPropType.STYLE, "height")

    @height.setter
    def height (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "height", value)

    @property
    def min_height (self) -> str:
        self._get_prop_value(ElementPropType.STYLE, "min-height")

    @min_height.setter
    def min_height (self, value: SizeUnit):
        self._set_prop_value(ElementPropType.STYLE, "min-height", value)

    @property
    def object_fit (self):
        """used to specify how an element should be resized to fit its container."""
        return self._get_prop_value(ElementPropType.STYLE, "object-fit")

    @object_fit.setter
    def object_fit (self, value: ObjectFit):
        self._set_prop_value(ElementPropType.STYLE, "object-fit", value)


    @property
    def padding (self) -> str:
        """CSS padding property is used to generate space around an element's content, inside of any defined borders."""
        return self._get_prop_value(ElementPropType.STYLE, "padding")

    @padding.setter
    def padding (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "padding", value)

    @property
    def border_radius (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "border-radius")

    @border_radius.setter
    def border_radius (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "border-radius", value)

    @property
    def border_width (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "border-width")

    @border_width.setter
    def border_width (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "border-width", value)

    @property
    def border_style (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "border-style")

    @border_style.setter
    def border_style (self, value: LineStyle):
        return self._set_prop_value(ElementPropType.STYLE, "border-style", value)

    @property
    def border_color (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "border-color")

    @border_color.setter
    def border_color (self, value: Color):
        self._set_prop_value(ElementPropType.STYLE, "border-color", value)

    @property
    def outline_style (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "outline-style")

    @outline_style.setter
    def outline_style (self, value: LineStyle):
        self._set_prop_value(ElementPropType.STYLE, "outline-style", value)

    @property
    def background_color (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "background-color")

    @background_color.setter
    def background_color (self, value: Color):
        return self._set_prop_value(ElementPropType.STYLE, "background-color", value)

    @property
    def color (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "color")

    @color.setter
    def color (self, value: Color):
        self._set_prop_value(ElementPropType.STYLE, "color", value)

    @property
    def font_size (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "font-size")

    @font_size.setter
    def font_size (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "font-size", value)

    
    @property
    def margin (self) -> str:
        return self._get_prop_value(ElementPropType.STYLE, "margin")

    @margin.setter
    def margin (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "margin", value)

    @property
    def cursor (self) -> str | Cursor:
        """The visual of the cursor when hovering over the control."""
        return self._get_prop_value(ElementPropType.STYLE, "cursor")

    @cursor.setter
    def cursor (self, value: Cursor | str):
        self._set_prop_value(ElementPropType.STYLE, "cursor", value)

    @property
    def overflow (self):
        return self._get_prop_value(ElementPropType.STYLE, "overflow")

    @overflow.setter
    def overflow (self, value):
        self._set_prop_value(ElementPropType.STYLE, "overflow", value)

    @property
    def position (self):
        return self._get_prop_value(ElementPropType.STYLE, "position")

    @position.setter
    def position (self, value: Position):
        self._set_prop_value(ElementPropType.STYLE, "position", value)


    @property
    def top (self):
        return self._get_prop_value(ElementPropType.STYLE, "top")

    @top.setter
    def top (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "top", value)

    @property
    def right (self):
        return self._get_prop_value(ElementPropType.STYLE, "right")

    @right.setter
    def right (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "right", value)

    @property
    def bottom (self):
        return self._get_prop_value(ElementPropType.STYLE, "bottom")

    @bottom.setter
    def bottom (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "bottom", value)

    @property
    def left (self):
        return self._get_prop_value(ElementPropType.STYLE, "left")

    @left.setter
    def left (self, value: SizeUnit | int):
        if isinstance(value, int):
            value = SizeUnit(UnitType.PX, value)
        self._set_prop_value(ElementPropType.STYLE, "left", value)

    @property
    def text_align (self):
        return self._get_prop_value(ElementPropType.STYLE, "text-align")

    @text_align.setter
    def text_align (self, value: Alignment):
        self._set_prop_value(ElementPropType.STYLE, "text-align", value)

    # EVENT HANDLERS
    @property
    def on_click (self):
        return self._get_interaction_handler("click")

    @on_click.setter
    def on_click (self, value):
        self._set_interaction_handler("click", value)