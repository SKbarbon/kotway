from ..core.controls.control import Control

class ControlsList (list):
    def __init__(self, on_append, on_remove, on_clear, control_instance = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_appened = on_append
        self.on_remove = on_remove
        self.on_clear = on_clear

        self.control_instance = control_instance
        if control_instance == None:
            self.control_instance = Control

    def append(self, object: Control):
        if not isinstance(object, self.control_instance):
            raise TypeError(f"You can only append a {self.control_instance.__name__} not '{type(object)}'.")

        self.on_appened(object)
        return super().append(object)

    def remove(self, value):
        self.on_remove(value)
        return super().remove(value)

    def clear(self):
        self.on_clear()