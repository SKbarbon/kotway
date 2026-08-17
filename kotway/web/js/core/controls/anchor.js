import { ParentControl } from "./parentcontrol.js";


export class Anchor extends ParentControl {
    constructor () {
        super();
        this.htmlElement = document.createElement("a");
    }
}