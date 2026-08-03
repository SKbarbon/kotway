import {AdapterTransport} from "../adaptertransport.js";


export class FlaskAdaptorTransport extends AdapterTransport {
    constructor () {
        super();
        this.hostUrl = window.location.origin;
    }

    start () {
        this.listenToEvents()
            .then((data) => {
            console.log("Async result received:", data);
            })
            .catch((error) => {
            console.error("Error in async operation:", error);
                this.onFatalError("Can't get host updates: "+error);
            });
    }

    async listenToEvents() {
        const streamUrl = new URL("/stream_events", this.hostUrl);

        const response = await fetch(streamUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                sessionId: this.page.getSessionId(),
            }),
        });

        const reader = response.body
            .pipeThrough(new TextDecoderStream())
            .getReader();

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;

            try {
                const parsedData = JSON.parse(value);
                const events = parsedData?.events;

                if (Array.isArray(events)) {
                    events.forEach((ev) => this.onHostEvent(ev));
                }
            } catch (err) {
                console.error("Failed to parse chunk:", err);
                this.onFatalError(err);
            }
        }
    }

    sendClientEvent (event) {
        // Sending the POST request
        fetch(window.location.origin, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(event),
        })
        .then((response) => response.json())
        .then((data) => {
            // console.log("Success:", data);
        })
        .catch((error) => {
            console.error("Error:", error);
            this.onFatalError(error);
        });
    }
}