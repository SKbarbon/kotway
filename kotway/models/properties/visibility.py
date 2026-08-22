from enum import Enum


class Visibility (Enum):
    VISIBLE = "visible"
    """The element is fully visible and rendered as normal."""

    HIDDEN = "hidden"
    """Hides the element from view, but the element still occupies its layout space in the document."""