import {ClientEventType} from "../models/clientevent.js";
import { Control } from "./control.js";

export class Window extends Control {
    constructor (page) {
        super();
        this.uuid = "WINDOW"
        this.page = page;
        this.htmlElement = window;

        const observer = new ResizeObserver((entries) => {
            for (const entry of entries) {
                // Gives exact content area dimensions post-layout
                const { width, height } = entry.contentRect;
                
                requestAnimationFrame(() => {
                    requestAnimationFrame(() => {
                        this._sendWindowSize();
                    });
                });
            }
        });

        // Observe the root HTML element
        observer.observe(document.documentElement);

        this._setTrigger("exchange_window_size", this.triggerWindowSize.bind(this))
        this._sendWindowSize();
    }

    triggerWindowSize () {
        this._sendWindowSize ()
    }

    _sendWindowSize () {
        this.onInteractionEvent("resize", {
            "width": parseFloat(window.innerWidth),
            "height": parseFloat(window.innerHeight)
        });
    }
}