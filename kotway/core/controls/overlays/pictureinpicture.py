from .overlaycontrol import OverlayControl, InteractionEvent
from ..parentcontrol import ParentControl
from collections.abc import Callable

from ....models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack


class PictureInPicture (ParentControl, OverlayControl):
    """A way to open a small, always-on-top floating window filled with custom controls and interactive elements."""
    def __init__ (self, on_present_change: Callable[[InteractionEvent], None]=None, *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)
        self._clear_unannounced_events()

        self.__is_presented: bool = False
        self.on_present_change = on_present_change

    def _on_client_interaction(self, e):
        if (e.interaction_name == "isPresented"):
            state = e.data["state"]
            self.__is_presented = state
        return super()._on_client_interaction(e)

    def request_window (self, width: int, height: int):
        """Request an always-on-top PIP window."""
        self._execute_trigger("request_window", trigger_data={"width": int(width), "height": int(height)})

    def close (self):
        """Close the PIP windows."""
        self._execute_trigger("close", trigger_data={})

    @property
    def is_presented (self) -> bool:
        """A read-only property that checks if the PIP is already presented."""
        return self.__is_presented

    @property
    def on_present_change (self):
        return self._get_interaction_handler("isPresented")

    @on_present_change.setter
    def on_present_change (self, value: Callable[[InteractionEvent], None]):
        self._set_interaction_handler("isPresented", value, custom_interaction=True)