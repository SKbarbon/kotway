from ..controls.control import Control
from typing import TypedDict, Unpack

from .controldefaultkwargs import ControlDefaultKwargs

class ParentControlDefaultKwargs(TypedDict):
    controls: list[Control]


# Inherit from both TypedDict classes
class CombinedControlKwargs(ControlDefaultKwargs, ParentControlDefaultKwargs):
    pass