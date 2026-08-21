import { InteractionEvent } from "../../models/interactionevent.js";
import {ClientEventType} from "../../models/clientevent.js";

export class Control {
    constructor () {
        this.htmlElement = null;
        this.uuid = null;

        this.page = null;
        this.view = null;
        this.parent = null;

        this.interaEventListenersControllers = {} // eventName: str, controller: AbortController
        this.triggers = {}; // triggerName: str, triggerFunction: void
    }
    
    updateProp (proptype, propName, propValue) {
        if (proptype == "prop") {
            this.htmlElement[propName] = propValue;
        }
        else if (proptype == "style") {
            this.htmlElement.style.setProperty(propName, propValue);
        }
    }

    removeProp (proptype, propName) {
        if (proptype == "prop") {
            this.htmlElement.removeAttribute(propName);
        }
        else if (proptype == "style") {
            this.htmlElement.style.removeProperty(propName);
        }
    }

    listenToInteractionEvent (interactionName, targetElement) {
        if (targetElement == null) {targetElement=this.htmlElement;}

        // Remove existing event if its there.
        this.removeInteractionEventListener(
            interactionName,
            targetElement
        );

        // Assign new event listner.
        const controller = new AbortController();
        this.interaEventListenersControllers[interactionName] = controller;
        targetElement.addEventListener(interactionName, (e) => {
            e.preventDefault();
            this.onInteractionEvent(interactionName, e.key, e.target.value);
        }, { signal: controller.signal });
    }

    removeInteractionEventListener (interactionEvent, targetElement) {
        if (targetElement == null) {targetElement=this.htmlElement;}

        if (interactionEvent in this.interaEventListenersControllers) {
            this.interaEventListenersControllers[interactionEvent].abort()
        }
    }

    onInteractionEvent (interactionName, eventName, eventValue) {
        if (this.uuid == null) {
            console.warn("Skipped interaction event " + interactionName + ". No uuid.")
            return;
        }
        this.page.announceClientEvent(
            ClientEventType.INTERACTION,
            new InteractionEvent({
                control_uuid: this.uuid,
                interaction_name: interactionName,
                data: {
                    eventName: eventName,
                    value: eventValue
                }
            })
        );
    }

    /**
     * Used to fire a stored trigger.
     */
    executeTrigger (triggerName, data) {
        const triggerFunc = this.triggers[triggerName];

        if (triggerFunc == null) {
            console.error("No trigger found for name: " + triggerName);
            return;
        }
        triggerFunc(data);
    }

    _setTrigger (triggerName, triggerFunc) {
        this.triggers[triggerName] = triggerFunc;
    }
}