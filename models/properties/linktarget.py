from enum import Enum

class LinkTarget (Enum):
    """The `target` attribute options."""

    BLANK = "_blank"
    """Opens the linked document in a new window or tab."""

    SELF = "_self"
    """Opens the linked document in the same frame/tab where it was clicked (default behavior)."""

    PARENT = "_parent"
    """Opens the linked document in the parent frame (used when working with `<iframe>` tags)."""

    TOP = "_top"
    """Opens the linked document in the full body of the window, breaking out of any framing structure."""