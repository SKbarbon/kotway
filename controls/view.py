from .parentcontrol import ParentControl

from ..models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack


class View (ParentControl):
    """View is the top most container for all other controls."""
    def __init__(self, route: str, *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)
        self.route = route

    @property
    def route (self) -> str:
        return self.__route

    @route.setter
    def route (self, route: str):
        if not route.startswith("/"):
            raise ValueError(f"The view route '{route}' must starts with '/'")
        self.__route = route