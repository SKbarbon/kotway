# Page
A page is the container that represents a client's session and all its views and content.

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