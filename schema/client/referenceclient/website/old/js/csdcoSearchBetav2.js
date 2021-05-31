/* jshint esversion: 6 */
import {
	html,
	render
} from '/js/lit-html.js';

// event listeners
document.querySelector('#q').addEventListener('keyup', function (e) {
	console.log("Document Query Selector");
	if (e.keyCode === 13) {
		searchActions();
	}
});

document.querySelector('#update').addEventListener('click', searchActions);

document.addEventListener('readystatechange', () => {
	console.log("Document Add event listener");
	if (document.readyState == 'complete') stateChangeSearch();
});

// popstate for nav buttons
window.onpopstate = event => {
	console.log("Window On pop state event");
	stateChangeSearch();
};

function stateChangeSearch() {
	console.log("State Change Search Called");
	var qup = getAllUrlParams().q;
	if (qup == null) {
		qup = "";
	}

	// Hack to replace any string like "word+word2" with "word word2"
	// happens on the form feed
	var qupv2 = qup.replace(/(?<=[A-Za-z_0-9])[+](?=[A-Za-z_0-9])/g, ' ');

	console.log(qupv2);


	var q = decodeURIComponent(qupv2);

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

	if (q != null && q != "") {
		blazefulltext(q, n, o);
	}
	updateURL(q, n, o, false);

	const navel = document.querySelector('#container1');
	render(navstatus(q, n, o), navel);
}

// rename to clickSearch  (needs updated elsewhere to do that)
function searchActions() {
	console.log("Search Actions Called");

	// let params = (new URL(location)).searchParams;
	let q = document.querySelector('#q').value;
	let n = document.querySelector('#nn').value;

	var o = getAllUrlParams().o;
	if (o == null) {
		o = 0;
	}
	console.log(o);

	if (q != null && q != "") {
		blazefulltext(q, n, o);
	}
	updateURL(q, n, o, true);

	const navel = document.querySelector('#container1');
	render(navstatus(q, n, o), navel);
}

function updateURL(q, n, o, push) {
	console.log("UpdateURL Called");

	let params = new URLSearchParams(location.search.slice(1));
	params.set('q', q);
	params.set('n', n);
	params.set('o', o);

	// Issues with current browsers and titles
	document.title = `Search:${q}&n=${n}&o=${o}`;

	//window.history.replaceState({}, '', location.pathname + '?' + params);
	const state = {
		q: q,
		n: n,
		o: o
	}
	if (push) {
		window.history.pushState(state, 'GeoDex Search', location.pathname + '?' + params);
	}

}

// lithtml function to update the navigation arrows for result sets
function navstatus(q, n, o) {
	console.log("NavStatus Called");

	const itemTemplates = [];

	// itemTemplates.push(html`<p>Number: ${n} Offset: ${o}</p>`);
	var oi = parseInt(o, 10);
	var ni = parseInt(n, 10);

	var onext = oi + ni; // use unary plus operator to add strings by converting to numbers
	var oprev = onext - (2 * ni);

	console.log(oi);
	console.log(ni);
	console.log(onext);
	console.log(oprev);

	// step up and step down o
	itemTemplates.push(html`<a href="/?q=${q}&n=${n}&o=0"><img style="height:35px" src="/img/rewind.svg">   </a>`);

	if (oprev >= ni) {
		itemTemplates.push(html`<a href="/?q=${q}&n=${n}&o=${oprev}"> <img style="height:35px" src="/img/back.svg"> </a>`);
	}

	itemTemplates.push(html`<a href="/?q=${q}&n=${n}&o=${onext}"> <img style="height:35px" src="/img/forward.svg"> </a>`);

	return html`
	<div style="margin-top:5px">
	   ${itemTemplates}
    </div>
	`;

}

