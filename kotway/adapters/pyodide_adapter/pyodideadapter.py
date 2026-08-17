from ..appadapter import AppAdapter
import sys

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


    def start(self):
        print("Pyodide adapter should start.")

    def __on_worker_message (self, message):
        """Called whenever a new message from the Js worker is sent."""
        print(f"Pyodide got message: {message}")


    def __is_env_pyodide (self) -> bool:
        """Check if the environment is pyodide."""
        return "pyodide" in sys.modules