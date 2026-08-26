from ..parentcontrol import ParentControl
from .overlaycontrol import OverlayControl

class OverlaysManager (ParentControl):
    """This control is the `page.overlays`, parenting the Overlay Controls."""
    def __init__ (self, page):
        super().__init__()
        self.page = page
        self.uuid = "OVERLAYS_MANAGER"
        self._clear_unannounced_events() # Remove assigning events from __init__.


    def add_control(self, control):
        if not isinstance(control, OverlayControl):
            raise ValueError(f"OverylaysManager can only add an `{OverlayControl.__name__}` not {type(control)}")
        return super().add_control(control)