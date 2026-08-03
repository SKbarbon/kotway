from .adapters import AppAdapter, FlaskAdapter
from .page import Page
import uuid, threading

from .utils.get_webapp_path import get_webapp_path

class App ():
    """The manager for kotway app pages."""
    def __init__(self, target, custom_adapter=None, webapp_path: str=None):
        self.target = target

        if custom_adapter == None:
            self.app_adapter: AppAdapter = FlaskAdapter()
        else:
            self.app_adapter: AppAdapter = custom_adapter

        if webapp_path == None:
            self.webapp_path = get_webapp_path()
        else:
            self.webapp_path = webapp_path

        self.active_pages: dict[str, Page] = {}

    def run (self, port: int = 1544):
        self.app_adapter.port = port
        self.app_adapter.webapp_path = self.webapp_path
        self.app_adapter.app_class = self
        self.app_adapter.start()


    # == Adapter APIs ==
    def start_new_page_session (self) -> Page:
        new_page = Page(str(uuid.uuid4()))

        threading.Thread(target=self.target, args={new_page}, daemon=True).start()

        self.active_pages[new_page.session_id] = new_page
        return new_page

    def get_page_by_sessionid (self, session_id):
        if session_id in self.active_pages:
            return self.active_pages[session_id]
        return None