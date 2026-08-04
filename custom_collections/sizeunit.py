from pydantic import BaseModel
from enum import Enum

class UnitType (Enum):
    """
    The Unit type is used to determine the unit used for size.
    """
    PX = "px"
    """pixel"""

    PT = "pt"
    """Points of an Inch"""

    AUTO = "auto"
    """Compute the size automatically based on normal document flow"""

    REM = "rem"
    """Relative to the root (<html>) element's font size."""

    VW = "vw"
    """Viewport Width"""

    VH = "vh"
    """Viewport Height"""

    PERCENT = "%"
    """Size relative to the parent element's specific property value"""

    FIT_CONTENT = "fit-content"

class SizeUnit (str):
    def __new__(cls, unit_type: UnitType, size: float | None = None):
        text = f"{'' if size is None else size}{unit_type.value}"
        obj = super().__new__(cls, text)
        obj.unit_type = unit_type
        obj.size = size
        return obj