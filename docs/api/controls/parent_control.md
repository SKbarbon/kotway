# ParentControl
The base for any control that can parent other controls.

Inherits: (Control)[control.md]

## Properties
### `controls: list[Control]`
A list of the parent's child controls.

## Methods
### `add_control(control: Control)`
Add a control to the `controls` list, then update.

### `remove_control(control: Control)`
Remove a control from the `controls` list, then update.