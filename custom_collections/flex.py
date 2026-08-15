from .sizeunit import SizeUnit, UnitType

class Flex (str):
    def __new__(cls, flex_grow: int = 0, flex_shrink:int = 1, flex_basis: SizeUnit = None):
        if flex_basis == None:
            flex_basis = SizeUnit(UnitType.AUTO)
        text = f"{flex_grow} {flex_shrink} {flex_basis}"
        obj = super().__new__(cls, text)
        return obj