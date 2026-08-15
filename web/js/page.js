import {ClientEvent, ClientEventType} from "./models/clientevent.js";
import { findControlByUuid } from "./utils/findcontrolbyuuid.js";
import { FatalErrorMessageView } from "./custom_views/fatalerrormessageview.js";
import { Window } from "./controls/window.js";
import { ClientPageEvent, ClientPageEventName, ClientPageEventUnhandeldRoute } from "./models/clientpageevent.js";

export class Page {
    constructor (adapterTransport) {
        this.adapterTransport = adapterTransport;
        this.window = new Window(this);
        
        this.views = [];
        this.currentRoute = "";

        this.viewsContainer = document.getElementById("VIEWS_CONTAINER");

        // Listen to page route changes.
        window.addEventListener("popstate", (event) => {
            const routeName = window.location.pathname;
            this.presentRouteView(routeName, false);
        });
    }

    getSessionId () {
        return sessionStorage.getItem('sessionId');
    }

    addView (view) {
        view.page = this;
        this.views.push(view);
    }

    removeView (viewUuid) {
        const view = this.getControlByUuid(viewUuid);
        this.views = this.views.filter(item => item !== view);
    }

    presentRouteView (route, updateState) {
        let v;
        try {
            v = this.getViewByRoute(route);
        }
        catch {
            v = null;
        }
        if (v == null) {
            this.announceClientEvent(
                ClientEventType.CLIENT_PAGE,
                new ClientPageEvent({
                    event_name: ClientPageEventName.UNHANDLED_ROUTE,
                    data: new ClientPageEventUnhandeldRoute({
                        route: route
                    })
                })
            );
            return;
        }
        this.viewsContainer = document.getElementById("VIEWS_CONTAINER");
        this.viewsContainer.replaceChildren();

        this.viewsContainer.append(v.htmlElement);
        if (updateState != false) {
            history.pushState({ page: 1 }, "", v.route); 
        }

        v.announcePresent();
    }

    getViewByRoute (route) {
        const view = this.views.find(v => v.route === route);
        if (view) {
            return view;
        }
        console.error("There is no found View for the route: "+route)
    }

    isRouteExist (route) {
        const view = this.views.find(v => v.route === route);
        if (view == null) {return false;}
        return true;
    }

    getControlByUuid (uuid) {
        if (uuid == "WINDOW") {return this.window;}
        for (const v of this.views) {
            if (v.uuid == uuid) {return v;}
            const found = findControlByUuid(uuid, v.controls);
            if (found != null) {
                return found;
            }
        }
    }

    /**
     * Can be used by the page and its controls to announce an interaction event.
     * 
     * interactionData: InteractionEvent class.
     */
    announceClientEvent (event_type, data) {
        const clientEvent = new ClientEvent({
            sessionId: this.getSessionId(),
            event_time: Date.now(),
            event_type: event_type,
            event_data: data
        })
        this.adapterTransport.sendClientEvent(clientEvent);
    }

    /**
     * Used to display an error message in a brand new page.
     * @param {*} errorContent Error message.
     */
    displayErrorPage (errorContent) {
        const errorRoute = "/error"
        // if there is a custom error page, present it.
        if (this.isRouteExist(errorRoute)) {
            this.presentRouteView(errorRoute)
            return;
        }

        // else, present default error page.
        const erv = new FatalErrorMessageView(errorContent);
        this.addView(erv);
        this.presentRouteView(erv.route);
    }
}