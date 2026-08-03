import { View } from "../controls/view.js";
import {Text} from "../controls/text.js";

export class FatalErrorMessageView extends View {
    constructor (errorMessage) {
        super()
        this.route = "/error"

        this.htmlElement.style.setProperty("display", "grid");
        this.htmlElement.style.setProperty("min-height", "100vh")
        this.htmlElement.style.setProperty("place-items", "center");
        
        const errorLabel = new Text();
        errorLabel.htmlElement["textContent"] = "Error: " + errorMessage;
        this.addControl(errorLabel);
    }
}