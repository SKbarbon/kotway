importScripts("https://cdn.jsdelivr.net/pyodide/v0.27.2/full/pyodide.js");

self.installRequirementsScript = `
import micropip

requirements = open("app/requirements.txt", encoding="utf-8").read()

packages = [
    line.strip()
    for line in requirements.splitlines()
    if line.strip() and not line.strip().startswith("#")
]

await micropip.install(packages)
`

// Start pyodide Python, get the python app, run it.
self.initPyodide = async function () {
    const pyodide = await loadPyodide();
    var appPath = self.location.origin + "/app.zip"
    await pyodide.loadPackage("micropip");
    await pyodide.runPythonAsync(`
import sys, runpy, traceback, os
from pyodide.http import pyfetch

# Get the app zip file. Extract it.
response = await pyfetch("${appPath}")
await response.unpack_archive()

# Download requirements
${self.installRequirementsScript}

# Try to run the app.
try:
    # 1. Change directory to the unzipped app folder
    os.chdir("app")
    
    # 2. Add the absolute current working directory to sys.path
    #    This lets Python find 'views' directly inside 'app'
    sys.path.insert(0, os.getcwd())
    
    # 3. Run 'main' directly instead of 'app.main'
    runpy.run_module("main", run_name="__main__")
except Exception as e:
    traceback.print_exception(e)
  `);
  
}

self.onmessage = async (event) => {
    const message = event.data;

    // A command to start/init pyodide.
    if (message == "start") {
        await self.initPyodide();
    }
}