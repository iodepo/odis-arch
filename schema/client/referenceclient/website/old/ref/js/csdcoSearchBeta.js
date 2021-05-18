/* jshint esversion: 6 */
import {
	html,
	render
} from './lit-html.js';

// event listeners
document.querySelector('#q').addEventListener('keyup', function (e) {
	if (e.keyCode === 13) {
		searchActions();
	}
});

document.querySelector('#update').addEventListener('click', searchActions);

document.addEventListener('readystatechange', () => {
	if (document.readyState == 'complete') stateChangeSearch();
});

// popstate for nav buttons
window.onpopstate = event => {
	stateChangeSearch();
};

function stateChangeSearch() {

	var q = getAllUrlParams().q;
	if (q == null) {
		q = "";
	}
	// set the search then
	let qdo = document.querySelector('#q');
	qdo.value = q;

	var n = getAllUrlParams().n;
	if (n == null) {
		n = 20;
	}

	var o = getAllUrlParams().o;
	if (o == null) {
		o = 0;
	}
	console.log(o);

	// TODO if we nav back to NULL..   we need to clear the result DOM
	// otherwise we still see the last none NULL search results
	if (q != null && q != "") {
		blazefulltext(q, n, o);
	}
	updateURL(q, n, o);

	const navel = document.querySelector('#container1');
	render(navstatus(q, n, o), navel);

}

// rename to clickSearch  (needs updated elsewhere to do that)
function searchActions() {
	// let params = (new URL(location)).searchParams;
	let q = document.querySelector('#q').value;
	let n = document.querySelector('#nn').value;

	var o = getAllUrlParams().o;
	if (o == null) {
		o = 0;
	}
	console.log(o);

	blazefulltext(q, n, o);
	updateURL(q, n, o);

	const navel = document.querySelector('#container1');
	render(navstatus(q, n, o), navel);

	// navstatus();   // update the paging UI
}

function navstatus(q, n, o) {
	const itemTemplates = [];

	// itemTemplates.push(html`<p>Number: ${n} Offset: ${o}</p>`);
	var oi = parseInt(o, 10);
	var ni = parseInt(n, 10);

	var onext = oi + ni; // use unary plus operator to add strings by converting to numbers
	var oprev = onext - (2*ni);

	console.log(oi);
	console.log(ni);
	console.log(onext);
	console.log(oprev);

	// step up and step down o
	itemTemplates.push(html`<a href="/search.html?q=${q}&n=${n}&o=0"><img style="height:35px" src="./img/rewind.svg">   </a>`);

	if (oprev >= ni ) {
		itemTemplates.push(html`<a href="/search.html?q=${q}&n=${n}&o=${oprev}"> <img style="height:35px" src="./img/back.svg"> </a>`);
	}

	itemTemplates.push(html`<a href="/search.html?q=${q}&n=${n}&o=${onext}"> <img style="height:35px" src="./img/forward.svg"> </a>`);

	return html`
	<div style="margin-top:5px">
	   ${itemTemplates}
    </div>
	`;

}

function updateURL(q, n, o) {
	// let qdo = document.querySelector('#q');
	// let ndo = document.querySelector('#n');
	// let sdo = document.querySelector('#s');
	// let ido = document.querySelector('#i');

	let params = new URLSearchParams(location.search.slice(1));
	params.set('q', q);
	params.set('n', n);
	params.set('o', o);
	// params.set('i', ido.value);


	// Issues with current browsers and titles
	document.title = `Search:${q}&n=${n}&o=${o}`;

	//window.history.replaceState({}, '', location.pathname + '?' + params);
	const state = {
		q: q,
		n: n,
		o: o
	}
	window.history.pushState({}, '', location.pathname + '?' + params);
}

