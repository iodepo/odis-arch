import {
	html,
	render
} from '/js/lit-html.js';
import { getSafe } from '/js/geodexv2/getSafe.js';
import { truncate } from '/js/geodexv2/truncate.js';
import { rrtoolask } from '/js/geodexv2/rr_toolask.js';


// lithtml render function
export const rrshowresults = (content) => {
	console.log("-----------------------------------------------");
	console.log(content);

    var gar = String(content).split(":");
    console.log(gar);

    var x = `https://dx.geodex.org/?o=/${gar[gar.length -2]}/${gar[gar.length -1]}.jsonld`;
    
    var sptxt = (html`<a target="_blank" href=${x}><img width="30px" src="/img/discover.svg"></a>`);

	return html`
	<div style="margin:3px">
	   ${sptxt}
    </div>
	`;
};
