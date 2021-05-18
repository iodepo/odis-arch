

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

