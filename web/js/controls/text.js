import {Control} from "./control.js";


export class Text extends Control {
    constructor () {
        super();
        this.htmlElement = document.createElement("span");
    }
}