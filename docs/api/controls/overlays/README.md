# Overlays
An overlay control is a `Control` whose client representation exists outside normal View/parent layout composition.

How to add an overlay control?
You either use the `page.add` which going to know that it is an Overlay control. 
Or use the manual way by doing `page.overlays.add_control`.