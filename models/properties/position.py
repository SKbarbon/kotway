from enum import Enum

class Position (Enum):
    STATIC = "static"
    RELATIVE = "relative"
    ABSOLUTE = "absolute"
    FIXED = "fixed"
    STICKY = "sticky"
    INHERIT = "inherit"
    INITIAL = "initial"