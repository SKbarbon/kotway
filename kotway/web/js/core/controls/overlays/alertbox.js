import { OverlayControl } from "./overlaycontrol.js";


export class AlertBox extends OverlayControl {
    constructor() {
        super();
        this._setTrigger("show_alert", this.showAlert.bind(this));
    }

    showAlert (data) {
        const message = data.message;
        window.alert(message);
    }
}