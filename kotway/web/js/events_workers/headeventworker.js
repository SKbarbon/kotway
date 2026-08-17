import {HEAD_ELEMS_FACTORY} from "../core/head/headelementsfactory.js"


export class HeadEventWorker {
    constructor (page, eventData) {
        this.page = page;
        const eventName = eventData.event_name;
        const data = eventData.data;

        if (eventName == "add_elem") {
            const requestedElemName = data.element_name;
            const providedElemUuid = data.element_uuid;

            const headElement = new HEAD_ELEMS_FACTORY[requestedElemName]();
            headElement.uuid = providedElemUuid;

            this.page.head.addElement(headElement);
            console.log("Added head element: " + requestedElemName);
        }
        else if (eventName == "update_elem") {
            const providedElemUuid = data.element_uuid;
            const selectedElement = page.head.getElementByUuid(providedElemUuid);

            this.updateElementProperties(selectedElement, data.props);
        }

        else if (eventName == "remove_elem") {
            const providedElemUuid = data.element_uuid;
            const selectedElement = page.head.getElementByUuid(providedElemUuid);

            this.page.head.removeElement(selectedElement);
        }
    }

    updateElementProperties (element, props) {
        Object.entries(props).forEach(([key, value]) => {
            element.updateProp(key, value);
        });
    }
}