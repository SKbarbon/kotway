import time


class ClientStreamManager:
    """Manages the life of a stream events."""
    def __init__(self, session_id: str):
        self.session_id: str = session_id
        self.pong_resp_limit = 15

        self.last_ping = time.time()
        self.keep_alive = True

        self.ping_request_sent = False
        self.should_ask_for_ping = False

    def pong (self):
        """The client ponged the ping"""
        self.ping_request_sent = False
        self.should_ask_for_ping = False
        self.last_ping = time.time()

    def update (self):
        """Called in the loop"""
        if time.time() - self.last_ping > self.pong_resp_limit:
            self.keep_alive = False

        elif time.time() - float(self.last_ping) > self.pong_resp_limit / 2:
            self.should_ask_for_ping = True