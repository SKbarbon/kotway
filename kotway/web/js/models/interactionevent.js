

export class InteractionEvent {
    constructor (data = {}) {
        this.control_uuid = data.control_uuid;
        this.interaction_name = data.interaction_name;
        this.data = data.data;
    }
}