from .overlaycontrol import OverlayControl


class AlertBox (OverlayControl):
    """Displays a message with a single OK button. Use this to give information to the user.
    
    IMPORTANT: Alerts are blocking on the client!"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._clear_unannounced_events()

    def show (self, message: str):
        """Show a message on an alert box."""
        self._execute_trigger("show_alert", {"message": str(message)})