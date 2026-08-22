from .sizeunit import SizeUnit, UnitType
from numbers import Number

def box_values (top: SizeUnit | Number,
             right: SizeUnit | Number,
             bottom: SizeUnit | Number,
             left: SizeUnit | Number):
    """* Formats top, right, bottom, and left numeric values into a CSS shorthand string following the TRBL (clockwise) rule."""
    top = SizeUnit(UnitType.PX, top) if isinstance(top, Number) else top
    right = SizeUnit(UnitType.PX, right) if isinstance(right, Number) else right
    bottom = SizeUnit(UnitType.PX, bottom) if isinstance(bottom, Number) else bottom
    left = SizeUnit(UnitType.PX, left) if isinstance(left, Number) else left

    return f"{top} {right} {bottom} {left}"