# Control
A control means a class that represents an element on the client DOM.
Everything on the DOM is a control. Texts, Buttons, Views, etc.. All are subclasses of a Control.

Everything discussed here is related to all controls.

## Interaction Event
An interaction event is like an announcement from the client of an interaction to a control.

The user clicked a button? That's an interaction event. The client will send an announcement to the app about the interaction.

### Default interaction events
There are a couple of default interactions shared across almost all controls.
- `on_click`: When the user clicks the control.

### Event handler arguments
When you set an event handler to any interaction event, you should expect an argument called `InteractionEvent`.
It`s a class that holds data tied to the event.

`InteractionEvent` has multiple properties:
- `control`: The control of the event.
- `control_uuid`: The control uniqe ID.
- `interaction_name`: The name of the interaction.
- `data`: A raw dictionary that holds data related to the event.

By default, setting an interaction event handler to `None`, removes its listener from the client completly, so an interaction event isn't announced to the app unless it has a handler.

And if an interaction set as `custom_interaction=True`, it means the interaction is custom and doesn't rely on a native js listener for that direct html element. So the client will not get an event to setup the interaction.

## Triggers
A trigger is a command from the app sent to the client to perform something related to a control.

For example, executing `TextField.blur()` on the app sends a trigger command to the client to perform the trigger handler already built on the client side.

So, in other words it can be: A trigger is a method built on the client side to perform something on its control, and can be called from the app.

## Updating properties
### Updating a property
When updating a property, you need to call the controls `.update()` method to push the changes.

Setting any property of any type to `None` will result to an attempt to remove the attr from the element completely.

For example, when updating a text property:
```python
text.content = "New content!"
text.update() # This announce the property change to update it.
text.color = None # This removes the attr `color` completely from the text.
```


### A little description on how properties work
At the backend API level, there are two types of properties, they set under the enum `ElementPropType`:
- ElementPropType.PROP: An html element's attr.
- ElementPropType.STYLE: An html element style attr.

### Custom properties
Sometimes, you might learn that an attr property or a style property does not have a direct property handler. You might like to use the private API to update the prop. For example:

```python
text._set_prop_value(
    kotway.ElementPropType.STYLE,
    prop_name="color",
    value="red"
)
```