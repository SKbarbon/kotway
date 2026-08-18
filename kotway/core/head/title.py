from .headelement import HeadElement

class Title (HeadElement):
    """The HTML `<title>` tag placed inside the `<head>` element
    that defines the text-based name of a web page.
    
    ARGS:
        `rel` (string): relationship attribute defines how the linked resource connects to the current document.
        `href` (string): hypertext reference attribute specifies the path or URL to that resource.
    """
    def __init__(self, content: str):
        super().__init__()

    @property
    def content (self) -> str:
        return self._get_prop("textContent")

    @content.setter
    def content (self, value: str):
        self._set_prop("textContent", value)