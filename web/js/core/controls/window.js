import {ClientEventType} from "../../models/clientevent.js";
import { Control } from "./control.js";

export class Window extends Control {
    constructor (page) {
        super();
        this.uuid = "WINDOW"
        this.page = page;
        this.htmlElement = window;

        this.realtime_size_event_active = false;

        const observer = new ResizeObserver((entries) => {
            for (const entry of entries) {
                // Gives exact content area dimensions post-layout
                const { width, height } = entry.contentRect;
                
                requestAnimationFrame(() => {
                    requestAnimationFrame(() => {
                        if (this.realtime_size_event_active == true) {
                            this._sendWindowSize();
                        }
                    });
                });
            }
        });

        // Observe the root HTML element
        observer.observe(document.documentElement);

        this._setTrigger("exchange_window_size", this.triggerWindowSize.bind(this));
        this._setTrigger("realtime_size_listener", this.setRealtimeSizeListener.bind(this))

        this._sendWindowSize();
    }

    triggerWindowSize () {
        this._sendWindowSize ()
    }

    setRealtimeSizeListener(data) {
        this.realtime_size_event_active = data.state;
    }

    _sendWindowSize () {
        this.onInteractionEvent("resize", "resize", {
            "width": parseFloat(window.innerWidth),
            "height": parseFloat(window.innerHeight)
        });
    }
}