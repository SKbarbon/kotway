from ..appadapter import AppAdapter
from ...models import ClientEvent, EventCore, EventType
from flask import Flask, send_file, request, Response, url_for
from flask.logging import default_handler
from flask_cors import CORS
import os, json, time, logging, webbrowser

from .client_stream_manager import ClientStreamManager

class FlaskAdapter (AppAdapter):
    def __init__(self):
        super().__init__()

        self.flask_app = Flask("__main__")
        CORS(self.flask_app)

        # 1. Catch the root domain /
        self.flask_app.add_url_rule(
            rule='/',
            endpoint='catch_all_root',
            view_func=self._flask_catch,
            defaults={'path': ''},
            methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
        )

        # 2. Catch all sub-paths
        self.flask_app.add_url_rule(
            rule='/<path:path>',
            endpoint='catch_all_paths',
            view_func=self._flask_catch,
            methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
        )

        # Client Streams Managers
        self.clients_streams_managers: dict[str, ClientStreamManager] = {}


    def _flask_catch (self, path="/"):
        if path == "" and request.method == "POST":
            try: event_data = ClientEvent(**request.get_json())
            except: return
            self.on_client_event(event_data)
            return {}
        elif path == "stream_events" and request.method == "POST":
            session_id = request.get_json()["sessionId"]
            return Response(self.stream_events(session_id), mimetype="text/event-stream")

        if os.path.isfile(os.path.join(self.webapp_path, path)):
            return send_file(os.path.join(self.webapp_path, path))

        session_id = self.create_session(requested_route=request.path)
        return self.__get_index_content(session_id)

    def stream_events (self, session_id: str):
        stream_manager = ClientStreamManager(session_id)
        self.clients_streams_managers[session_id] = stream_manager

        try:
            while stream_manager.keep_alive:
                events = self.fetch_session_events(session_id)
                if stream_manager.should_ask_for_ping and stream_manager.ping_request_sent == False:
                    events.append(EventCore(event_type=EventType.PING_EVENT, data={}))
                    stream_manager.ping_request_sent = True
                
                if events != []:
                    response = {"events": [e.model_dump(mode='json') for e in events]}
                    yield f"{json.dumps(response)}\n\n"

                stream_manager.update()
                time.sleep(0.05)
        finally:
            self.on_client_session_end(session_id)

    def start(self):
        host_url = f"http://localhost:{self.port}"

        if not self.debug:
            # Set Werkzeug to only output ERROR and CRITICAL logs
            logging.getLogger('werkzeug').setLevel(logging.ERROR)
            
            # Set Flask's app logger to only output ERRORs
            self.flask_app.logger.setLevel(logging.ERROR)
            
            print(f"Host is running at: {host_url}")

        try:
            webbrowser.open(host_url)
        except:
            pass
        self.flask_app.run(
            port=self.port,
            debug=False,
            threaded=True,
            host="localhost"
        )

    def on_client_pong(self, session_id):
        if session_id in self.clients_streams_managers:
            sm = self.clients_streams_managers[session_id]
            sm.pong()

    def on_client_session_end(self, session_id):
        super().on_client_session_end(session_id)
        if session_id in self.clients_streams_managers:
            self.clients_streams_managers[session_id].keep_alive = False
            del self.clients_streams_managers[session_id]


    def __get_index_content (self, session_id: str) -> str:
        index_path = os.path.join(self.webapp_path, "index.html")
        cont = open(index_path, encoding="utf-8").read()

        cont = cont.replace("const sessionId = null;",
                            f'const sessionId = "{session_id}";')
        return cont