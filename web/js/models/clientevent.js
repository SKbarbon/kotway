

export const ClientEventType = Object.freeze({
    INTERACTION: "interaction"
});

export class ClientEvent {
    constructor (data = {}) {
        this.sessionId = data.sessionId;
        this.event_time = data.event_time;
        this.event_type = data.event_type;
        this.event_data = data.event_data;
    }
}