# Head element
A head element (`HeadElement`) represents an html head element. They are not controls, so they do NOT belong to a View as a parent.

A `HeadElement` is a child to the `Head` class (`Page.head`).

## Updating properties
Similar to a `Control`, updating properties work exactly the same way.
```python
HeadElement.some_prop = "new value"
```
But to actually update and push the changes to the client, you call the element's `.update()` method.

## Custom props
If you encounter a property that doesn't have a supported setter, you can still use the private API to set a value to the prop manually.

```python
HeadElement._set_prop("prop_name", "prop_value")
```