import {HeadElement} from "./headelement.js"
import { Title } from "./title.js";

export class Head {
    constructor () {
        this.elements = [];

        this.title = new Title();
        this.title.htmlElement = document.getElementById("mainTitle");
        this.title.uuid = "TITLE";
        document.head.appendChild(this.title.htmlElement);
    }

    /**
     * 
     * @param {HeadElement} element 
     */
    addElement (element) {
        this.elements.push(element);
        document.head.appendChild(element.htmlElement);
    }

    removeElement (element) {
        this.elements = this.elements.filter(item => item !== element);
        element.htmlElement.remove();
    }

    getElementByUuid (uuid) {
        if (uuid == "TITLE") {
            return this.title;
        }
        const elem = this.elements.find(el => el.uuid === uuid);
        return elem;
    }
}