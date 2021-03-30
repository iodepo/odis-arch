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
        //    var endpoint = resID.replace(/opencoredata.org/i, 'localhost:9900');
        var endpoint = resID;

            // GET test
            function tj_providers(id) {
                return fetch(id, {
                    headers: { 'Content-Type': 'application/ld+json', },
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
            tj_providers(endpoint).then((feature) => {
                this.attachShadow({ mode: 'open' });

                // CAUTION DEV / DEMO HACK..  comment out in production!!!!!!
                var newid = feature["@id"].replace(/http:\/\/opencoredata.org\/id\/do/i, '.');

                this.shadowRoot.innerHTML = `
                <div style="overflow-wrap: break-word;width=100%">
                    <a href="${newid}">
                    ${feature["Hole ID"]}</a>
                    (IGSN: <a href="http://sesar.org/${feature["IGSN"]}">
                    ${feature["IGSN"]}<a/>
                    )
                   (${feature["Date"]}) <br>
                   PI(s): ${feature["PI"]}

                    <table style="margin-top:15px;margin-bottom:15px;border:1px solid #333;">              
                   <tr>
                   <td>Water Depth(m)</td><td style="border-right: thin solid;border-left: thin solid; border-top: thin solid; border-bottom: thin solid;text-align: center;">${feature["Water depth"]} </td>
                    </tr>
                    <tr>
                    <td>Elevation (m)</td><td style="border-right: thin solid;border-left: thin solid; border-top: thin solid; border-bottom: thin solid;text-align: center;">${feature["Elevation"]}</td>
                    </tr>
                    <tr>
                    <td>Depth Top (m)</td> <td style="border-right: thin solid;border-left: thin solid; border-top: thin solid; border-bottom: thin solid;text-align: center;">${feature["MBLF top"]}</td>
                    </tr>
                    <tr>
                    <td>Depth Bottom (m)</td> <td style="border-right: thin solid;border-left: thin solid; border-top: thin solid; border-bottom: thin solid;text-align: center;">${feature["MBLF bottom"]}</td>
                    </tr>
                    </table>


                     ${feature["Country"]} ,
                     ${feature["County Region"]} ,
                     ${feature["Location"]}
                     <br>
                     <a target="_blank" href="https://www.google.com/maps/search/?api=1&zoom=4&basemap=terrain&query=${feature["Lat"]},${feature["Long"]}">
                     (lat:  ${feature["Lat"]}
                      long:  ${feature["Long"]}
                    )
                    </a>
                    <hr>
                </div> `;

            });
        }
    }
    window.customElements.define('geodex-getfeature', SimpleGet);
})();

