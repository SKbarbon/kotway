import {Page} from "./page.js";

export class KotwayApp {
    constructor (adapterTransport) {
        this.page = new Page(adapterTransport)
        this.adapterTransport = adapterTransport
        console.log("Session ID is: " + this.page.getSessionId());
    }

    run () {
        console.debug("kotway app started!");

        this.adapterTransport.page = this.page;
        this.adapterTransport.start();
    }
}