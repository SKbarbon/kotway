import {eventExecutor} from "./exec_event.js"


export class AdapterTransport {
    constructor () {
        this.page = null;
    }

    /**
     * Start the transport.
     */
    start () {
        this.listenToEvents();
    }

    /**
     * Subclasses override this. Used to start listening to new events from the adapter.
     */
    listenToEvents () {

    }

    onHostEvent (event) {
        eventExecutor(event, this.page);
    }

    /**
     * Send an event from this client to the Python app.
     * @param {*} event 
     */
    sendClientEvent (event) {

    }
    
    onFatalError (content) {
        this.page.displayErrorPage(content);
    }
}