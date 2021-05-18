/* jshint esversion: 6 */
import {
	html,
	render
} from '/js/lit-html.js';

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

window.onpopstate = event => {
	console.log("Window On pop state event");
	stateChangeSearch();
};

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

	// Add other search actions here..
	// like to Resource Registry or to filter builders/guides
	if (q != null && q != "") {
		generalText(q, n, o);
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
