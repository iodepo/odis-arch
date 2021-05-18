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

            // console.log(obj);
            const detailsTemplate = [];


            if (obj.description == undefined)
            detailsTemplate.push( html`<div> Description: No Description Available  </div>`);
            else detailsTemplate.push( html`<div> Description: ${obj.description} </div>`);


            if (obj.keywords == undefined)
            detailsTemplate.push( html`<div> Keywords: No Keywords Available  </div>`);
            else detailsTemplate.push( html`<div> Keywords: ${obj.keywords} </div>`);

            if (obj.license == undefined)
            detailsTemplate.push( html`<div> License: No License Noted  </div>`);
            else detailsTemplate.push( html`<div> License: ${obj.license} </div>`);

            if (obj.name == undefined)
            detailsTemplate.push( html`<div> Name: No Name Available  </div>`);
            else detailsTemplate.push( html`<div> Name: ${obj.name} </div>`);

            // if (obj.url == undefined)
            // detailsTemplate.push( html`<div> Metadata URL: No URL Available For the Metadata </div>`);
            // else detailsTemplate.push( html`<div> Metadata object: 
            // <a target="_blank" href="${obj.url}">${obj.url}</a> </div>`);

            if (obj.distribution == undefined)
            detailsTemplate.push( html`<div> Distribution URL: No URL Available For the Distribution </div>`);
            else detailsTemplate.push( html`<div> Digital object:
            <a target="_blank" href="${obj.distribution.contentUrl}">${obj.distribution.contentUrl}</a> </div>`);

            this.attachShadow({ mode: 'open' });
            render(detailsTemplate, this.shadowRoot);

        }
    }
    window.customElements.define('geodex-schemadorg', SchemaDOrg);
})();
