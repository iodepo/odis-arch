package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"cuelang.org/go/cue"
	"cuelang.org/go/cue/errors"
	"cuelang.org/go/encoding/json"
)

func main() {
	fmt.Println("Cue testing")

	var cfg, trg string
	flag.StringVar(&cfg, "cue", "foo", "cue file")
	flag.StringVar(&trg, "target", "foo", "target json file to validate")

	flag.Parse()

	config, err := ioutil.ReadFile(cfg)
	if err != nil {
		log.Println(err)
	}

	t, err := ioutil.ReadFile(trg)
	if err != nil {
		log.Println(err)
	}

	var cr cue.Runtime
	cc, err := cr.Compile("test", string(config)) // no result change for Compile or Parse
	if err != nil {
		log.Println(err)
	}

	//dim := cc.Lookup("name")
	dim, err := cc.LookupField("#Min")
	if err != nil {
		log.Print(err)
	}

	//err = json.Validate([]byte(t), dim)
	err = json.Validate([]byte(t), dim.Value)
	if err != nil {
		fmt.Println("----------")
		errors.Print(os.Stderr, err, nil)
	}

}
