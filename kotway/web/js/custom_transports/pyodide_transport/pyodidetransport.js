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
    }

    listenToEvents() {
        this.pythonWorker.postMessage("start")
    }

    sendClientEvent (event) {
        this.pythonWorker.postMessage(event);
    }

    /**
     * Handle the messages from the python worker.
     * @param {string} message 
     */
    _handlerPythonWorkerMessage (message) {
        try {
            const event = JSON.parse(message);
            // If provided sessionId, store it.
            if ("sessionId" in event) {
                sessionStorage.setItem('sessionId', event.sessionId);
            }
            this.onHostEvent(event);
        } catch (err) {
            console.error("Failed to parse chunk line:", err);
            console.log("Error on value: " + message);
            this.onFatalError(err);
        }
    }
}