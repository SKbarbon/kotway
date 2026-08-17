import {Control} from "./control.js";

export class TextField extends Control {
    constructor () {
        super();
        this.htmlElement = document.createElement("input");
        this.htmlElement.type = "text";

        // const interactionEvents = ["input", "change"];
        // interactionEvents.forEach(ie => {
        //     this.listenToInteractionEvent(
        //         ie
        //     )
        // });

        this._setTrigger("focus", this.toggleFocus.bind(this));
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