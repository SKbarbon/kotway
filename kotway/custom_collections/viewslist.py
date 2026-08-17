from ..core.controls.view import View

class ViewsList (list):
    def __init__(self, on_remove, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_remove = on_remove

    def append(self, object: View):
        if not isinstance(object, View):
            raise TypeError(f"You can only append a View not '{type(object)}'.")

        return super().append(object)

    def remove(self, value):
        self.on_remove(value)
        return super().remove(value)