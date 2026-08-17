from ..appadapter import AppAdapter
from ...models.events.client_events.clientevent import ClientEvent
from ...models.events.eventcore import EventCore
import sys, json
import asyncio

# If running inside pyodide env, import js.
if "pyodide" in sys.modules:
    from pyodide.ffi import create_proxy
    import js

class PyodideAdapter (AppAdapter):
    """The adapter for Python pyodide.
    
    NOTE: This adapter thinks it is running inside a pyodide environment."""
    def __init__(self):
        super().__init__()

        if not self.__is_env_pyodide():
            raise Exception("This adapter should run only inside pyodide environment.")

        # Hook to messages listener.
        self.message_handler = create_proxy(self.__on_worker_message)
        js.self.addEventListener("message", self.message_handler)

    def start(self):
        # Start a local page session
        self.session_id = self.create_session("/")
        js.postMessage(json.dumps({"sessionId": self.session_id}))

        self.page = self.app_class.get_page_by_sessionid(self.session_id)


        self.page.adapter_hook_on_add_event = self.send_app_event
        self.send_app_event(None)

    def send_app_event (self, event: EventCore):
        """Event from the python app."""
        for e in self.fetch_session_events(self.session_id):
            js.postMessage(e.model_dump_json())

    def __on_worker_message (self, message):
        """Called whenever a new message from the Js worker is sent."""
        self.on_client_event(ClientEvent(**message.data.to_py()))


    def __is_env_pyodide (self) -> bool:
        """Check if the environment is pyodide."""
        return "pyodide" in sys.modules