function blazefulltext(q, n, o) {
	console.log(n);


	(async () => {

		var url = new URL("https://graph.samples.earth/blazegraph/namespace/samplesearth/sparql"),

			// var url = new URL("http://192.168.2.89:8080/blazegraph/sparql"),
			// params = { query: "SELECT * { ?s ?p ?o  } LIMIT 11" }

			params = {
				query: ` prefix schema: <http://schema.org/> \
SELECT ?subj ?p ?score ?name ?relto ?url  ?description \
 WHERE { \
   ?lit bds:search \"${q}\" . \
   ?lit bds:matchAllTerms "false" . \
   ?lit bds:relevance ?score . \
   ?subj ?p ?lit . \
   BIND (?subj as ?s) \
   OPTIONAL {?s schema:name ?name .} \
   OPTIONAL {?s schema:isRelatedTo ?relto .} \
   OPTIONAL {?s schema:url ?url . } \
   OPTIONAL {?s schema:description ?description . } \
 } \
ORDER BY DESC(?score)
LIMIT ${n}
OFFSET ${o}
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
		//console.log(content);

		const el = document.querySelector('#container2');
		const s1 = document.querySelector('#side1');
		render(showresults(content), el);
		render(projresults(content), s1);

	})();
}

function getSafe(fn) {
	try {
		return fn();
	} catch (e) {
		return undefined;
	}
}

function truncate(n, useWordBoundary) {
	if (this.length <= n) { return this; }
	var subString = this.substr(0, n - 1);
	return (useWordBoundary
		? subString.substr(0, subString.lastIndexOf(' '))
		: subString) + "...";
};

// lit-html constant
//  SELECT ?subj  ?p ?score  ?type  ?name ?relto ?addtype ?url  ?description \
const showresults = (content) => {
	console.log("-----------------------------------------------")
	console.log(content)

	var barval = content.results.bindings
	var count = Object.keys(barval).length;
	const itemTemplates = [];

	itemTemplates.push(html`<p>Data Files</p>`);

	for (var i = 0; i < count; i++) {
		// console.log("-in  data files loop ---")

		// if (getSafe(() => barval[i].type.value)) {
		itemTemplates.push(html`<div style="margin-top:30px">`);

		if (getSafe(() => barval[i].relto.value)) {
			itemTemplates.push(html`<div>See project:
					<a target="_blank" href="/id/do/${barval[i].relto.value}">${barval[i].relto.value}</a> </div>`);
		}

		if (getSafe(() => barval[i].url.value)) {
			itemTemplates.push(html`<div>Digital Object:
                        <a class="nemo" target="_blank" style="text-decoration: underline dotted blue;color:black" href="${barval[i].url.value}">Link: ${barval[i].url.value}</a> </div>`);
		}
		// console.log(barval[i].url.value)

		if (getSafe(() => barval[i].description.value)) {
			itemTemplates.push(html`<div> Description: ${barval[i].description.value} </div>`);
		}

		if (getSafe(() => barval[i].score.value)) {
			itemTemplates.push(html`<div> score: ${barval[i].score.value} </div>`);
		}
		// }

		itemTemplates.push(html`</div>`);
	}

	return html`
	<div style="margin-top:30px">
	   ${itemTemplates}
    </div>
	`;
};

// lit-html constant
//  SELECT ?subj  ?p ?score  ?type  ?name ?relto ?addtype ?url  ?description \
const projresults = (content) => {

	console.log("-top of Research Project---")

	var barval = content.results.bindings
	var count = Object.keys(barval).length;
	const itemTemplates = [];

	itemTemplates.push(html`<p>Related Projects</p>`);

	for (var i = 0; i < count; i++) {
		console.log("-in loop ---")


		if (getSafe(() => barval[i].type.value)) {
			if (barval[i].type.value == "http://schema.org/ResearchProject") {

				console.log("-Research Project---")

				itemTemplates.push(html`<div style="margin-top:30px">`);

				if (getSafe(() => barval[i].name.value) && getSafe(() => barval[i].url.value)) {
					itemTemplates.push(html`<p> <a href="${barval[i].url.value}">${barval[i].name.value}</a> </p>`);
				}

				if (getSafe(() => barval[i].relto.value)) {
					itemTemplates.push(html`<div> ${barval[i].relto.value} </div>`);
				}

				if (getSafe(() => barval[i].description.value)) {
					var s = barval[i].description.value
					itemTemplates.push(html`<div> Description: ${truncate.apply(s, [100, true])} </div>`);
				}


				if (getSafe(() => barval[i].addtype.value)) {
					itemTemplates.push(html`<div> ${barval[i].addtype.value} </div>`);
				}

				if (getSafe(() => barval[i].score.value)) {
					itemTemplates.push(html`<div> score: ${barval[i].score.value} </div>`);
				}

			}
		}

		itemTemplates.push(html`</div>`);
	}

	return html`
	<div style="margin-top:30px">
	   ${itemTemplates}
    </div>
	`;
};




// function pageLoadSearch() {
// 	console.log("=======================  Window load =======================");
// }



// const OLDshowresults = (content) => {
// 	console.log("-----------------------------------------------")
// 	console.log(content);

// 	return html`<div style="text-align:center;margin-top:50px;position:relative">
// 	<br> Results:  ${content}</div>`;
// }

/*

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
	  method: 'POST', // *GET, POST, PUT, DELETE, etc.
	  mode: 'cors', // no-cors, *cors, same-origin
	  cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
	  credentials: 'same-origin', // include, *same-origin, omit
	  headers: {
		  'Content-Type': 'application/json'
		  // 'Content-Type': 'application/x-www-form-urlencoded',
	  },
	  redirect: 'follow', // manual, *follow, error
	  referrer: 'no-referrer', // no-referrer, *client
	  body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return await response.json(); // parses JSON response into native JavaScript objects
}

try {
  const data = await postData('http://example.com/answer', { answer: 42 });
  console.log(JSON.stringify(data)); // JSON-string from `response.json()` call
} catch (error) {
  console.error(error);
}

*/


function getAllUrlParams(url) {

	// get query string from url (optional) or window
	var queryString = url ? url.split('?')[1] : window.location.search.slice(1);

	// we'll store the parameters here
	var obj = {};

	// if query string exists
	if (queryString) {

		// stuff after # is not part of query string, so get rid of it
		queryString = queryString.split('#')[0];

		// split our query string into its component parts
		var arr = queryString.split('&');

		for (var i = 0; i < arr.length; i++) {
			// separate the keys and the values
			var a = arr[i].split('=');

			// set parameter name and value (use 'true' if empty)
			var paramName = a[0];
			var paramValue = typeof (a[1]) === 'undefined' ? true : a[1];

			// (optional) keep case consistent
			paramName = paramName.toLowerCase();
			if (typeof paramValue === 'string') paramValue = paramValue.toLowerCase();

			// if the paramName ends with square brackets, e.g. colors[] or colors[2]
			if (paramName.match(/\[(\d+)?\]$/)) {

				// create key if it doesn't exist
				var key = paramName.replace(/\[(\d+)?\]/, '');
				if (!obj[key]) obj[key] = [];

				// if it's an indexed array e.g. colors[2]
				if (paramName.match(/\[\d+\]$/)) {
					// get the index value and add the entry at the appropriate position
					var index = /\[(\d+)\]/.exec(paramName)[1];
					obj[key][index] = paramValue;
				} else {
					// otherwise add the value to the end of the array
					obj[key].push(paramValue);
				}
			} else {
				// we're dealing with a string
				if (!obj[paramName]) {
					// if it doesn't exist, create property
					obj[paramName] = paramValue;
				} else if (obj[paramName] && typeof obj[paramName] === 'string') {
					// if property does exist and it's a string, convert it to an array
					obj[paramName] = [obj[paramName]];
					obj[paramName].push(paramValue);
				} else {
					// otherwise add the property
					obj[paramName].push(paramValue);
				}
			}
		}
	}

	return obj;
}

