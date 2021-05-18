/*jshint esversion: 6 */
import {
	html,
	render
} from './lit-html.js';

(function () {
    class SimpleGet extends HTMLElement {
        constructor() {
            super();

            const resID = this.getAttribute('res-id');

            // CAUTION DEV / DEMO HACK..  comment out in production!!!!!!
            // var newstr = resID.replace(/opencoredata.org/i, 'localhost:9900');  // just do . and have it work in both?
            var newstr = resID;
            // console.log(newstr);

            // GET test
            function tj_providers(id) {
                return fetch(id, {
                    headers: { 'Accept': 'application/ld+json', },
                    })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (myJson) {
                        console.log(myJson);
                        // console.log(JSON.stringify(myJson));
                        // return JSON.stringify(myJson);
                        return myJson;
                    });
            }

            // GET test call...
            tj_providers(newstr).then((feature) => {
                this.attachShadow({ mode: 'open' });

                // CAUTION DEV / DEMO HACK..  comment out in production!!!!!!
                // var ns = feature["distribution"].contentUrl.replace(/opencoredata.org/i, '192.168.2.89:9900');
                var ns = feature.distribution.contentUrl; //.replace(/http:\/\/opencoredata.org\//i, '/');

                console.log(ns);

                this.shadowRoot.innerHTML = `
                <div style="margin-top:10px;overflow-wrap: break-word;width=100%">
                    ${feature["description"]}

                    <a href="${ns}"> Dataset Landing Page </a>
                   

                    ( Download as: <a href="${ns}.zip">zip</a>,
                    <a target="_blank" href="${ns}">FDP</a> )
                </div>
                  `;

            });
        }
    }
    window.customElements.define('geodex-getpackage', SimpleGet);
})();


