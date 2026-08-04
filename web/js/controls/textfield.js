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
                this.fieldElem,
                ie
            )
        });
        
        this.listenToInteractionEvent(
            null,
            "submit"
        )

        this._setTrigger("focus", this.toggleFocus.bind(this));
    }

    updateProp (proptype, propName, propValue) {
        if (proptype == "prop") {
            this.fieldElem[propName] = propValue;
        }
        else if (proptype == "style") {
            this.fieldElem.style.setProperty(propName, propValue);
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