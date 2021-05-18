/*jshint esversion: 6 */

import {
    html,
    render
} from './lit-html.js';

(function () {
    class SimpleGet extends HTMLElement {
        constructor() {
            super();

            // Pull in the JSON GET boilerplate from the Fence code.
            // Nee to make sure to centralize the component work in geocomponents.org
            // How to do this locally?

            const resID = this.getAttribute('res-id');

            // CAUTION DEV / DEMO HACK..  comment out in production!!!!!!
            // var newstr = resID.replace(/opencoredata.org/i, 'localhost:9900');
            var newstr = resID;
            // console.log(newstr);

            // GET test
            function tj_providers(id) {
                return fetch(id, {
                    // headers: { 'Accept': 'application/ld+json', },
                })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (myJson) {
                        console.log("=== fdp viewer ===")
                        console.log(myJson);
                        // console.log(JSON.stringify(myJson));
                        // return JSON.stringify(myJson);
                        return myJson;
                    });
            }

            // GET test call...
            tj_providers(newstr).then((feature) => {
                this.attachShadow({ mode: 'open' });

                var  count = Object.keys(feature.resources).length;
                const detailsTemplate = [];


                // Some names get long..  for better layout 
                // truncate them if they are long.  Say > 30 characters
             

                var i;
                for (i = 0; i < count; i++) {
                    var shortname = truncate((feature.resources[i].name), "30", "[...]");
                    detailsTemplate.push( html`<div>
                    <a href="${feature.resources[i].path}" download="${shortname}"> 
                    <img src="/common/images/download.svg" height="15px">
                    </a>

                    <a target="_blank"
                    href="${feature.resources[i].path}">${shortname}</a>  
                    </div>`);
                }

                var h = html`<div style="margin-top:10px">
                <span>${feature.title}</span><br>
                ${detailsTemplate}</div>`;
                // this.shadowRoot.innerHTML = `${h}`;
                render(h, this.shadowRoot);

            });
        }
    }
    window.customElements.define('fcore-fdpviewer', SimpleGet);
})();

var truncate = function (fullStr, strLen, separator) {
    if (fullStr.length <= strLen) return fullStr;

    separator = separator || '...';

    var sepLen = separator.length,
        charsToShow = strLen - sepLen,
        frontChars = Math.ceil(charsToShow/2),
        backChars = Math.floor(charsToShow/2);

    return fullStr.substr(0, frontChars) + 
           separator + 
           fullStr.substr(fullStr.length - backChars);
};