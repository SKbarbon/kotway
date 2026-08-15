from ..models import ElementPropType
from .parentcontrol import ParentControl
from ..models.properties.cursor import Cursor
from ..models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack


class Button (ParentControl):
    """A button"""
    def __init__(self,cursor: Cursor | str = Cursor.POINTER, *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)

        # self.display = None
        # self.flex_direction = None
        self.cursor = cursor