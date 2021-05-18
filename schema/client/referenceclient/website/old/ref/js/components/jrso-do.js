/*jshint esversion: 6 */
import {
    html,
    render
} from './lit-html.js';
import './jsonld.min.js';

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

                // console.log(jp);
                // console.log(jp["@graph"][1]["https://schema.org/description"]);
                // Description: No Description Available
                // Keywords: No Keywords Available
                // License: No License Noted
                // Name: No Name Available
                // Distribution URL: No URL Available For the Distribution

                const detailsTemplate = [];
                detailsTemplate.push(html`<h3>Digital Document metadata</h3>`);

                if (jp["@graph"][1]["https://schema.org/name"] == undefined)
                    detailsTemplate.push(html`<div> Name: No name available  </div>`);
                else detailsTemplate.push(html`<div> Name: ${jp["@graph"][1]["https://schema.org/name"]} </div>`);

                if (jp["@graph"][1]["https://schema.org/encodingFormat"] == undefined)
                    detailsTemplate.push(html`<div> No encoding format provided </div>`);
                else detailsTemplate.push(html`<div> Encoding format: ${jp["@graph"][1]["https://schema.org/encodingFormat"]} </div>`);

                if (jp["@graph"][1]["https://schema.org/dateCreated"] == undefined)
                    detailsTemplate.push(html`<div> Date Created: No creation date available  </div>`);
                else detailsTemplate.push(html`<div> Date Created: ${jp["@graph"][1]["https://schema.org/dateCreated"]} </div>`);

                if (jp["@graph"][1]["https://schema.org/isRelatedTo"] == undefined)
                    detailsTemplate.push(html`<div> No related project  </div>`);
                else detailsTemplate.push(html`<div> Project relation: <a href='/id/csdco/res/${jp["@graph"][1]["https://schema.org/isRelatedTo"]}'> ${jp["@graph"][1]["https://schema.org/isRelatedTo"]}</a> </div>`);

                if (jp["@graph"][1]["https://schema.org/description"] == undefined)
                    detailsTemplate.push(html`<div> Description: No Description Available  </div>`);
                else detailsTemplate.push(html`<div> Description: ${jp["@graph"][1]["https://schema.org/description"]} </div>`);

                if (jp["@graph"][1]["url"] == undefined)
                 detailsTemplate.push(html`<div> URL: No document URL available  </div>`);
                else detailsTemplate.push(html`<div> URL: <a href='${jp["@graph"][1]["url"]}'>${jp["@graph"][1]["url"]}</a> </div>`);


                this.attachShadow({ mode: 'open' });
                render(detailsTemplate, this.shadowRoot);                // var h =  `<div>${itemTemplates}</div>`;
                // this.shadowRoot.appendChild(this.cloneNode(h));

            });

        }
    }
    window.customElements.define('csdco-do', FCTest);
})();


