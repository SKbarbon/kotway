# Counter app.
Inspired by the default flutter counter app, here is how you can do the exact same in `kotway`:

## Result
When you run the code, you will get this result:
<img width="680" height="390" alt="kotway_counter_app_example" src="https://github.com/user-attachments/assets/30f3ef74-8278-467b-8779-a0f5d013b53f" />


## Script
```python

from kotway import UnitType, Position
import kotway


def main (page: kotway.Page):
    def plus_one (e):
        counter_label.content = str(int(counter_label.content)+1)
        counter_label.update()
    
    page.update_title("Counter App")

    center_container = kotway.Container(
        place_items=kotway.Alignment.CENTER,
        display=kotway.DisplayType.GRID,
        height=kotway.SizeUnit(kotway.UnitType.VH, 100),
        flex=kotway.Flex(1)
    )
    page.add(center_container)

    contents_container = kotway.Container(
        display=kotway.DisplayType.FLEX,
        flex_direction=kotway.FlexDirection.COLUMN,
        place_items = kotway.Alignment.CENTER,
        controls=[
            kotway.Text(
                "You have pushed the button this many times:"
            )
        ]
    )
    center_container.add_control(contents_container)


    counter_label = kotway.Text(
        "0", font_size=30
    )
    contents_container.controls.append(counter_label)

    counter_btn = kotway.Button(
        controls=[
            kotway.Text("+", font_size=20, color="white")
        ], 
        padding=0, 
        background_color=kotway.Color.hex("#2196F3"), 
        color="white",
        border_radius=kotway.SizeUnit(UnitType.PERCENT, 50), 
        position=kotway.Position.FIXED,
        bottom=20, right=20, width=50, height=50, display=kotway.DisplayType.GRID,
        place_items=kotway.Alignment.CENTER,
        on_click=plus_one
    )
    counter_btn._set_prop_value(kotway.ElementPropType.STYLE, "z-index", 999)
    page.add(counter_btn)

kotway.App(target=main).run()
```
