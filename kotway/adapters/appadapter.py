from ..models import EventCore, ClientEvent, ClientEventType, InteractionEvent
from ..models.events.client_events.clientpageevent import ClientPageEvent
from ..page import Page
import traceback

class AppAdapter:
    """
AppAdapter allows the app to interact with events though API. For example, the default adapter is a server.
    """
    def __init__(self):
        self.__port = None
        self.__webapp_path = None
        self.app_class = None
        self.debug: bool = True

    def start (self):
        """Start the adapter.
        
        Subclasses OVERRIDE this."""
        pass

    # Events
    def create_session (self, requested_route: str) -> str:
        return self.app_class.start_new_page_session(requested_route=requested_route).session_id


    def on_client_event (self, e: ClientEvent):
        """Handle events sent by the client."""
        try: self.__on_client_event(e)
        except Exception:
            traceback.print_exc()

    def __on_client_event (self, e: ClientEvent):
        """The worker for handling client events."""
        # When event is pong.
        if e.event_type == ClientEventType.PONG:
            self.on_client_pong(session_id=e.sessionId)
            return

        # Handle other event types
        page: Page = self.app_class.get_page_by_sessionid(e.sessionId)
        if page == None: return

        if e.event_type == ClientEventType.INTERACTION:
            page.fire_interaction_event(InteractionEvent(**e.event_data))

        elif e.event_type == ClientEventType.CLIENT_PAGE:
            page._handle_client_page_event(ev=ClientPageEvent(**e.event_data))

    def on_client_pong (self, session_id: str):
        """When a client responed for a Ping event. Override by custom adapters."""

    def fetch_session_events (self, session_id: str):
        """The adapter calls this in a loop to check for new events."""
        page: Page = self.app_class.get_page_by_sessionid(session_id)
        if page != None:
            return page.fetch_events_clean()
        else:
            return []


    def on_client_session_end (self, session_id):
        """Do cleanup after a session is done"""
        self.app_class.remove_page_session(session_id)

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