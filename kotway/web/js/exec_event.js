import {PageEventWorker} from "./events_workers/pageeventworker.js"
import { ControlEventWorker } from "./events_workers/controleventworker.js";
import { ClientEventType } from "./models/clientevent.js";

export function eventExecutor (ev, page) {
    const event_type = ev["event_type"];
    const event_data = ev["data"];

    if (event_type == "page_event") {
        new PageEventWorker(page, event_data);
    }
    else if (event_type == "control_event") {
        new ControlEventWorker(event_data, page);
    }
    else if (event_type == "ping_event") {
        page.announceClientEvent(
            ClientEventType.PONG,
            {}
        )
    }
}