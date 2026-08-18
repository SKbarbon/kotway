# Multiple views
In this page I will explain how you can do multiple views in your app.

The `Page` class contains an argument named `views`.

Each view represents a route. The default view represents the index route "/".

## Create and Add
Creating and adding a View is simple and a little similar to adding a Control.

This is an example of adding a new view that represents the route `/v2`
```python
import kotway

def main (page: kotway.Page):
    v2 = kotway.View("/v2")
    page.add_view(v2)

kotway.App(main).run()
```

## Presenting a view
To present a view, you use `page.present_view()` method.

You can either pass the `View` or the route as an arg:
```python
page.present_view(v2)
```

or
```
page.present_view("/v2")
```
Both works.

## Noting
You always get `page.current_view` and `page.current_route` which they do change based on which `View` is currently presented.