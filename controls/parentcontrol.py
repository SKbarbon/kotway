from ..custom_collections.controlslist import ControlsList
from ..models.controldefaultkwargs import ControlDefaultKwargs, Unpack
from ..models.events.controlevent import *
from ..models import ElementPropType, DisplayType, FlexDirection, Alignment
from .control import Control



class ParentControl (Control):
    def __init__ (self, controls: list[Control] = None, display: DisplayType = DisplayType.FLEX, flex_direction: FlexDirection=FlexDirection.COLUMN,
                  place_items: Alignment = None, *args, **kwargs: Unpack[ControlDefaultKwargs]):
        super().__init__(*args, **kwargs)

        self.controls: list[Control] = ControlsList(
            on_append=self.__setup_control_child,
            on_remove=lambda c: self.__remove_control_child(c)
        )

        if controls != None:
            for added_control in controls:
                self.controls.append(added_control)


    def update (self):
        if self.page == None: raise Exception(f"The {self._get_control_name()} must be added to Page first.")

        # Create add childs events for the childs waiting to be added.
        for control in self.controls:
            if control.page == None:
                control.page = self.page
                self._add_control_event (
                    event_name=ControlEventName.ADD_CHILD,
                    event_data=ControlEventDataAddControl(
                        control_name=control._get_control_name(),
                        control_uuid=control.uuid,
                        props=control.current_props
                    ).model_dump()
                )

        # Update self
        super().update()

        # Update childs.
        for control in self.controls:
            control.update()


    def add_control (self, control: Control):
        """Adds the control to the Parent then calls update."""
        self.controls.append(control)
        self.update()

    def remove_control (self, control: Control):
        """Removes the control from the Parent then calls update."""
        self.controls.remove(control)
        self.update()

    def __setup_control_child (self, control: Control):
        """Sets up and prepare a control to be a child of this control."""
        control.view = self.view
        control.parent = self


    def __remove_control_child (self, control: Control):
        """Completes the removal of the child control from this parent by removing all parent references."""
        control.view = None
        control.parent = None
        control.page = None

        self._add_control_event(
            event_name=ControlEventName.REMOVE_CHILD,
            event_data=ControlEventDataRemoveChild(
                control_uuid=control.uuid
            ).model_dump()
        )


    @property
    def display (self) -> DisplayType:
        """style.display prop."""
        self._get_prop_value(ElementPropType.STYLE, prop_name="display")

    @display.setter
    def display (self, value: DisplayType):
        self._set_prop_value(ElementPropType.STYLE, prop_name="display", value=value)

    @property
    def flex_direction (self) -> FlexDirection:
        """Set the flex direction of the View.
        
        You need to set .display to DisplayType.FLEX to work."""
        self._get_prop_value(ElementPropType.STYLE, prop_name="flex-direction")

    @flex_direction.setter
    def flex_direction (self, value: FlexDirection):
        self._set_prop_value(ElementPropType.STYLE, prop_name="flex-direction", value=value)


    @property
    def place_items (self) -> Alignment:
        return Alignment(self._get_prop_value(ElementPropType.STYLE, "place-items"))

    @place_items.setter
    def place_items (self, value: Alignment):
        self._set_prop_value(ElementPropType.STYLE, "place-items", value)