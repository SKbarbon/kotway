from .text import Text
from .parentcontrol import ParentControl
from ...models.properties.cursor import Cursor
from ...models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack


class Button (ParentControl):
    """A button element.
    
    ARGS:
        text (str): If not None, it will auto create and add a text element containing the text in the `controls`.
    """
    def __init__(self, text: str = None, cursor: Cursor | str = Cursor.POINTER, *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)

        # self.display = None
        # self.flex_direction = None
        self.cursor = cursor

        if text is not None:
            self.controls.append(Text(str(text)))