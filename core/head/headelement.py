import uuid

class HeadElement:
    """Core class for head elements."""
    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self._props: dict[str, any] = {}


    def update (self):
        pass

    def _set_prop (self, prop_name: str, value: any):
        self._props[prop_name] = value

    def _get_prop (self, prop_name: str):
        if prop_name in self._props:
            return self._props[prop_name]