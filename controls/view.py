from .parentcontrol import ParentControl

from ..models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack


class View (ParentControl):
    """View is the top most container for all other controls."""
    def __init__(self, route: str, *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)
        self.route: str = route