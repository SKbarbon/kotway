import {Control} from "./control.js";

export class TextField extends Control {
    constructor () {
        super();
        this.htmlElement = document.createElement("form");
        this.fieldElem = document.createElement("input");
        this.htmlElement.append(this.fieldElem);

        this.htmlElement.type = "text";

        const interactionEvents = ["input", "change"];
        interactionEvents.forEach(ie => {
            this.listenToInteractionEvent(
                ie,
                this.fieldElem
            )
        });
        
        this.listenToInteractionEvent(
            "submit",
            null
        )

        this._setTrigger("focus", this.toggleFocus.bind(this));

        // Can't remove or modify the activation of textfield events as their customized.
        // this.listenToInteractionEvent = function() {};
        // this.removeInteractionEventListener = function() {};
    }

    updateProp (proptype, propName, propValue) {
        if (proptype == "prop") {
            this.fieldElem[propName] = propValue;
        }
        else if (proptype == "style") {
            this.fieldElem.style.setProperty(propName, propValue);
        }
    }

    removeProp (proptype, propName) {
        if (proptype == "prop") {
            this.fieldElem.removeAttribute(propName);
        }
        else if (proptype == "style") {
            this.fieldElem.style.removeProperty('color');
        }
    }

    toggleFocus (data) {
        const focusState = data.state;
        if (focusState == true) {
            this.fieldElem.focus();
        } else {
            this.fieldElem.blur();
        }
    }
}