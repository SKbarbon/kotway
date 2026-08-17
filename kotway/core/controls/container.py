from .parentcontrol import ParentControl
from ...models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack


class Container (ParentControl):
    def __init__(self,  *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)