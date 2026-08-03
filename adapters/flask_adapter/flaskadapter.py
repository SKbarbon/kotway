from ..appadapter import AppAdapter
from ...models import ClientEvent
from flask import Flask, send_file, request, Response
from flask_cors import CORS
import os, json, time

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


    def _flask_catch (self, path="/"):
        if path == "" and request.method == "POST":
            event_data = ClientEvent(**request.get_json())
            self.onClientEvent(event_data)
            return {}
        elif path == "stream_events" and request.method == "POST":
            session_id = request.get_json()["sessionId"]
            return Response(self.stream_events(session_id), mimetype="text/event-stream")

        if os.path.isfile(os.path.join(self.webapp_path, path)):
            return send_file(os.path.join(self.webapp_path, path))

        session_id = self.create_session()
        return self.__get_index_content(session_id)

    def stream_events (self, session_id: str):
        while True:
            events = self.fetchSessionEvents(session_id)
            if events != []:
                response = {"events": [e.model_dump(mode='json') for e in events]}
                yield f"{json.dumps(response)}\n\n"

            time.sleep(0.05)

    def start(self):
        self.flask_app.run(
            port=self.port,
            debug=False,
            threaded=True,
            host="localhost"
        )


    def __get_index_content (self, session_id: str) -> str:
        index_path = os.path.join(self.webapp_path, "index.html")
        cont = open(index_path, encoding="utf-8").read()

        cont = cont.replace("const sessionId = null;",
                            f'const sessionId = "{session_id}";')
        return cont