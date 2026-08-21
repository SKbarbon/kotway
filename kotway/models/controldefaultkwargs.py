from collections.abc import Callable

from ..custom_collections.sizeunit import SizeUnit
from ..models import ObjectFit, InteractionEvent
from ..custom_collections.color import Color
from ..models import *
from typing import TypedDict, Unpack

class ControlDefaultKwargs(TypedDict):
    width: SizeUnit | int
    height: SizeUnit | int
    object_fit: ObjectFit
    padding: SizeUnit | int
    margin: SizeUnit | int
    background_color: Color
    color: Color
    border_radius: SizeUnit | int
    border_style: LineStyle
    border_color: Color
    cursor: Cursor | str
    overflow: Overflow
    position: Position
    top: SizeUnit | int
    right: SizeUnit | int
    bottom: SizeUnit | int
    left: SizeUnit | int
    outline_style: LineStyle
    text_align: Alignment

    on_click: Callable[[InteractionEvent], None]
    on_pointer_enter: Callable[[InteractionEvent], None]
    on_pointer_move: Callable[[InteractionEvent], None]
    on_mouse_leave: Callable[[InteractionEvent], None]
    on_pointer_down: Callable[[InteractionEvent], None]
    on_pointer_up: Callable[[InteractionEvent], None]