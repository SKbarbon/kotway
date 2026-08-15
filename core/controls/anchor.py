from .parentcontrol import ParentControl, ElementPropType
from ...models.parentcontroldefaultkwargs import CombinedControlKwargs, Unpack
from ...models.properties.linktarget import LinkTarget

class Anchor (ParentControl):
    """The HTML `<a>` tag, or anchor element, is used to create hyperlinks that connect web pages, files, email addresses, or specific locations on the same page."""
    def __init__ (self, href: str | None = None, 
                  target: LinkTarget | str | None = None,
                  download: str | None = None,
                  *args, **kwargs: Unpack[CombinedControlKwargs]):
        super().__init__(*args, **kwargs)

        self.href = href
        self.target = target
        self.download = download

    @property
    def href (self):
        return self._get_prop_value(ElementPropType.PROP, "href")

    @href.setter
    def href (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "href", value)

    @property
    def target (self):
        """Specifies where to open the linked document."""
        return self._get_prop_value(ElementPropType.PROP, "target")

    @target.setter
    def target (self, value: LinkTarget | str):
        self._set_prop_value(ElementPropType.PROP, "target", value)

    @property
    def download (self):
        """Instructs the browser to download the linked file instead of navigating to it.
        
        The value of this property will be used as the file name of the downloaded content."""
        return self._get_prop_value(ElementPropType.PROP, "download")

    @download.setter
    def download (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "download", value)