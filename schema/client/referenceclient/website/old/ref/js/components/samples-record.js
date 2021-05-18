/*jshint esversion: 6 */
import {
    html,
    render
} from './lit-html.js';

(function () {
    class SchemaDOrg extends HTMLElement {
        constructor() {
            super();

            // need to think about calling jsonld.js and using
            // it to parse the graph
            var obj;
            var inputs = document.getElementsByTagName('script');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].type.toLowerCase() == 'application/ld+json') {
                    obj = JSON.parse(inputs[i].innerHTML);
                }
            }

            console.log("did I find the object?");
            console.log(obj);

            // console.log(obj);
            const TemplateResult = [];

            let myMap = new Map();
            myMap.set("title", "title");
            myMap.set("title id", "http://purl.org/dc/terms/title" );


            for (let [key, value] of myMap) {
                console.log(key + ' : ' + value);
                if (obj[value] == undefined)
                TemplateResult.push( html`<div> ${key}: Not Available  </div>`);
                else TemplateResult.push( html`<div> <span style="color:blue">${key}</span><span style="font-weight:bold"> ${obj[value] }</span> </div>`);
            }



            // if (obj.distribution == undefined)
            // TemplateResult.push( html`<div> Distribution URL: No URL Available For the Distribution </div>`);
            // else TemplateResult.push( html`<div> Digital object:
            // <a target="_blank" href="${obj.distribution.contentUrl}">${obj.distribution.contentUrl}</a> </div>`);

            this.attachShadow({ mode: 'open' });
            render(TemplateResult, this.shadowRoot);

        }
    }
    window.customElements.define('samples-record', SchemaDOrg);
})();
