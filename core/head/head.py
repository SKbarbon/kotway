from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...page import Page

from .headelement import HeadElement


class Head:
    """The Page.head element.
    
    Representing the `<head>` element in HTML which is a container for metadata."""
    def __init__(self, page: Page):
        self.__page: Page = page
        self.__elements: list[HeadElement] = []

    def add_element (self, element: HeadElement):
        """Add a head element"""
        self.__elements.append(element)

    def remove_element (self, element: HeadElement):
        self.__elements.remove(element)

    def _add_head_event (self, event):
        """Cache the head event in the next events for the page."""

    @property
    def page (self):
        return self.__page