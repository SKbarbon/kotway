from .models import EventCore, EventType, InteractionEvent
from .utils.find_control_by_uuid import find_control_by_uuid
from .models.events.pageevent import *
from .custom_collections.viewslist import ViewsList
from .controls.control import Control
from .controls.view import View

class Page:
    """
A Page is a session and views container.
    """
    def __init__(self, session_id: str):
        self.__session_id: str = session_id
        self.views: list[View] = ViewsList()
        self.views.append(View("/"))
        self.current_route: str = "/"

        self.__next_events: list[EventCore] = []

        self.update()
        self.present_view("/")

    # utils
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

    def update (self):
        # Make sure Views have the Page reference and registered.
        for v in self.views:
            if v.page == None:
                v.parent = self
                v.page = self
                page_add_view_event = PageEventAddView(
                    view_route=v.route,
                    view_uuid=v.uuid
                )
                event = EventCore(
                    event_type=EventType.PAGE_EVENT,
                    data=PageEvent(
                        event_name=PageEventName.ADD_VIEW,
                        data=page_add_view_event.model_dump()
                    ).model_dump()
                )
                self.add_event(event)

        for v in self.views:
            v.update()

    def fire_interaction_event (self, event_data: InteractionEvent):
        control: Control = self.get_control_by_uuid(event_data.control_uuid)
        control._on_client_interaction(event_data)


    def get_control_by_uuid (self, uuid:str):
        for v in self.views:
            if v.uuid == uuid: return v
            control = find_control_by_uuid(uuid=uuid, controls=v.controls)
            return control

    # Props

    @property
    def current_view (self) -> View:
        return self.get_route_view(self.current_route)

    @property
    def session_id (self) -> str:
        return self.__session_id