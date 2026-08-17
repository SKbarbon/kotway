from ...models.controldefaultkwargs import ControlDefaultKwargs, Unpack
from .control import Control
from ...models import ElementPropType

class Image (Control):
    def __init__(self, src: str="", alt: str="", *args, **kwargs: Unpack[ControlDefaultKwargs]):
        super().__init__(*args, **kwargs)

        self.src = src
        self.alt = alt

    @property
    def src (self) -> str:
        """The image source path."""
        return self._get_prop_value(ElementPropType.PROP, "src")

    @src.setter
    def src (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "src", value)

    @property
    def alt (self) -> str:
        """A textual description added to an image element that displays or reads aloud when the image cannot be seen."""
        self._get_prop_value(ElementPropType.PROP, "alt")

    @alt.setter
    def alt (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "alt", value)