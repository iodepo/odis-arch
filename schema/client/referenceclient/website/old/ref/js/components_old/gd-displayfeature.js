/*jshint esversion: 6 */

import {
    html,
    render
} from './lit-html.js';


(function () {
    class SimpleGet extends HTMLElement {
        constructor() {
            super();

            var obj;
            var inputs = document.getElementsByTagName('script');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].type.toLowerCase() == 'application/ld+json') {
                    obj = JSON.parse(inputs[i].innerHTML);
                }
            }

            // console.log(inputs);
            console.log("-----  gd-displayfeater");
            console.log(obj);

            // var  count = Object.keys(obj).length;
            const detailsTemplate = [];

            detailsTemplate.push(html`<table>`);
            var item, subitem;
            for (item in obj) {
                // need an if here to remove things with @
                if (!item.includes("@")) {
                    // test obj[item] is a URL  if so do a simple template push to include in
                    // the following template
                    const linkTemplate = [];
                    var oi = obj[item];
                     console.log(oi);
                    if (oi.constructor === String) {
                        console.log("string!");
                        if (oi.includes("http://")) {
                            linkTemplate.push(html`<a href="${obj[item]}>${obj[item]}</a>`);
                        } else {
                            linkTemplate.push(html`${obj[item]}`);
                        }
                    } else {
                        console.log("not a string!");
                        linkTemplate.push(html`${obj[item]}`);
                    }
                    detailsTemplate.push(html`
                <tr>
                     <td>${item}</td><td> ${obj[item]} </td>
                </tr>
                `);
                }
            }

            detailsTemplate.push(html`</table>`);

            var h = html`
                <div style="overflow-wrap: break-word;width=100%">
                    Feature of: <a href="${obj["about"]}">${obj["about"]}</a><br>
                    Feature ID: <a href="${obj["@id"]}">${obj["Hole ID"]}</a><br>
                    PI(s): ${obj["PI"]}<br>
                     ${obj["Country"]} : ${obj["County Region"]} : ${obj["Location"]} <br>
                     <br>
                     <a target="_blank" href="https://www.google.com/maps/search/?api=1&zoom=4&basemap=terrain&query=${obj["Lat"]},${obj["Long"]}">
                     Google Map Link (lat:  ${obj["Lat"]}  long:  ${obj["Long"]}) </a>
                
                    <hr>
                      ${detailsTemplate}
                 
                </div> `;

            this.attachShadow({ mode: 'open' });
            render(h, this.shadowRoot);
        }

    }
    window.customElements.define('geodex-displayfeature', SimpleGet);
})();

