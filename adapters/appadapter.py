from ..models import EventCore, ClientEvent, ClientEventType, InteractionEvent
from ..page import Page

class AppAdapter:
    """
AppAdapter allows the app to interact with events though API. For example, the default adapter is a server.
    """
    def __init__(self):
        self.__port = None
        self.__webapp_path = None
        self.app_class = None

    def start (self):
        """Start the adapter.
        
        Subclasses OVERRIDE this."""
        pass

    # Events
    def create_session (self, requested_route: str) -> str:
        return self.app_class.start_new_page_session(requested_route=requested_route).session_id

    def send_host_event (self, e: EventCore):
        pass

    def on_client_event (self, e: ClientEvent):
        """Handle events sent by the client."""
        # When event is pong.
        if e.event_type == ClientEventType.PONG:
            self.on_client_pong(session_id=e.sessionId)
            return

        # Handle other event types
        page = self.app_class.get_page_by_sessionid(e.sessionId)
        if page == None: return

        if e.event_type == ClientEventType.INTERACTION:
            page.fire_interaction_event(InteractionEvent(**e.event_data))

    def on_client_pong (self, session_id: str):
        """When a client responed for a Ping event. Override by custom adapters."""

    def fetch_session_events (self, session_id: str):
        """The adapter calls this in a loop to check for new events."""
        page: Page = self.app_class.get_page_by_sessionid(session_id)
        if page != None:
            return page.fetch_events_clean()
        else:
            return []

    # Props
    @property
    def port (self):
        return self.__port

    @port.setter
    def port (self, value: int):
        self.__port = value


    @property
    def webapp_path (self):
        return self.__webapp_path

    @webapp_path.setter
    def webapp_path (self, value: str):
        self.__webapp_path = value