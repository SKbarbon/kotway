import {PageEventWorker} from "./events_workers/pageeventworker.js"
import { ControlEventWorker } from "./events_workers/controleventworker.js";

export function eventExecutor (ev, page) {
    const event_type = ev["event_type"];
    const event_data = ev["data"];

    if (event_type == "page_event") {
        new PageEventWorker(page, event_data);
    }
    else if (event_type == "control_event") {
        new ControlEventWorker(event_data, page);
    }
}