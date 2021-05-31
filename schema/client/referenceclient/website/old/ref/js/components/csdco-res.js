/*jshint esversion: 6 */
import {
    html,
    render
} from './lit-html.js';
import './jsonld.min.js';

(function () {
    class SchemaDOrg extends HTMLElement {
        constructor() {
            super();

            // A place holder context 
            const context = {
                "url": { "@id": "https://schema.org/url", "@type": "@id" },
                "image": { "@id": "https://schema.org/image", "@type": "@id" }
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

            // const compacted = jsonld.compact(obj, context).then(sC, fC);
            const compacted = jsonld.compact(obj, context).then((providers) => {
                var j = JSON.stringify(providers, null, 2);
                var jp = JSON.parse(j);

                var t = (jp["@type"]);

                // look for Borehole and ResearchProject
                console.log(t);

                var dt;

                if (t.includes("Borehole")) {
                    console.log("found a Borehole");
                    dt = typeBorehole(jp);
                } else if (t.includes("ResearchProject")) {
                    console.log("found a Project");
                    dt = typeProj(jp);
                } else {
                    console.log("found nothing");
                }

                this.attachShadow({ mode: 'open' });
                render(dt, this.shadowRoot);

            });


            function typeBorehole(obj) {
                console.log(obj);
                const detailsTemplate = [];

                detailsTemplate.push(html`<h3>Borehole metadata</h3>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/IGSN"] == undefined)
                    detailsTemplate.push(html`<div>No IGSN available  </div>`);
                else detailsTemplate.push(html`<div>IGSN:  ${obj["https://opencoredata.org/voc/csdco/v1/IGSN"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/comment"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Comment:  ${obj["https://opencoredata.org/voc/csdco/v1/comment"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/country"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Country:  ${obj["https://opencoredata.org/voc/csdco/v1/country"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/county_Region"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>County / Region: ${obj["https://opencoredata.org/voc/csdco/v1/county_Region"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/date"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Date: ${obj["https://opencoredata.org/voc/csdco/v1/date"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/dip"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Dip: ${obj["https://opencoredata.org/voc/csdco/v1/dip"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/azimuth"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Azimuth: ${obj["https://opencoredata.org/voc/csdco/v1/azimuth"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/elevation"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Elevation: ${obj["https://opencoredata.org/voc/csdco/v1/elevation"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/expedition"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Expedition: ${obj["https://opencoredata.org/voc/csdco/v1/expedition"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/hole"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Hole: ${obj["https://opencoredata.org/voc/csdco/v1/hole"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/hole_ID"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Hole ID: ${obj["https://opencoredata.org/voc/csdco/v1/hole_ID"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/location"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Location: ${obj["https://opencoredata.org/voc/csdco/v1/location"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/location_ID"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Location ID: ${obj["https://opencoredata.org/voc/csdco/v1/location_ID"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/location_Type"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Location Type: ${obj["https://opencoredata.org/voc/csdco/v1/location_Type"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/mblf_B"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>mblf_B: ${obj["https://opencoredata.org/voc/csdco/v1/mblf_B"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/mblf_T"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>mblf_T: ${obj["https://opencoredata.org/voc/csdco/v1/mblf_T"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/metadata_Source"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Metadata Source: ${obj["https://opencoredata.org/voc/csdco/v1/metadata_Source"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/original_ID"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Original ID: ${obj["https://opencoredata.org/voc/csdco/v1/original_ID"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/pi"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>PI: ${obj["https://opencoredata.org/voc/csdco/v1/pi"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/platform"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Platofrm: ${obj["https://opencoredata.org/voc/csdco/v1/platform"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/platform_name"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Platform Name: ${obj["https://opencoredata.org/voc/csdco/v1/platform_name"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/platform_type"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Platform Type: ${obj["https://opencoredata.org/voc/csdco/v1/platform_type"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/position"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Position: ${obj["https://opencoredata.org/voc/csdco/v1/position"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/sample_Type"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Sample Type: ${obj["https://opencoredata.org/voc/csdco/v1/sample_Type"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/site"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Site: ${obj["https://opencoredata.org/voc/csdco/v1/site"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/siteHole"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Site Hole: ${obj["https://opencoredata.org/voc/csdco/v1/siteHole"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/state_Province"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>State Province: ${obj["https://opencoredata.org/voc/csdco/v1/state_Province"]} </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/water_Depth"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Water Depth: ${obj["https://opencoredata.org/voc/csdco/v1/water_Depth"]} </div>`);

                if (obj["https://schema.org/about"] == undefined)
                    detailsTemplate.push(html`<div>Item not present</div>`);
                else detailsTemplate.push(html`<div>Related to: ${obj["https://schema.org/about"]} </div>`);

                return detailsTemplate;
            }


            function typeProj(obj) {
                console.log(obj);
                const detailsTemplate = [];

                if (obj["https://schema.org/name"] == undefined)
                    detailsTemplate.push(html`<div>No Name Available  </div>`);
                else detailsTemplate.push(html`<div><h3>${obj["https://schema.org/name"]} </h3></div>`);


                if (obj["https://schema.org/description"] == undefined)
                    detailsTemplate.push(html`<div> No Description Available  </div>`);
                else detailsTemplate.push(html`<div style="margin-top:lem"><h4>About</h4><p>${obj["https://schema.org/description"]}</p> </div>`);


                detailsTemplate.push(html`<div> <h4>Other Details</h4> </div>`);

                if (obj["https://opencoredata.org/voc/csdco/v1/discipline"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Discipline: ${obj["https://opencoredata.org/voc/csdco/v1/discipline"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/expedition"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Expedition: ${obj["https://opencoredata.org/voc/csdco/v1/expedition"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/funding"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Funding Source: ${obj["https://opencoredata.org/voc/csdco/v1/funding"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/investigators"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Investigators: ${obj["https://opencoredata.org/voc/csdco/v1/investigators"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/lab"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Lab: ${obj["https://opencoredata.org/voc/csdco/v1/lab"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/outreach"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> OutReach: ${obj["https://opencoredata.org/voc/csdco/v1/outreach"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/repository"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Repository: ${obj["https://opencoredata.org/voc/csdco/v1/repository"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/startdate"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Start Date: ${obj["https://opencoredata.org/voc/csdco/v1/startdate"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/status"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Status: ${obj["https://opencoredata.org/voc/csdco/v1/status"]}</div>`);
                }
                if (obj["https://opencoredata.org/voc/csdco/v1/technique"] != undefined) {
                    detailsTemplate.push(html`<div style="margin-top:lem"> Technique: ${obj["https://opencoredata.org/voc/csdco/v1/technique"]}</div>`);
                }


                if (obj.keywords == undefined)
                    detailsTemplate.push(html`<div> Keywords: No Keywords Available  </div>`);
                else detailsTemplate.push(html`<div style="margin-top:lem"> Keywords: ${obj["https://schema.org/keywords"]} </div>`);

                if (obj.license == undefined)
                    detailsTemplate.push(html`<div> License: No License Noted  </div>`);
                else detailsTemplate.push(html`<div style="margin-top:lem"> License: ${obj["https://schema.org/license"]} </div>`);


                // if (obj.url == undefined)
                // detailsTemplate.push( html`<div> Metadata URL: No URL Available For the Metadata </div>`);
                // else detailsTemplate.push( html`<div> Metadata object:
                // <a target="_blank" href="${obj.url}">${obj.url}</a> </div>`);

                // if (obj.distribution == undefined)
                // detailsTemplate.push( html`<div> Distribution URL: No URL Available For the Distribution </div>`);
                // else detailsTemplate.push( html`<div> Digital object:
                // <a target="_blank" href="${obj.distribution.contentUrl}">${obj.distribution.contentUrl}</a> </div>`);

                // this.attachShadow({ mode: 'open' });
                // render(detailsTemplate, this.shadowRoot);

                return detailsTemplate;
            }

        }
    }
    window.customElements.define('csdco-res', SchemaDOrg);
})();
