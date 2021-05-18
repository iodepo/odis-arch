#Min: {
	#Context: {
		"@vocab": "https://schema.org/"
		// Must start with an uppercase letter.
	}

	#Description: {
		"@type":  string
		"@value": string
	}

	"@context":    #Context
	"@type":       string
	"@id":         string // must have an @id value node
	"name":        string
	"description": string | #Description
	"keywords":    [...string] | string
}
