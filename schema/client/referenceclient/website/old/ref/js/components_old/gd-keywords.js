/*jshint esversion: 6 */
import {
    html,
    render
} from './lit-html.js';

(function () {
    class GeoKeywords extends HTMLElement {
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

            if (obj.keywords == undefined) 
            detailsTemplate.push( html`<div> Keywords: No Keywords Available  </div>`);
            else detailsTemplate.push( html`<div> Keywords: ${obj.keywords} </div>`);

            if (obj["csdco:lab"] == undefined) 
            detailsTemplate.push( html`<div> Lab: not set  </div>`);
            else detailsTemplate.push( html`<div> Lab: ${obj["csdco:lab"]} </div>`);

            if (obj["csdco:discipline"] == undefined) 
            detailsTemplate.push( html`<div> Discipline: net set  </div>`);
            else detailsTemplate.push( html`<div> Discipline: ${obj["csdco:discipline"]} </div>`);

            if (obj["csdco:startdate"] == undefined) 
            detailsTemplate.push( html`<div> Start Date: net set  </div>`);
            else detailsTemplate.push( html`<div> Start Date: ${obj["csdco:startdate"]} </div>`);

            if (obj["csdco:status"] == undefined) 
            detailsTemplate.push( html`<div> Status: net set  </div>`);
            else detailsTemplate.push( html`<div> Status: ${obj["csdco:status"]} </div>`);

            if (obj["csdco:funding"] == undefined) 
            detailsTemplate.push( html`<div> Funding: net set  </div>`);
            else detailsTemplate.push( html`<div> Funding: ${obj["csdco:funding"]} </div>`);

            if (obj["csdco:repository"] == undefined) 
            detailsTemplate.push( html`<div> Repository: net set  </div>`);
            else detailsTemplate.push( html`<div>Repository: ${obj["csdco:repository"]} </div>`);

            if (obj["csdco:technique"] == undefined) 
            detailsTemplate.push( html`<div> Technique: net set  </div>`);
            else detailsTemplate.push( html`<div> Technique: ${obj["csdco:technique"]} </div>`);

            this.attachShadow({ mode: 'open' });
            render(detailsTemplate, this.shadowRoot);

        }
    }
    window.customElements.define('geodex-keywords', GeoKeywords);
})();
