from pydantic import BaseModel


class PingEvent (BaseModel):
    PING: str = "PING"