// Conduct the SPARQL call and call the lithtml functions to render results
function blazefulltext(q, n, o) {
	console.log("Get Blaze full text");
	console.log(n);

	(async () => {

		var url = new URL("https://graph.openknowledge.network/blazegraph/namespace/oih/sparql"),

		params = {query: `prefix schema: <http://schema.org/> \
SELECT DISTINCT ?s ?type ?score ?name ?lit ?url ?description ?headline \
WHERE { \
  ?lit bds:search \"${q}\" . \
  ?lit bds:matchAllTerms "false" . \
  ?lit bds:relevance ?score . \
  ?s ?p ?lit . \
   OPTIONAL { ?s schema:name ?name . } \
   OPTIONAL { ?s schema:headline ?headline . } \
  OPTIONAL { ?s schema:url ?url . } \
 OPTIONAL { ?s schema:description ?description .  } \
  ?s rdf:type schema:Dataset  . \
} \
ORDER BY DESC(?score) \
LIMIT ${n} \
OFFSET ${o} \
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
		// render(projresults(content), s1);

	})();
}

// Helper function: See if an object is undefine
function getSafe(fn) {
	try {
		return fn();
	} catch (e) {
		return undefined;
	}
}

// Helper function: truncate a block of text to a length n
function truncate(n, useWordBoundary) {
	if (this.length <= n) { return this; }
	var subString = this.substr(0, n - 1);
	return (useWordBoundary
		? subString.substr(0, subString.lastIndexOf(' '))
		: subString) + "...";
};

// Helper function return all the parameters from a URL
function getAllUrlParams(url) {
	console.log("Get All URL params Called");

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

// lithtml render function
const showresults = (content) => {
	console.log("-----------------------------------------------")
	console.log(content)

	var barval = content.results.bindings
	var count = Object.keys(barval).length;
	const itemTemplates = [];
	// itemTemplates.push(html`<div class="container">`);

	// Start the card

	for (var i = 0; i < count; i++) {
		const headTemplate = [];  // write to this and then save to the itemTemplate
		const containerTemplate = [];  // write to this and then save to the itemTemplate

		console.log("--- in  data files loop ---")
		// itemTemplates.push(html`<div class="row" style="margin-top:30px"> <div class="col-12"> <pre> <code>`);


		if (getSafe(() => barval[i].url.value)) {
			headTemplate.push(html`<p> <a href="${barval[i].url.value}">${barval[i].url.value}</a>
			</span></p> `);
		}


		// loopTemplate.push(html`<div class="rescontainer">`);


		// if (getSafe(() => barval[i].s.value)) {
		// 	var u = barval[i].s.value
		// 	containerTemplate.push(html`<span>URL: <a target="_blank"
		// 		href="${barval[i].s.value}">${truncate.apply(u, [300, true])}</a> </span> `);
		// }

		// if (getSafe(() => barval[i].score.value)) {
		// 	containerTemplate.push(html`<span> (score: ${barval[i].score.value}) </span> `);
		// }

		if (getSafe(() => barval[i].description.value)) {
			var s = barval[i].description.value
			containerTemplate.push(html`<p>${truncate.apply(s, [900, true])} </p>`);
		}

		if (getSafe(() => barval[i].addtype.value)) {
			containerTemplate.push(html`<p>File type: ${barval[i].addtype.value} </p>`);
		}

		if (getSafe(() => barval[i].relto.value)) {
			containerTemplate.push(html`<p>See project:
			<a target="_blank" href="/id/do/${barval[i].relto.value}">${barval[i].relto.value}</a> </p>`);
		}

		if (getSafe(() => barval[i].score.value)) {
			var s = barval[i].score.value
			containerTemplate.push(html`<p>${truncate.apply(s, [900, true])} </p>`);
		}

		// itemTemplates.push(html`</code></pre></div></div>`);
		itemTemplates.push(html`<div class="rescard"><div class="resheader">${headTemplate}</div><div class="rescontainer">${containerTemplate} </div> </div>`);
	}

	return html`
	<div style="margin:30px">
	   ${itemTemplates}
    </div>
	`;
};

// lithtml render function
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
