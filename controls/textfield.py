from ..models.controldefaultkwargs import ControlDefaultKwargs, Unpack
from ..models import InteractionEvent
from .control import Control, ElementPropType


class TextField (Control):
    def __init__(self, value: str = "", placeholder: str = "", on_change=None, on_submit=None, on_input=None, *args, **kwargs: Unpack[ControlDefaultKwargs]):
        super().__init__(*args, **kwargs)

        self.value = value
        self.placeholder = placeholder

        self.on_change = on_change
        self.on_submit = on_submit
        self.on_input = on_input


    @property
    def value (self) -> str:
        """The text value of the TextField"""
        return self._get_prop_value(ElementPropType.PROP, "value")

    @value.setter
    def value (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "value", value)

    @property
    def placeholder (self) -> str:
        return self._get_prop_value(ElementPropType.PROP, "placeholder")

    @placeholder.setter
    def placeholder (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "placeholder", value)


    @property
    def on_change (self):
        "Event handler for focus change."
        return self._get_interaction_handler("change")

    @on_change.setter
    def on_change (self, value):
        self._set_interaction_handler("change", value)

    @property
    def on_submit (self):
        """Event handler for submit."""
        return self._get_interaction_handler("submit")

    @on_submit.setter
    def on_submit (self, value):
        self._set_interaction_handler("submit", value)


    @property
    def on_input (self):
        """Event handler on new text value change."""
        return self._get_interaction_handler("input")

    @on_input.setter
    def on_input (self, value):
        self._set_interaction_handler("input", value)

    def _on_client_interaction(self, e: InteractionEvent):
        if e.interaction_name == "input":
            self.value = e.data["interactionValue"]
        super()._on_client_interaction(e)