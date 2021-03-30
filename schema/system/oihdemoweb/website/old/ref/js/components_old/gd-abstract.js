/*jshint esversion: 6 */

(function () {
    class GeoAbstract extends HTMLElement {
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

            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
            var yyyy = today.getFullYear();

            today = mm + '/' + dd + '/' + yyyy;

            // var version = 'Not Provided'; // override if set by the SDO

            // TODO check for no abstract and note that

            // TODO If abstract is long use the details elements
            var abstract = obj["csdco:abstract"];
            var ablen = abstract.length;

            this.attachShadow({ mode: 'open' });

            if (ablen > 1250 ) {
                var summary = abstract.substring(0,1000);
                var restof = abstract.substring(1000);
                this.shadowRoot.innerHTML = `
                <div style="overflow-wrap: break-word;width=100%">
                <details><summary>${summary}</summary>  <p>${restof} </p></details>
                </div>
                  `;
            } else {
                this.shadowRoot.innerHTML = `
                <div style="overflow-wrap: break-word;width=100%">
                   <p> ${obj["csdco:abstract"]} </p>
                </div>
                  `;
            }
    
        }
    }
    window.customElements.define('geodex-abstract', GeoAbstract);
})();
