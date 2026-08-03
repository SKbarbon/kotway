from ..controls.view import View

class ViewsList (list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append(self, object: View):
        if not isinstance(object, View):
            raise TypeError(f"You can only append a View not '{type(object)}'.")

        return super().append(object)

    def remove(self, value):
        return super().remove(value)