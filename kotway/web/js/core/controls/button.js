import { ParentControl } from "./parentcontrol.js";


export class Button extends ParentControl {
    constructor () {
        super();
        this.htmlElement = document.createElement("button");
        
        // this.listenToInteractionEvent(
        //     null,
        //     "click"
        // )
    }
}