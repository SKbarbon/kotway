import { ParentControl } from "./parentcontrol.js";


export class Container extends ParentControl {
    constructor () {
        super();

        this.htmlElement = document.createElement("div");
    }
}