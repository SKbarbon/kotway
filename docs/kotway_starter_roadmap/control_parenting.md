# Learn about Control Parenting
Control parenting is very important in any UI building tool.

## What is parenting a control?
Parenting a control is making a control lives inside another control.

### Why is it useful?

Because it allows you to control the layout better, make rows or columns, or just stack a bunch of controls to stick together.

And here is the thing, if you built a `kotway` app, you already DID parent a control!

In `kotway`, a Page has something called `views`. And a `View` is the most top-level parent you can have.

By default, a Page do create an index `View`, and when you used `page.add(Text)` you basically added that text to the View!

Meaning, you made the `View` a parent of that `Text` 😱!!!

### Let's make a control that can parent other controls.
A button. A `Button` is a parent control!
```python
import kotway

def main (page: kotway.Page):
    btn = kotway.Button(controls=[
        kotway.Text("Click me!")
    ])
    page.add(btn)

kotway.App(main).run()
```

See, just like that you made a button, and gave it a kid!

You can also do that dynamically like:
```python
import kotway

def main (page: kotway.Page):
    btn = kotway.Button()
    page.add(btn)

    btn.add_control(kotway.Text("Click me!"))

kotway.App(main).run()
```

## You are the master now 😎!