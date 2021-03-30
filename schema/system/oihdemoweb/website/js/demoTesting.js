/* jshint esversion: 6 */
import {
	html,
	render
} from '/js/lit-html.js';

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

function getUrlParam(parameter, defaultvalue){
    var urlparameter = defaultvalue;
    if(window.location.href.indexOf(parameter) > -1){
        urlparameter = getUrlVars()[parameter];
        }
    return urlparameter;
}

var mytext = getUrlParam('q','');
var res = mytext.replaceAll("+", " ");
var qbox = document.getElementById("q");
if( res) {
   qbox.value = res
}
console.log(decodeURIComponent(res));
blazefulltext(res, 20, 0)

// Conduct the SPARQL call and call the lithtml functions to render results
function blazefulltext(q, n, o) {
	console.log("Get Blaze full text");
	console.log(n);

	var x = document.getElementById("loadspinner");
	x.style.display = "block";

	(async () => {

		var url = new URL("https://graph.openknowledge.network/blazegraph/namespace/oih/sparql"),
		//var url = new URL("http://192.168.86.45:32775/blazegraph/namespace/oih/sparql"),

		params = {query: `prefix schema: <https://schema.org/> \
        prefix prov: <http://www.w3.org/ns/prov#> \
        SELECT DISTINCT ?g  ?s ?wat ?orgname ?type ?score ?name ?url ?lit ?description ?headline \
        WHERE \
            { \
            { \
              graph ?g { \
               ?lit bds:search \"${q}\" . \
               ?lit bds:matchAllTerms "false" . \
               ?lit bds:relevance ?score . \
               ?s ?p ?lit . \
               OPTIONAL { ?s schema:name ?name .  } \
               OPTIONAL { ?s schema:headline ?headline .  } \
               OPTIONAL { ?s schema:url ?url .  } \
               OPTIONAL { ?s schema:description ?description .   } \
               ?s rdf:type schema:Course  . \
              } \
               ?sp prov:generated ?g  . \
               ?sp prov:used ?used . \
               ?used prov:hadMember ?hm . \
               ?hm prov:wasAttributedTo ?wat . \
               ?wat rdf:name ?orgname \
              } \
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
			//cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
			headers: {
				'Accept': 'application/sparql-results+json',
				'Content-Type': 'application/json'
			}
		});

		const content = await rawResponse.json();
		//const content = await rawResponse
		console.log(content);

		x.style.display = "none";

		const el = document.querySelector('#container2');
		// const s1 = document.querySelector('#side1');
		render(showresults(content), el);
		// render(projresults(content), s1);

	})();
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

		console.log("--- in  NEW data files loop ---")
		// itemTemplates.push(html`<div class="row" style="margin-top:30px"> <div class="col-12"> <pre> <code>`);



		var s
		if (getSafe(() => barval[i].s.value)) {
			s = barval[i].s.value
		}

		var name
		var nameshort = "Name unavailable"
		if (getSafe(() => barval[i].name.value)) {
			name = barval[i].name.value
			nameshort = truncate.apply(barval[i].name.value, [45, true])
		}

		var resurl
		if (getSafe(() => barval[i].url.value)) {
			resurl = barval[i].url.value
		}

		var desc
		if (getSafe(() => barval[i].description.value)) {
			desc = truncate.apply(barval[i].description.value, [900, true])
		}

		var orgname
		if (getSafe(() => barval[i].orgname.value)) {
			orgname = truncate.apply(barval[i].orgname.value, [900, true])
		}
		// if (getSafe(() => barval[i].addtype.value)) {
		// 	containerTemplate.push(html`<p>File type: ${barval[i].addtype.value} </p>`);
		// }

		// if (getSafe(() => barval[i].relto.value)) {
		// 	containerTemplate.push(html`<p>See project:
		// 	<a target="_blank" href="/id/do/${barval[i].relto.value}">${barval[i].relto.value}</a> </p>`);
		// }

		var score;
		if (getSafe(() => barval[i].score.value)) {
			score = barval[i].score.value
			// containerTemplate.push(html`<p>${truncate.apply(s, [900, true])} </p>`);
		}

		console.log(s)

		// itemTemplates.push(html`</code></pre></div></div>`);
		// itemTemplates.push(html`<div class="rescard"><div class="resheader">${headTemplate}</div><div class="rescontainer">${containerTemplate} </div> </div>`);

		// itemTemplates.push(html`<div class="rescard"><div
		// class="resheader">${headTemplate}</div>
		// <div class="rescontainer">${containerTemplate} </div> </div>`);



		itemTemplates.push(html`
		<article class="border w-2/4 mx-auto border-gray-400 rounded-lg md:p-4 bg-white sm:py-3 py-4 px-2 m-10"
    data-article-path="/hagnerd/setting-up-tailwind-with-create-react-app-4jd" data-content-user-id="112962">
    <div role="presentation">
      <div>
        <div class="m-2">
          <div class="flex items-center">
            <div class="mr-2">
              <a href="/hagnerd">
                <!-- <img class="rounded-full w-8"
                  src="./images/cdf.png"
                  alt="hagnerd profile" loading="lazy"> -->
              </a>
            </div>
            <div>
              <p>
                <a href="/hagnerd" class="text text-gray-700 text-sm hover:text-black">Source: ${orgname} </a>
              </p>
              <a href="/hagnerd/setting-up-tailwind-with-create-react-app-4jd"
                class="text-xs text-gray-600 hover:text-black">
                <time datetime="2019-08-02T13:58:42.196Z">Score: ${score}</time>
              </a>
            </div>
          </div>
        </div>
        <div class="pl-12 md:pl-10 xs:pl-10">
          <h2 class="text-2xl font-bold mb-2 hover:text-blue-600 leading-7">
            <a target="_blank" href="${s}" >
              ${nameshort}
            </a>
          </h2>

          <div class="mb-1 leading-6">
            ${desc}
          </div>
          <div class="flex justify-between items-center">
            <div class="flex">
             <!--  external links here -->
            </div>
            <div class="flex items-center">
              <small class="mr-2 text-gray-600"> </small>
            <!--
			  <button type="button"
                class="bg-gray-400 rounded text-sm px-3 py-2 text-current hover:text-black hover:bg-gray-500">
                <span>View Details</span>
              </button>

			  -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </article>


		`);

	}

	return html`
	<div style="margin:30px">
	   ${itemTemplates}
    </div>
	`;
};

// lithtml render function
const OLDshowresults = (content) => {
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
			headTemplate.push(html`<p> Resource: <a href="${barval[i].url.value}">${barval[i].url.value}</a>
			</span></p> `);
		}

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
