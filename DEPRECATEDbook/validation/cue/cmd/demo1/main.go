package main

import (
	"fmt"
	"log"
	"os"

	"cuelang.org/go/cue"
	"cuelang.org/go/cue/errors"
	"cuelang.org/go/encoding/json"
)

func main() {
	fmt.Println("Cue testing")

	const config = `
#Dimensions :: {
    width:  number
	depth:  number
	height: number
}
	   `

	const j = `{ "width": "a string", "height": 23, "depth": 0.2  }`

	var r cue.Runtime
	i, err := r.Compile("test", config) // no result change for Compile or Parse
	if err != nil {
		log.Print(err)
	}

	dim, err := i.LookupField("#Dimensions")
	if err != nil {
		log.Print(err)
	}

	err = json.Validate([]byte(j), dim.Value)
	if err != nil {
		errors.Print(os.Stderr, err, nil)
	}

}
