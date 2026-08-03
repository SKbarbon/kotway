from ..models.controldefaultkwargs import ControlDefaultKwargs, Unpack
from .control import Control, ElementPropType


class Text (Control):
    def __init__(self, content:str, *args, **kwargs: Unpack[ControlDefaultKwargs]):
        super().__init__(*args, **kwargs)
        self.content = content

    @property
    def content (self) -> str:
        return self._get_prop_value(ElementPropType.PROP, "textContent")

    @content.setter
    def content (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "textContent", value)