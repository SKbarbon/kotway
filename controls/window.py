from .control import Control, ElementPropType
from ..models import InteractionEvent
from enum import Enum
import threading

class Window (Control):
    """The page.window property. Represents the window."""
    def __init__(self, page):
        super().__init__()
        self.uuid = "WINDOW"
        self.page = page


    def update(self):
        return


    def _on_client_interaction(self, e: InteractionEvent):
        super()._on_client_interaction(e)

        if e.interaction_name == "resize":
            new_values = e.data["interactionValue"]
            self.width = new_values["width"]
            self.height = new_values["height"]


    def exchange_window_size (self):
        """Fires a trigger to get on_resize event with current window size.."""
        self._execute_trigger("exchange_window_size", {})

    def set_realtime_size_listener (self, state: bool):
        """Start getting realtime interaction events for on_resize when a resize happens"""
        self._execute_trigger("realtime_size_listener", {"state": state})


    @property
    def on_resize (self):
        """Set an event to listen when the window is resized"""
        return self._get_interaction_handler("resize")

    @on_resize.setter
    def on_resize (self, value):
        self._set_interaction_handler("resize", value)