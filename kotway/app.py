from .adapters import AppAdapter, FlaskAdapter, PyodideAdapter
from .page import Page
import uuid, sys

from .utils.execute_target import execute_target
from .utils.get_webapp_path import get_webapp_path

class App ():
    """The manager for kotway app pages."""
    def __init__(self, target, custom_adapter=None, webapp_path: str=None, debug: bool = False):
        self.target = target
        self.debug = debug

        if custom_adapter == None:
            if "pyodide" in sys.modules:
                self.app_adapter: AppAdapter = PyodideAdapter()
            else:
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
        self.app_adapter.debug = self.debug
        self.app_adapter.start()


    # == Adapter APIs ==
    def start_new_page_session (self, requested_route: str) -> Page:
        new_page = Page(
            session_id=str(uuid.uuid4())
        )

        def run_target ():
            self.target(new_page)
            new_page._client_changed_route(requested_route)

        execute_target(target=run_target)

        self.active_pages[new_page.session_id] = new_page
        return new_page

    def remove_page_session (self, session_id: str):
        if session_id in self.active_pages:
            page = self.active_pages[session_id]
            execute_target(target=page.on_session_end)
            del self.active_pages[session_id]

    def get_page_by_sessionid (self, session_id):
        if session_id in self.active_pages:
            return self.active_pages[session_id]
        return None