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


            (async () => {

                const detailsTemplate = [];

                var url = new URL("https://graph.geodex.org/blazegraph/namespace/cdf/sparql"),

                    // var url = new URL("https://192.168.2.89:8080/blazegraph/sparql"),
                    // params = { query: "SELECT * { ?s ?p ?o  } LIMIT 11" }

                    params = {
                        query: ` prefix schema: <http://schema.org/> \
        SELECT ?subj ?disurl ?score  ?name ?description \
         WHERE { \
           ?lit bds:search \"ocean\" . \
           ?lit bds:matchAllTerms "false" . \
           ?lit bds:relevance ?score . \
           ?subj ?p ?lit . \
           BIND (?subj as ?s) \
              {  \
                   SELECT  ?s (MIN(?url) as ?disurl) { \
                     ?s a schema:Dataset . \
                     ?s schema:distribution ?dis . \
                       ?dis schema:url ?url . \
                     } GROUP BY ?s \
           } \
           ?s schema:name ?name . \
           ?s schema:description ?description .  \
         } \
        ORDER BY DESC(?score)
        LIMIT 10
        OFFSET 0
        ` }

                Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

                console.log(params["query"]);

                const rawResponse = await fetch(url, {
                    method: 'GET',
                    //mode: 'no-cors', // no-cors, *cors, same-origin
                    // cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                    //credentials: 'omit', // include, *same-origin, omit
                    headers: {
                        'Accept': 'application/sparql-results+json',
                        'Content-Type': 'application/json'
                    } // ,
                    // body: JSON.stringify({ query: 'SELECT * { ?s ?p ?o  } LIMIT 1', format: 'json' })
                });

                const content = await rawResponse.json();
                // console.log(content);

                var r = content.results.bindings;

//                r.forEach(element => {
//                    detailsTemplate.push(html`<div> Test : ${element.disurl.value} </div>`);
//                    detailsTemplate.push(html`<div> Test : ${element.name.value} </div>`);
//                }
//                );
                //

                r.forEach(element => {
                detailsTemplate.push(html`<sl-card class="card-footer" style="margin:3px;max-width: 290px;"> \
                        ${element.name.value}  \
                        <div slot="footer"> \
                        <sl-button type="primary" pill> \
                        <a target="_blank" href="${element.disurl.value}">View</a> \
                        </sl-button> </div> </sl-card>`);
                }
                );




                this.attachShadow({ mode: 'open' });
                render(detailsTemplate, this.shadowRoot);

            })();

        }
    }
    window.customElements.define('fc-sparql', FCTest);
})();


