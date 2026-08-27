import { ParentControl } from "../parentcontrol.js";


export class PictureInPicture extends ParentControl {
    constructor () {
        super();
        this.htmlElement = document.createElement("div");
        this.pipInstance = null

        this._setTrigger("request_window", this.requestWindowTrigger.bind(this));
        this._setTrigger("close", this.closeTrigger.bind(this));
    }

    requestWindowTrigger (data) {
        // Call requestWindow synchronously within the event stack
        this.pipInstance = window.documentPictureInPicture.requestWindow({
            width: data.width,
            height: data.height
        });

        // Handle the async resolution via .then() instead of await
        this.pipInstance
            .then((pipWindow) => {
                pipWindow.document.body.append(this.htmlElement);
                this.pipInstance = pipWindow
                this.sendIsPresentEvent(true);

                pipWindow.addEventListener('pagehide', (event) => {
                    this.sendIsPresentEvent(false);
                });
            })
            .catch((err) => {
            console.error('Failed to open PiP window:', err);
        });
    }

    closeTrigger () {
        if (this.pipInstance != null) {
            this.pipInstance.close()
            this.sendIsPresentEvent(false);
        }
    }

    sendIsPresentEvent (state) {
        this.onInteractionEvent(
            "isPresented",
            {
                "state": state
            }
        )
    }
}