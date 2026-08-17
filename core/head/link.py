from .headelement import HeadElement

class Link (HeadElement):
    """The HTML `<link>` tag placed inside the `<head>` element 
    establishes a connection between the HTML document and an external resource.
    
    ARGS:
        `rel` (string): relationship attribute defines how the linked resource connects to the current document.
        `href` (string): hypertext reference attribute specifies the path or URL to that resource.
    """
    def __init__(self, rel: str, href: str):
        super().__init__()
        self.rel: str = rel
        self.href: str = href


    @property
    def rel (self):
        return self._get_prop("rel")

    @rel.setter
    def rel (self, value: str):
        self._set_prop("rel", value)

    @property
    def href (self):
        return self._get_prop("href")

    @href.setter
    def href (self, value: str):
        self._set_prop("href", value)