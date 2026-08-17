

class Color:
    @classmethod
    def hex (self, code: str):
        if code.startswith("#"): return code
        else: return f"#{code}"

    @classmethod
    def rgb (self, red: int, green: int, blue: int, transparency: float = 1):
        """RGB color (red, green, blue, transparency). 
        As if transparency is 1 means fully visible."""
        return f"rgb({red}, {green}, {blue}, {transparency})"

    @classmethod
    def none (self):
        return "none"