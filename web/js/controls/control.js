import { InteractionEvent } from "../models/interactionevent.js";


export class Control {
    constructor () {
        this.htmlElement = null;
        this.uuid = null;

        this.page = null;
        this.view = null;
        this.parent = null;
    }
    
    updateProp (proptype, propName, propValue) {
        if (proptype == "prop") {
            this.htmlElement[propName] = propValue;
        }
        else if (proptype == "style") {
            this.htmlElement.style.setProperty(propName, propValue);
        }
    }

    listenToInteractionEvent (targetElement, interactionName) {
        if (targetElement == null) {targetElement=this.htmlElement}
        targetElement.addEventListener(interactionName, (e) => {
            this.onInteractionEvent(interactionName, e.target.value);
        });
    }

    onInteractionEvent (interactionName, interactionValue) {
        this.page.announceInteractionEvent(
            this,
            new InteractionEvent({
                control_uuid: this.uuid,
                interaction_name: interactionName,
                data: {
                    interactionName: interactionName,
                    interactionValue: interactionValue
                }
            })
        );
    }
}