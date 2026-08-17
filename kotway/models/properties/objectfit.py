from enum import Enum


class ObjectFit (Enum):
    FILL = "fill"
    """Stretches the object to exactly fill the element's box. The aspect ratio is not preserved, so the image can look squished."""

    CONTAIN = "contain"
    """Scales the object to fit entirely inside the box while preserving its aspect ratio. You may get empty space (letterboxing or pillarboxing)."""\

    COVER = "cover"
    """Scales the object to completely cover the box while preserving its aspect ratio. Parts of the object may be cropped."""

    NONE = "none"
    """Doesn't scale the object. It uses its intrinsic size, which may overflow or leave empty space."""

    SCALE_DOWN = "scale-down"
    """Behaves like whichever results in the smaller displayed object between 'none' and 'contain'. It never makes the object larger than its intrinsic size."""
