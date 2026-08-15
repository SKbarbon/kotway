from .headelement import HeadElement

class Link (HeadElement):
    """The HTML `<link>` tag placed inside the `<head>` element 
    establishes a connection between the HTML document and an external resource."""
    def __init__(self, ref: str, href: str):
        super().__init__()
        self.ref: str = ref
        self.href: str = href


    @property
    def ref (self):
        return self._get_prop("ref")

    @ref.setter
    def ref (self, value: str):
        self._set_prop("ref", value)

    @property
    def href (self):
        return self._get_prop("href")

    @href.setter
    def href (self, value: str):
        self._set_prop("href", value)