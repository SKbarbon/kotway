from ..models.controldefaultkwargs import ControlDefaultKwargs, Unpack
from .control import Control, ElementPropType
from ..custom_collections.sizeunit import SizeUnit

class Text (Control):
    def __init__(self, content:str, font_size: SizeUnit | int = None, *args, **kwargs: Unpack[ControlDefaultKwargs]):
        super().__init__(*args, **kwargs)

        self.content = content
        self.font_size = font_size

    @property
    def content (self) -> str:
        return self._get_prop_value(ElementPropType.PROP, "textContent")

    @content.setter
    def content (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "textContent", value)