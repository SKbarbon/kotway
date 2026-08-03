import { ParentControl } from "./parentcontrol.js";


export class View extends ParentControl{
    constructor (route) {
        super();
        this.route = route;
        this.htmlElement = document.createElement("div");
    }

    addControl (control) {
        super.addControl(control)
        control.view = this;
    }
}