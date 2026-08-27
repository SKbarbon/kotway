from enum import Enum


class UserSelect (Enum):
    AUTO = "auto"
    """Uses the browser's default behavior for the element type 
    (text in `<p>` is selectable, text in `<button>` usually isn't)."""

    NONE = "none"
    """Disables selection entirely for the element and its children."""

    TEXT = "text"
    """Explicitly allows the user to highlight and select text."""

    ALL = "all"
    """Forces an "all-or-nothing" selection. A single click selects the entire element's content instantly."""

    CONTAIN = "contain"
    """Restricts selection boundary. 
    Starting a selection inside the element prevents it from overflowing outside. (Limited browser support)"""