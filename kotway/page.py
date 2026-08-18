from .models import EventCore, EventType, InteractionEvent
from .models.events.pageevent import *
from .models.events.client_events.clientpageevent import *

from .core.controls.window import Window
from .core.controls import Control, View
from .core.head.head import Head

from .custom_collections.viewslist import ViewsList

from collections.abc import Callable

from .utils.execute_target import execute_target
from .utils.find_control_by_uuid import find_control_by_uuid
import threading

class Page:
    """
A Page is a session and views container.
    """
    def __init__(self, session_id: str):
        self.__session_id: str = session_id
        self.__next_events: list[EventCore] = []

        self.head = Head(page=self)
        self.window = Window(page=self)

        self.views: list[View] = ViewsList(
            on_remove=self.__remove_view
        )
        self.views.append(View("/"))

        self.__current_route: str = "/"

        # Events
        self.__adapter_hook_on_add_event = None
        self.on_unhandled_route_change: Callable[[str], None] = None
        """When the client goes to a route that has no view."""

        self.on_session_end: Callable[[], None] = None
        """When the client is already out and disconnected."""

        self.update()
        self.present_view("/")
        
        self.head.title.update()

    # utils
    def update (self):
        """Update the Page and its views."""
        # Make sure Views have the Page reference and registered.
        for v in self.views:
            if v.page == None:
                self.add_view(
                    view=v,
                    manage_duplicates=False
                )

        for v in self.views:
            v.update()

        
    def add_view (self, view: View, manage_duplicates: bool = True):
        """Adds a View to the views list. Manages the duplicate issue (removes the old view of same route)
        and register the event."""
        # Manage duplicates.
        if self.is_route_exist(view.route):
            if manage_duplicates == False: raise Exception(f"Found duplicated view: '{view.route}'")
            old_view = self.get_route_view(view.route)
            self.views.remove(old_view)

        if view not in self.views:
            self.views.append(view)
        # Add view references.
        view.page = self
        view.parent = self

        # Add the event.
        page_add_view_event = PageEventDefineView(
            view_route=view.route,
            view_uuid=view.uuid
        )
        event = EventCore(
            event_type=EventType.PAGE_EVENT,
            data=PageEvent(
                event_name=PageEventName.ADD_VIEW,
                data=page_add_view_event.model_dump()
            ).model_dump()
        )
        self.add_event(event)

        view.update()

    def push_page_exception (self, exc: str, traceback: str = ""):
        raise Exception(f"{traceback}\n\n{exc}")

    def get_route_view (self, route: str):
        for v in self.views:
            if (v.route == route):
                return v
        self.push_page_exception(f"There is no View for route '{route}'")


    def fetch_events_clean (self) -> list[EventCore]:
        """Returns a list of next events, ordered in events time, then clean the events cache."""
        current_events = self.__next_events.copy()
        self.__next_events.clear()
        return current_events


    def add_event (self, event: EventCore):
        """Store any event in the next events cache of the session."""
        if type(event) != EventCore:
            raise TypeError(f"Event must be an EventCore not '{type(event)}'.")
        self.__next_events.append(event)

        if self.__adapter_hook_on_add_event != None:
            self.__adapter_hook_on_add_event(event)

    def add_page_event (self, event_name: PageEventName, data: dict):
        page_event = PageEvent(
            event_name=event_name,
            data=data
        )
        event = EventCore(event_type=EventType.PAGE_EVENT,
                          data=page_event.model_dump())
        self.add_event(event)

    def present_view (self, view_route: str | View):
        if isinstance(view_route, View):
            view_route = view_route.route
        self.get_route_view(view_route)

        page_present_event = PageEventPresentView(view_route=view_route)
        self.add_page_event(PageEventName.PRESENT_VIEW, page_present_event.model_dump())
        self.__current_route = view_route


    def fire_interaction_event (self, event_data: InteractionEvent):
        control: Control = self.get_control_by_uuid(event_data.control_uuid)
        control._on_client_interaction(event_data)

    def _handle_client_page_event (self, ev: ClientPageEvent):
        if ev.event_name == ClientPageEventName.UNHANDLED_ROUTE:
            data = ClientPageEventUnhandeldRoute(**ev.data)
            self.__run_event_handler(self.on_unhandled_route_change, data.route)

    def get_control_by_uuid (self, uuid:str):
        if uuid == "WINDOW": return self.window
        found_control = None
        for v in self.views:
            if v.uuid == uuid: return v
            found_control = find_control_by_uuid(uuid=uuid, controls=v.controls)
            if found_control is not None: break
        return found_control

    def is_route_exist (self, route: str):
        """Checks if a route view exists in this page.views list."""
        for v in self.views:
            if v.route == route and v.page != None: return True
        return False


    def update_title (self, title: str):
        """Update the page title.
        
        Modifies the head.title content."""
        self.head.title.content = str(title)
        self.head.title.update()


    def _client_changed_route (self, route: str, informative: bool = False):
        """Fired by the adapter when the client change the route.
        
        if informative, the page.current_route will be updated only with no more actions."""
        if informative:
            self.__current_route = route
            return
        if route == "/": return

        if self.is_route_exist(route):
            self.present_view(route)
        else:
            self.__run_event_handler(self.on_unhandled_route_change, route)

    def __remove_view (self, view: View):
        view.page = None
        view.parent = None
        self.add_page_event(
            event_name=PageEventName.REMOVE_VIEW,
            data=PageEventDefineView(
                view_route=view.route,
                view_uuid=view.uuid
            ).model_dump()
        )

    def __run_event_handler (self, func, *args):
        if func == None: return
        execute_target(target=func, args=args)
    
    # Props
    @property
    def adapter_hook_on_add_event (self):
        """Used by adapters to hook into the add_event function."""
        return

    @adapter_hook_on_add_event.setter
    def adapter_hook_on_add_event (self, hooker):
        if self.__adapter_hook_on_add_event != None:
            raise Exception("This property is locked.")
        self.__adapter_hook_on_add_event = hooker

    @property
    def current_view (self) -> View:
        return self.get_route_view(self.current_route)

    @property
    def session_id (self) -> str:
        return self.__session_id

    @property
    def current_route (self) -> str:
        return self.__current_route