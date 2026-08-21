from ...models.controldefaultkwargs import ControlDefaultKwargs, Unpack
from ...models import InteractionEvent
from .control import Control, ElementPropType
from pydantic import BaseModel

class FieldFocusData (BaseModel):
    state: bool

class TextField (Control):
    def __init__(self, value: str = "", placeholder: str = "", on_change=None, on_submit=None, on_input=None, *args, **kwargs: Unpack[ControlDefaultKwargs]):
        super().__init__(*args, **kwargs)

        self.value = value
        self.placeholder = placeholder

        self.on_change = on_change
        self.on_submit = on_submit
        self.on_input = on_input


    def focus (self):
        """Focus the pointer on the field."""
        self._execute_trigger("focus", FieldFocusData(state=True).model_dump())

    def blur (self):
        """Remove the pointer from the field"""
        self._execute_trigger("focus", FieldFocusData(state=False).model_dump())


    def _on_client_interaction(self, e: InteractionEvent):
        if e.interaction_name == "input":
            self.value = e.data["inputValue"]
        super()._on_client_interaction(e)

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
    def on_input (self):
        """Event handler on new text value change."""
        return self._get_interaction_handler("input")

    @on_input.setter
    def on_input (self, value):
        self._set_interaction_handler("input", value)