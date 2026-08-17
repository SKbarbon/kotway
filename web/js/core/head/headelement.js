


export class HeadElement {
    constructor () {
        this.htmlElement = null;
        this.uuid = null;
    }

    /**
     * Update the props of the element.
     * @param {string} propName 
     * @param {string} propValue 
     */
    updateProp (propName, propValue) {
        this.htmlElement[propName] = propValue;
    }
}