import {HeadElement} from "./headelement.js"

export class Title extends HeadElement {
    constructor () {
        super();
        this.htmlElement = document.createElement("title");
    }
}