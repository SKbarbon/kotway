import { Control } from "./control.js";


export class IFrame extends Control {
    constructor () {
        super();
        this.htmlElement = document.createElement("iframe");

        this._setTrigger("modify_sandbox_tokens", this.modifySandboxTokens.bind(this));
        this._setTrigger("modify_allow_policies", this.modifyAllowPolicies.bind(this));
    }

    /**
     * A trigger handler for "modify_sandbox_tokens"
     * @param {Array} data 
     */
    modifySandboxTokens (data) {
        const token = data.token;
        if (data.action == "add") {
            this.htmlElement.sandbox.add(token);
        }
        else if (data.action == "remove") {
            this.htmlElement.sandbox.remove(token);
        }
    }

    /**
     * A trigger handler for 'modify_allow_policies'
     * @param {Array} data 
     */
    modifyAllowPolicies (data) {
        const policy = data.policy;
        if (data.action == "add") {
            this._appendAllowPolicy(policy)
        }
        else if (data.action == "remove") {
            this._removeAllowPolicy(policy);
        }
    }

    _appendAllowPolicy(policy) {
        const current = this.htmlElement.getAttribute('allow') || '';
        const cleanCurrent = current.trim().replace(/;$/, '');
        
        this.htmlElement.setAttribute(
            'allow', 
            cleanCurrent ? `${cleanCurrent}; ${policy}` : policy
        );
    }

    _removeAllowPolicy(policyToRemove) {
        const current = this.htmlElement.getAttribute('allow') || '';
        if (!current) return;

        // Split into individual policy directives, filter out the target, and rejoin
        const updated = current
            .split(';')
            .map(p => p.trim())
            .filter(p => p && !p.startsWith(policyToRemove))
            .join('; ');

        this.htmlElement.setAttribute('allow', updated);
    }
}