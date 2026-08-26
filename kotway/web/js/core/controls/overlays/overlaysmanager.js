import { ParentControl } from "../parentcontrol.js";


export class OverlaysManager extends ParentControl {
    constructor (page) {
        super();
        this.page = page;
        this.uuid = "OVERLAYS_MANAGER";
    }

    updateProp() {}
    removeProp() {}

    addControl(control) {
        control.page = this.page;
        control.parent = this.parent;

        this.controls.push(control);
    }

    removeControl(control) {
        this.page = null;
        this.parent = null;

        this.controls = this.controls.filter(item => item !== control);
    }
}