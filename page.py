from .models import EventCore, EventType, InteractionEvent
from .utils.find_control_by_uuid import find_control_by_uuid
from .models.events.pageevent import *
from .controls.window import Window
from .custom_collections.viewslist import ViewsList
from .controls import Control, View

import threading

class Page:
    """
A Page is a session and views container.
    """
    def __init__(self, session_id: str, requested_route: str):
        self.__session_id: str = session_id
        self.__next_events: list[EventCore] = []

        self.window = Window(page=self)

        self.views: list[View] = ViewsList(
            on_remove=self.__remove_view
        )
        self.views.append(View("/"))

        self.__current_route: str = "/"
        self.__href: str = ""

        self.update()
        self.present_view("/")

        # Events
        self.on_unhandled_route_change = None
        """When the client goes to a route that has no view."""

        self.on_route_change = None
        """When the client goes to a route that has an existed view, and the transition managed automatically."""

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
        current_events.sort(key=lambda event: event.event_time)
        self.__next_events.clear()
        return current_events


    def add_event (self, event: EventCore):
        """Store any event in the next events cache of the session."""
        if type(event) != EventCore:
            raise TypeError(f"Event must be an EventCore not '{type(event)}'.")
        self.__next_events.append(event)

    def add_page_event (self, event_name: PageEventName, data: dict):
        page_event = PageEvent(
            event_name=event_name,
            data=data
        )
        event = EventCore(event_type=EventType.PAGE_EVENT,
                          data=page_event.model_dump())
        self.add_event(event)

    def present_view (self, view_route: str):
        self.get_route_view(view_route)

        page_present_event = PageEventPresentView(view_route=view_route)
        self.add_page_event(PageEventName.PRESENT_VIEW, page_present_event.model_dump())
        self.__current_route = view_route


    def fire_interaction_event (self, event_data: InteractionEvent):
        control: Control = self.get_control_by_uuid(event_data.control_uuid)
        control._on_client_interaction(event_data)


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


    def _client_changed_route (self, route: str, handled: bool):
        """Fired by the adapter when the client change the route."""
        if handled == None and route == "/": handled = True

        if handled:
            self.__run_event_handler(self.on_route_change, route)
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
        threading.Thread(target=func, args=args, daemon=True).start()

    # Props

    @property
    def current_view (self) -> View:
        return self.get_route_view(self.current_route)

    @property
    def session_id (self) -> str:
        return self.__session_id

    @property
    def current_route (self) -> str:
        return self.__current_route

    @property
    def href (self) -> str:
        """The href which the client is at. Updated by the client only."""
        self.__href