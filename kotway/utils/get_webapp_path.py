import os

def get_webapp_path ():
    """Get the default webapp path"""
    util_path = os.path.dirname(__file__)
    root_path = os.path.dirname(util_path)
    web_path = os.path.join(root_path, "web")

    return web_path