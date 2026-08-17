import { View } from "../core/controls/view.js";
import { HeadEventWorker } from "./headeventworker.js";

export class PageEventWorker {
    constructor (page, pageEvent) {
        this.pageEvent = pageEvent;
        this.page = page;

        if (pageEvent.event_name == "add_view") {
            const add_ev_data = pageEvent.data;
            this.addNewView(add_ev_data);
        }
        else if (pageEvent.event_name == "present_view") {
            const viewRoute = pageEvent.data.view_route;
            this.presentRouteView(viewRoute)
        }
        else if (pageEvent.event_name == "remove_view") {
            const viewUuid = pageEvent.data.view_uuid;
            this.page.removeView(viewUuid);
        }
        else if (pageEvent.event_name == "head_event") {
            new HeadEventWorker(
                page,
                pageEvent.data
            );
        }
    }

    addNewView (view_data) {
        var newView = new View(view_data.view_route);
        newView.uuid = view_data.view_uuid;
        this.page.addView(newView);
    }

    presentRouteView (viewRoute) {
        this.page.presentRouteView(viewRoute);
    }
}