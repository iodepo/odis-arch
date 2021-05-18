// Conduct the SPARQL call and call the lithtml functions to render results
/* jshint esversion: 6 */
import {
	html,
	render
} from '/js/lit-html.js';
import { showresults } from '/js/geodexv2/general_render.js';

export function generalText(q, n, o) {
	console.log("Get Blaze full text");
	console.log(n);

	(async () => {

		var url = new URL("https://graph.geodex.org/blazegraph/namespace/nabu/sparql"),

		// params format
		// 		params = {
		// 			query: ` 
		// 			...			
		// 		?lit bds:search \"${q}\" . \
		// ...
		// LIMIT ${n}
		// OFFSET ${o}
		// ` }

		params = {
			query: ` 
			prefix schema: <http://schema.org/>  \
			prefix sschema: <https://schema.org/>  \
			SELECT DISTINCT ?s ?g ?url ?score  ?name ?description   \
			WHERE {     \
			  ?lit bds:search \"${q}\" .    \
			  ?lit bds:matchAllTerms "false" .   \
			  ?lit bds:relevance ?score .   \
			  ?s ?p ?lit .       \
			   \
			  VALUES (?dataset) { ( schema:Dataset ) ( sschema:Dataset ) } \
			  ?s a ?dataset .   \
			  ?s schema:name|sschema:name ?name .   \
			 \
			  graph ?g { \
			  ?s schema:description|sschema:description ?description .  \
			  } \
			 \
			  OPTIONAL { \
				?s schema:distribution|sschema:distribution ?dis .    	 \
				?dis schema:contentUrl |sschema:contentUrl  ?url .    	     \
			  } \
			 \
			} ORDER BY DESC(?score) \
			LIMIT ${n} \
			OFFSET ${o} \
` }


		Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
		console.log(params["query"]);

		const rawResponse = await fetch(url, {
			method: 'GET',
			headers: {
				'Accept': 'application/sparql-results+json',
				'Content-Type': 'application/json'
			}
		});

		const content = await rawResponse.json();
		//console.log(content);

		const el = document.querySelector('#container2');
		render(showresults(content), el);
		// const s1 = document.querySelector('#side1');
		// render(projresults(content), s1);
	})();
}
