# Drawing app 🎨
This is a very simple drawing app (pool-based ink). You will get something like this at the end where you can draw:

<img width="891" height="677" alt="image" src="https://github.com/user-attachments/assets/6e547309-a33a-4af0-b8d5-5251b3fcaaa6" />


## Script
```python

import kotway, time, sys

class DrawApp:
    def __init__(self, page: kotway.Page):
        self.page = page
        self._start_time = time.perf_counter() # Used to help reduce lag on server.
        self.draw_comp_pool = []

        loading_text = kotway.Text("The pool is Loading..")
        page.add(loading_text)

        for _ in range(500):
            com = kotway.Container(
                background_color="black",
                width=20,
                height=20,

                position=kotway.Position.FIXED,
                top=-500
            )
            self.draw_comp_pool.append(com)
            page.add(com)

        page.current_view.remove_control(loading_text)

        page.add(kotway.Container(
            controls=[
                kotway.Text(
                    "Draw something..",
                    color="#C0C0C0"
                )
            ],
            display=kotway.DisplayType.GRID,
            place_items=kotway.Alignment.CENTER,
            height=kotway.SizeUnit(kotway.UnitType.VH, 100)
        ))

        page.current_view.width = kotway.SizeUnit(kotway.UnitType.VW, 100)
        page.current_view.height = kotway.SizeUnit(kotway.UnitType.VH, 100)

        page.current_view.on_pointer_down = lambda e: self.start_drawing()
        page.current_view.on_pointer_up = lambda e: self.stop_drawing()

        page.update()

    def draw_on_pointer(self, e: kotway.InteractionEvent):
        if not self.is_draw_allowed(): 
            return
        
        # 1. Get pointer position
        pool_element: kotway.Container = self.draw_comp_pool[0]
        top_pos = int(e.data["clientY"] - float(kotway.SizeUnit.number(pool_element.height) / 2))
        left_pos = int(e.data["clientX"] - float(kotway.SizeUnit.number(pool_element.width) / 2))

        # 2. Pop the reusable component from the pool (or grab by index)
        # Rotating the pool using pop(0) and append() ensures true Round-Robin usage
        comp = self.draw_comp_pool.pop(0)

        comp.top = top_pos
        comp.left = left_pos

        # 3. Only add to the UI tree IF it hasn't been mounted yet
        if comp.page is None:
            self.page.current_view.add_control(comp)
        else:
            # If it's already mounted, just update position directly
            comp.update()

        # 4. Put the component back at the end of the queue
        self.draw_comp_pool.append(comp)
        

    def start_drawing (self):
        self._start_time = time.perf_counter()
        self.page.current_view.on_pointer_move = self.draw_on_pointer
        self.page.current_view.update()

    def stop_drawing (self):
        self.page.current_view.on_pointer_move = None
        self.page.current_view.update()


    def is_draw_allowed (self):
        if "pyodide" in sys.modules: return True
        if time.perf_counter() - self._start_time < 0.025:
            return False
        else:
            self._start_time = time.perf_counter()
            return True

kotway.App(DrawApp).run(port=8000)
```
