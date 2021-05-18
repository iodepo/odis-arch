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
                "url": { "@id": "http://schema.org/url", "@type": "@id" },
                "image": { "@id": "http://schema.org/image", "@type": "@id" }
            };

            var obj;
            //var inputs = document.getElementsByTagName('script');
            /*for (var i = 0; i < inputs.length; i++) {*/
                //if (inputs[i].type.toLowerCase() == 'application/ld+json') {
                    //obj = JSON.parse(inputs[i].innerHTML);
                //}
            /*}*/

            // read object from URL
            fetch('https://raw.githubusercontent.com/IGSN/igsn-json/master/schema.igsn.org/json/registration/v0.1/context.jsonld')
                .then(res => res.json())
                .then(data => obj = data)
                .then(() => console.log(obj))

            console.log(obj)

            // const compacted = jsonld.compact(obj, context).then(sC, fC);
            const compacted = jsonld.compact(obj, context).then((providers) => {
                var j = JSON.stringify(providers, null, 2);
                var jp = JSON.parse(j);

                // console.log(jp);
                // console.log(jp["@graph"][1]["http://schema.org/description"]);
                // Description: No Description Available
                // Keywords: No Keywords Available
                // License: No License Noted
                // Name: No Name Available
                // Distribution URL: No URL Available For the Distribution

                const detailsTemplate = [];
                detailsTemplate.push(html`<h3>Digital Document metadata</h3>`);


                //if (jp["@graph"][1]["url"] == undefined)
                 //detailsTemplate.push(html`<div> URL: No document URL available  </div>`);
                //else detailsTemplate.push(html`<div> URL: <a href='${jp["@graph"][1]["url"]}'>${jp["@graph"][1]["url"]}</a> </div>`);


                this.attachShadow({ mode: 'open' });
                render(detailsTemplate, this.shadowRoot);                // var h =  `<div>${itemTemplates}</div>`;
                // this.shadowRoot.appendChild(this.cloneNode(h));

            });

        }
    }
    window.customElements.define('fc-doview', FCTest);
})();


