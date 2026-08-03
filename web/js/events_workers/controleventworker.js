import { CONTROLS_FACTORY } from "../controls/controls_factory.js";


export class ControlEventWorker {
    constructor (ev, page, skip_event_checking=false) {
        this.page = page;
        this.selectedControl = page.getControlByUuid(ev.control_uuid);
        
        if (skip_event_checking==true) {return;}
        if (ev.event_name == "update_props") {
            this.updateControlProps(ev.data)
        }
        else if (ev.event_name == "add_child") {
            this.addChildToParentControl(ev.data);
        }
    }

    updateControlProps (eventData) {
        Object.entries(eventData.props.prop).forEach(([key, value]) => {
            this.selectedControl.updateProp("prop", key, value);
        });

        Object.entries(eventData.props.style).forEach(([key, value]) => {
            this.selectedControl.updateProp("style", key, value);
        });
    }

    addChildToParentControl (eventData) {
        const controlName = eventData.control_name;
        const controlUuid = eventData.control_uuid;
        const slot = eventData.slot;
        
        if (controlName in CONTROLS_FACTORY == false) {
            console.error(`Control not found: '${controlName}'. Can't add to Parent.`);
        }
        const newControl = new CONTROLS_FACTORY[controlName]();
        newControl.uuid = controlUuid;
        this.selectedControl.addControl(newControl);

        const cew = new ControlEventWorker(eventData, this.page, true);
        cew.selectedControl = newControl;
        cew.updateControlProps(eventData);
    }
}