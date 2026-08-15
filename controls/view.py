from .parentcontrol import ParentControl

from ..models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack
from ..models import InteractionEvent
from collections.abc import Callable

class View (ParentControl):
    """View is the top most container for all other controls."""
    def __init__(self, route: str, on_presented: Callable[[InteractionEvent], None] = None, 
                 *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)
        self.route = route

        self.on_presented = on_presented


    def _on_client_interaction(self, e: InteractionEvent):
        if e.interaction_name == "presented":
            self.page._client_changed_route(
                route=self.route,
                informative=True
            )
        super()._on_client_interaction(e)

    @property
    def route (self) -> str:
        return self.__route

    @route.setter
    def route (self, route: str):
        if not route.startswith("/"):
            raise ValueError(f"The view route '{route}' must starts with '/'")
        self.__route = route

    @property
    def on_presented (self):
        """An event which fired once the View be presented on the client Page."""
        print("Im called!")
        return self._get_interaction_handler("presented")

    @on_presented.setter
    def on_presented (self, value):
        self._set_interaction_handler("presented", value, custom_interaction=True)