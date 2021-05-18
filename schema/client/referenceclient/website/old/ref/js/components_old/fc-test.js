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
                "This is Foo": "http://opencoredata.org/voc/csdco/1/foo",
                "name": "http://schema.org/name",
                "homepage": { "@id": "http://schema.org/url", "@type": "@id" },
                "image": { "@id": "http://schema.org/image", "@type": "@id" }
            };


            // need to think about calling jsonld.js and using
            // it to parse the graph
            var obj;
            var inputs = document.getElementsByTagName('script');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].type.toLowerCase() == 'application/ld+json') {
                    obj = JSON.parse(inputs[i].innerHTML);
                }
            }

            console.log(obj);
            var j;
            jsonld.compact(obj, context, function (err, compacted) {
                j = JSON.stringify(compacted, null, 2);
                console.log(j);
                console.log(JSON.parse(j));
            });


            var jp = JSON.parse(j);
            // console.log(obj);
            const detailsTemplate = [];
            detailsTemplate.push(html`<p>Detail test push </p>`);

            if (jp["homepage"] == undefined)
                detailsTemplate.push(html`<div> Homepage: not set  </div>`);
            else detailsTemplate.push(html`<div> Homepage: ${jp["homepage"]} </div>`);

            this.attachShadow({ mode: 'open' });
            render(detailsTemplate, this.shadowRoot);

        }
    }
    window.customElements.define('fc-test', FCTest);
})();

