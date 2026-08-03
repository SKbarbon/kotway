import {ClientEvent, ClientEventType} from "./models/clientevent.js";
import { findControlByUuid } from "./utils/findcontrolbyuuid.js";
import { FatalErrorMessageView } from "./custom_views/fatalerrormessageview.js";

export class Page {
    constructor (adapterTransport) {
        this.adapterTransport = adapterTransport;
        this.views = [];
        this.currentRoute = "";

        this.viewsContainer = document.getElementById("VIEWS_CONTAINER");
    }

    getSessionId () {
        return sessionStorage.getItem('sessionId');
    }

    addView (view) {
        view.page = this;
        this.views.push(view);
    }

    presentRouteView (route) {
        const v = this.getViewByRoute(route);
        this.viewsContainer = document.getElementById("VIEWS_CONTAINER");
        this.viewsContainer.replaceChildren();

        this.viewsContainer.append(v.htmlElement);
    }

    getViewByRoute (route) {
        const view = this.views.find(v => v.route === route);
        if (view) {
            return view;
        }
        console.error("There is no found View for the route: "+route)
    }

    getControlByUuid (uuid) {
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
    announceInteractionEvent (control, interactionData) {
        const clientEvent = new ClientEvent({
            sessionId: this.getSessionId(),
            event_time: Date.now(),
            event_type: ClientEventType.INTERACTION,
            event_data: interactionData
        })
        this.adapterTransport.sendClientEvent(clientEvent);
    }

    /**
     * Used to display an error message in a brand new page.
     * @param {*} errorContent Error message.
     */
    displayErrorPage (errorContent) {
        const erv = new FatalErrorMessageView(errorContent);
        this.addView(erv);
        this.presentRouteView(erv.route);
    }
}