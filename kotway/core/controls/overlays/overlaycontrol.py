from ..control import Control, InteractionEvent


class OverlayControl (Control):
    """An overlay control is a `Control` whose client representation exists outside normal View/parent layout composition."""
    def __init__ (self):
        super().__init__()