from ..core.controls.parentcontrol import ParentControl

def find_control_by_uuid (uuid:str, controls: list):
    for c in controls:
        if uuid == c.uuid:
            return c

        if isinstance(c, ParentControl):
            cc = find_control_by_uuid(uuid, c.controls)
            if cc != None:
                return cc