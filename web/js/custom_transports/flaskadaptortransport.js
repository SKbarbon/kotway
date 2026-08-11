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
                this.onFatalError("Can't get host updates: " + error);
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

        let buffer = ""; // Accumulates incoming raw chunk fragments

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;

            buffer += value;
            
            // Network chunks do not align with JSON boundaries.
            // Split incoming text buffer by line breaks.
            const lines = buffer.split("\n");
            
            // The last item in 'lines' might be an incomplete JSON line,
            // so we keep it in 'buffer' to prepend to the next network chunk.
            buffer = lines.pop(); 

            for (const line of lines) {
                const trimmed = line.trim();
                if (!trimmed) continue; // Ignore empty frames

                try {
                    const parsedData = JSON.parse(trimmed);
                    const events = parsedData?.events;

                    if (Array.isArray(events)) {
                        events.forEach((ev) => this.onHostEvent(ev));
                    }
                } catch (err) {
                    console.error("Failed to parse chunk line:", err);
                    console.log("Error on value: " + trimmed);
                    this.onFatalError(err);
                }
            }
        }

        // Parse any remaining trailing string in buffer when stream completes
        if (buffer.trim()) {
            try {
                const parsedData = JSON.parse(buffer.trim());
                const events = parsedData?.events;
                if (Array.isArray(events)) {
                    events.forEach((ev) => this.onHostEvent(ev));
                }
            } catch (err) {
                console.error("Failed to parse remaining stream buffer:", err);
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