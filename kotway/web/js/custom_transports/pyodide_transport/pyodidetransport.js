import { AdapterTransport } from "../../adaptertransport.js";

/**
 * The main entry of the Pyodide transport for the pyodide python's adapter.
 * 
 * It starts the python worker, then runs the Python script.
 */
export class PyodideTransport extends AdapterTransport {
    constructor () {
        super();
        this.pythonWorker = new Worker(new URL('./python-worker.js', import.meta.url));
        this.pythonWorker.onmessage = (event) => {this._handlerPythonWorkerMessage(event.data);}
        
        this.pythonWorker.postMessage("start")
    }

    listenToEvents() {

    }

    /**
     * Handle the messages from the python worker.
     * @param {string} message 
     */
    _handlerPythonWorkerMessage (message) {
        console.log("Transport got a message: " + message)
    }
}