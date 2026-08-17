

export const ClientPageEventName = Object.freeze({
    UNHANDLED_ROUTE: "unhandled_route"
});

export class ClientPageEvent {
    constructor (data = {}) {
        this.event_name = data.event_name;
        this.data = data.data;
    }
}

export class ClientPageEventUnhandeldRoute {
    constructor (data = {}) {
        this.route = data.route;
    }
}