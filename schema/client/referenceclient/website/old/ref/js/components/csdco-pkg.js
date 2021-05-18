/*jshint esversion: 6 */
import {
    html,
    render
} from './lit-html.js';
import './jsonld.min.js';
import { parts } from './lib/render.js';

(function () {
    class FCTest extends HTMLElement {
        constructor() {
            super();

            const context = {
                "url": { "@id": "https://schema.org/url", "@type": "@id" },
                "image": { "@id": "https://schema.org/image", "@type": "@id" }
            };

            var obj;
            var inputs = document.getElementsByTagName('script');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].type.toLowerCase() == 'application/ld+json') {
                    obj = JSON.parse(inputs[i].innerHTML);
                }
            }

            // const compacted = jsonld.compact(obj, context).then(sC, fC);
            const compacted = jsonld.compact(obj, context).then((providers) => {
                var j = JSON.stringify(providers, null, 2);
                var jp = JSON.parse(j);

                console.log(jp);
                console.log(jp["https://schema.org/description"]);

                const detailsTemplate = [];
                detailsTemplate.push(html`<h3>Digital Data Package metadata</h3>`);

                if (jp["https://schema.org/description"] == undefined)
                    detailsTemplate.push(html`<div> No description available  </div>`);
                else detailsTemplate.push(html`<div><h3> ${jp["https://schema.org/description"]} </h3></div>`);

                if (jp["https://schema.org/keywords"] == undefined)
                    detailsTemplate.push(html`<div> No keywords available  </div>`);
                else detailsTemplate.push(html`<div> Keywords: ${jp["https://schema.org/keywords"]} </div>`);

                if (jp["https://schema.org/about"] == undefined)
                    detailsTemplate.push(html`<div> No related project  </div>`);
                else detailsTemplate.push(html`<div> Project relation: <a href='${jp["https://schema.org/about"]}'> ${jp["https://schema.org/about"]}</a> </div>`);

                if (jp["https://schema.org/license"] == undefined)
                    detailsTemplate.push(html`<div> No license Available  </div>`);
                else detailsTemplate.push(html`<div> License: ${jp["https://schema.org/license"]} </div>`);

                if (jp["https://schema.org/url"] == undefined)
                 detailsTemplate.push(html`<div> URL: No document URL available  </div>`);
                else detailsTemplate.push(html`<div> Package URL: <a href='${jp["https://schema.org/url"]}'>${jp["https://schema.org/url"]}</a> </div>`);


                if (jp["https://schema.org/distribution"]["https://schema.org/contentUrl"] == undefined)
                detailsTemplate.push(html`<div> No distribution URL available  </div>`);
               else detailsTemplate.push(html`<div> <a href='${jp["https://schema.org/distribution"]["https://schema.org/contentUrl"]}' download>Download Data Package</a> </div>`);


               if (jp["https://schema.org/hasPart"] == undefined)
               detailsTemplate.push(html`<div> No package documents available  </div>`);
               else {
                detailsTemplate.push(html`<div> Package content links:  </div>`);
                   var p = jp["https://schema.org/hasPart"];
                   p.forEach(element =>
                    detailsTemplate.push(html`<div> Document : <a href='${element["https://schema.org/url"]}'>${element["https://schema.org/url"]}</a> </div>`));
               }

                this.attachShadow({ mode: 'open' });
                render(detailsTemplate, this.shadowRoot);                // var h =  `<div>${itemTemplates}</div>`;
                // this.shadowRoot.appendChild(this.cloneNode(h));

            });
        }
    }
    window.customElements.define('csdco-pkg', FCTest);
})();


