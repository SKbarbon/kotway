from pydantic import BaseModel

class InteractionEvent (BaseModel):
    control: None = None
    control_uuid: str
    interaction_name: str
    data: dict