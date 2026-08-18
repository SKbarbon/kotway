from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...page import Page

from ...models import EventCore, EventType, PageEvent, PageEventName
from ...models.events.headevent import *
from .headelement import HeadElement
from .title import Title


class Head:
    """The Page.head element.
    
    Representing the `<head>` element in HTML which is a container for metadata."""
    def __init__(self, page: Page):
        self.__page: Page = page
        self.__elements: list[HeadElement] = []

        self.__title: Title = Title("kotway")
        self.__title.page = page
        self.__title.uuid = "TITLE"

    def add_element (self, element: HeadElement):
        """Add a head element"""
        element.page = self.page
        self.__elements.append(element)
        self._add_head_event(
            event_name=HeadEventName.ADD_ELEM,
            event_data=HeadEventDataAddElem(
                element_name=element._get_element_name(),
                element_uuid=element.uuid
            ).model_dump()
        )
        element.update()

    def remove_element (self, element: HeadElement):
        element.page = None
        self.__elements.remove(element)
        self._add_head_event(
            event_name=HeadEventName.REMVOVE_ELEM,
            event_data=HeadEventDataRemElem(
                element_uuid=element.uuid
            ).model_dump()
        )

    def _add_head_event (self, event_name: HeadEventName, event_data: dict):
        """Cache the head event in the next events for the page."""
        hev = HeadEvent(
            event_name=event_name,
            data=event_data
        )
        ev = EventCore(
            event_type=EventType.PAGE_EVENT,
            data=PageEvent(
                event_name=PageEventName.HEAD_EVENT,
                data=hev.model_dump()
            ).model_dump()
        )
        self.page.add_event(ev)

    @property
    def page (self) -> Page:
        return self.__page

    @property
    def title (self) -> Title:
        return self.__title