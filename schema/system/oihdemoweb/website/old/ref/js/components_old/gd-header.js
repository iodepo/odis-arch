/*jshint esversion: 6 */
import {
    html,
    render
} from './lit-html.js';

(function () {
    class GeoHeader extends HTMLElement {
        constructor() {
            super();

            var obj;
            var inputs = document.getElementsByTagName('script');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].type.toLowerCase() == 'application/ld+json') {
                    obj = JSON.parse(inputs[i].innerHTML);
                }
            }
            
            const detailsTemplate = [];

            detailsTemplate.push( html`<div style="overflow-wrap: break-word;width=100%">`);


            if (obj.name == undefined)
            detailsTemplate.push( html`<h3> Can not find proper name for this object </h3>`);
            else detailsTemplate.push( html`<h3> ${obj.name} </h3>`);

            if (obj["csdco:expedition"] == undefined)
            detailsTemplate.push( html` `);  // add nothing
            else detailsTemplate.push( html`<h4> ${obj["csdco:expedition"]} </h4>`);

            detailsTemplate.push( html`</div>`);


            //  still need  <span> Distribution org, </span>  <span> Release Date, </span>
            this.attachShadow({ mode: 'open' });
            // this.shadowRoot.innerHTML = `
            //         <div style="overflow-wrap: break-word;width=100%">
            //        <h3>${obj.name}    (${obj["csdco:expedition"]}) </h3>,
                   
            //         </div>
            //           `;

            render(detailsTemplate, this.shadowRoot);



        }
    }
    window.customElements.define('geodex-header', GeoHeader);
})();
