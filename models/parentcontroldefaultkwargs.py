from ..controls.control import Control
from typing import TypedDict, Unpack

from ..models.properties.displaytype import DisplayType
from ..models.properties.flexdirection import FlexDirection
from ..models.properties.alignment import Alignment
from ..custom_collections.flex import Flex
from .controldefaultkwargs import ControlDefaultKwargs

class ParentControlDefaultKwargs(TypedDict):
    controls: list[Control]
    display: DisplayType
    flex_direction: FlexDirection
    place_items: Alignment
    justify_content: Alignment
    align_items: Alignment
    flex: Flex

# Inherit from both TypedDict classes
class CombinedControlKwargs(ControlDefaultKwargs, ParentControlDefaultKwargs):
    pass