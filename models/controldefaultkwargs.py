from ..custom_collections.sizeunit import SizeUnit
from ..models import ObjectFit
from typing import TypedDict, Unpack

class ControlDefaultKwargs(TypedDict):
    width: SizeUnit
    height: SizeUnit
    object_fit: ObjectFit