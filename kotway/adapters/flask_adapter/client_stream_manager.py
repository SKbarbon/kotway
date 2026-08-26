import time


class ClientStreamManager:
    """Manages the life of a stream events."""
    def __init__(self, session_id: str):
        self.session_id: str = session_id
        self.pong_resp_limit = 15

        self.last_ping = time.time()
        self.keep_alive = True
        self.__disconnected: bool = False

        self.ping_request_sent = False
        self.should_ask_for_ping = False

        self.on_disconnect = None
        self.on_reconnect = None
        

    def pong (self):
        """The client ponged the ping"""
        self.ping_request_sent = False
        self.should_ask_for_ping = False
        self.disconnected = False
        self.last_ping = time.time()

    def update (self):
        """Called in the loop"""
        if time.time() - self.last_ping > self.pong_resp_limit:
            self.disconnected = True

        elif time.time() - float(self.last_ping) > self.pong_resp_limit / 2:
            self.should_ask_for_ping = True


    @property
    def disconnected (self):
        return self.__disconnected

    @disconnected.setter
    def disconnected (self, value):
        if value == self.__disconnected: return

        if value == True and self.on_disconnect != None: self.on_disconnect()
        if value == False and self.__disconnected == True:
            if self.on_reconnect != None:
                self.on_reconnect()
        self.__disconnected = value