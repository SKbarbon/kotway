import {HeadElement} from "./headelement.js"


export class Head {
    constructor () {
        this.elements = [];
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
        const elem = this.elements.find(el => el.uuid === uuid);
        return elem;
    }
}