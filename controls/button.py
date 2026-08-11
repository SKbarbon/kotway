from ..models import ElementPropType
from .parentcontrol import ParentControl
from ..models.properties.cursor import Cursor
from ..models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack


class Button (ParentControl):
    """A button"""
    def __init__(self, on_click=None, cursor: Cursor | str = Cursor.POINTER, *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)
        self.on_click = on_click

        # self.display = None
        # self.flex_direction = None
        self.cursor = cursor


    @property
    def on_click (self):
        """The on button click event handler."""
        return self._get_interaction_handler("click")

    @on_click.setter
    def on_click (self, value):
        self._set_interaction_handler("click", value)