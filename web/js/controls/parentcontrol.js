import { Control } from "./control.js";


export class ParentControl extends Control {
    constructor () {
        super();

        this.controls = [];
    }

    addControl (control) {
        control.page = this.page;
        control.view = this.view;
        control.parent = this;

        this.controls.push(control);

        this.htmlElement.append(control.htmlElement);
    }

    removeControl (control, wrapperElement) {
        control.view = null;
        control.page = null;
        control.parent = null;

        this.controls = this.controls.filter(item => item !== control);
        control.htmlElement.remove();
    }
}