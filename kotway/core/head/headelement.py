from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...page import Page
from ...models.events.headevent import HeadEventName, HeadEventDataUpdateElem
import uuid

class HeadElement:
    """Core class for head elements."""
    def __init__(self):
        self.page: Page = None
        self.uuid: str = str(uuid.uuid4())
        self.current_props: dict[str, any] = {}


    def update (self):
        """Append an update event of this element in the next page sent events."""
        if self.page == None: raise Exception("Element must be added to the Page's head first.")
        self.page.head._add_head_event(
            event_name=HeadEventName.UPDATE_ELEM,
            event_data=HeadEventDataUpdateElem(
                element_uuid=self.uuid,
                props=self.current_props
            ).model_dump()
        )

    def _set_prop (self, prop_name: str, value: any):
        self.current_props[prop_name] = value

    def _get_prop (self, prop_name: str):
        if prop_name in self.current_props:
            return self.current_props[prop_name]

    def _get_element_name (self):
        return str(type(self).__name__)