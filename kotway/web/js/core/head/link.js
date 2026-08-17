import {HeadElement} from "./headelement.js"

export class Link extends HeadElement {
    constructor () {
        super();
        this.htmlElement = document.createElement("link");
    }
}