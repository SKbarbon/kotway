import { Control } from "./control.js";


export class Image extends Control {
    constructor () {
        super();
        this.htmlElement = document.createElement("img");
    }
}