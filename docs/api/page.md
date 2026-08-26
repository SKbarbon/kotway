# Page
A page is the container that represents a client's session and all its views and content.

## Methods
### `update`
Update the Page and all its views.

### `add_view (View)`
Add a view to the `views` list, then call the view's update.

Optional params:
- `manage_duplicates: bool`: If `True`, it will remove the old view of same route.

### `get_route_view (route: str)`
Search and get the first found `View` that represents the provided route.

### `present_view (view_route: str | View)`
Route the client to the view.

### `get_control_by_uuid`
Get the first found control with requested UUID.

### `is_route_exist (route: str)`
Checks if a route view exists in this `page.views` list.

### `update_title (title: str)`
Update the page title on the browser.

This is an API method, it modifies the `head.title` content.

### `add (control: Control | OverlayControl)`
Add a control to the current view or to the overlays.

It checks the control type, if it`s a normal UI control:        
- Uses the `current_view.add_control`.

If it's an `OverlayControl`:
- It use `self.overlays.add_control`.

## Event handlers

### `on_route_changed (str)`
Fired when the client changes the route/view to a handled route. Gets a string argument of the route.

### `on_unhandled_route_change (str)`
Fired when the client tries to access a route that has no View. Get a string argument of the route.

### `on_session_end`
Fired when the client ends the session completly.

### `on_disconnect (Page)`
Fired when the adapter classify the client as `disconnected` but the connection is active.

### `on_reconnect (Page)`
Fired when the client connects after being calssified as disconnected.