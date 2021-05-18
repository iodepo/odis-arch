# RDF Data Factory

[![Build Status](https://travis-ci.org/rubensworks/rdf-data-factory.js.svg?branch=master)](https://travis-ci.org/rubensworks/rdf-data-factory.js)
[![Coverage Status](https://coveralls.io/repos/github/rubensworks/rdf-data-factory.js/badge.svg?branch=master)](https://coveralls.io/github/rubensworks/rdf-data-factory.js?branch=master)
[![npm version](https://badge.fury.io/js/rdf-data-factory.svg)](https://www.npmjs.com/package/rdf-data-factory)

This package contains an implementation of the [RDF/JS Data model](http://rdf.js.org/data-model-spec/).
It works in both JavaScript and TypeScript.

Concretely, it provides an implementation of the following interfaces:

* [`DataFactory`](http://rdf.js.org/data-model-spec/#datafactory-interface): A factory for instantiating RDF terms and quads.
* [`NamedNode`](http://rdf.js.org/data-model-spec/#namednode-interface): A term that contains an IRI.
* [`BlankNode`](http://rdf.js.org/data-model-spec/#blanknode-interface): A term that represents an RDF blank node with a label.
* [`Literal`](http://rdf.js.org/data-model-spec/#literal-interface): A term that represents an RDF literal, containing a string with an optional language tag or datatype.
* [`Variable`](http://rdf.js.org/data-model-spec/#variable-interface): A term that represents a variable.
* [`DefaultGraph`](http://rdf.js.org/data-model-spec/#defaultgraph-interface): A singleton term instance that represents the default graph.

If using TypeScript, it is recommended to use this in conjunction with [`@types/rdf-js`](https://www.npmjs.com/package/@types/rdf-js).

## Installation

```bash
$ npm install rdf-data-factory
```
or
```bash
$ yarn add rdf-data-factory
```

This package also works out-of-the-box in browsers via tools such as [webpack](https://webpack.js.org/) and [browserify](http://browserify.org/).

## Usage

It is recommended to always create terms via a `DataFactory` instance:
```typescript
import { DataFactory } from 'rdf-data-factory';
import * as RDF from 'rdf-js';

const factory: RDF.DataFactory = new DataFactory();
```

You can pass the following option to define a blank node prefix:
```typescript
const factory: RDF.DataFactory = new DataFactory({ blankNodePrefix: 'bnode_' });
```
If no `blankNodePrefix` is passed, it will generate a unique prefix of the form `df_[0-9]+_`,
which ensures there will be no blank nodes clashes when instantiating multiple factories.

### Creating named nodes

```typescript
const term: RDF.NamedNode = factory.namedNode('http://example.org');
console.log(term.value); // 'http://example.org'
console.log(term.termType); // 'NamedNode'
console.log(term.equals(term)); // true
```

### Creating blank nodes

With a given blank node label:
```typescript
const term: RDF.BlankNode = factory.blankNode('bnode');
console.log(term.value); // 'bnode'
console.log(term.termType); // 'BlankNode'
console.log(term.equals(term)); // true
```

Autogenerate a blank node label using an internal blank node counter:
```typescript
const term: RDF.BlankNode = factory.blankNode();
console.log(term.value); // 'df-0'
console.log(term.termType); // 'BlankNode'
console.log(term.equals(term)); // true
```

Reset the blank node label counter:
```typescript
factory.resetBlankNodeCounter();
```

### Creating literals

Plain string literal:
```typescript
const term: RDF.Literal = factory.literal('abc');
console.log(term.value); // 'abc'
console.log(term.termType); // 'Literal'
console.log(term.language); // ''
console.log(term.datatype); // namedNode('http://www.w3.org/2001/XMLSchema#string')
console.log(term.equals(term)); // true
```

Languaged tagged string literal:
```typescript
const term: RDF.Literal = factory.literal('abc', 'en-us');
console.log(term.value); // 'abc'
console.log(term.termType); // 'Literal'
console.log(term.language); // 'en-us'
console.log(term.datatype); // namedNode('http://www.w3.org/1999/02/22-rdf-syntax-ns#langString')
console.log(term.equals(term)); // true
```

Datatyped literal:
```typescript
const term: RDF.Literal = factory.literal('1.2', factory.namedNode('http://www.w3.org/2001/XMLSchema#double'));
console.log(term.value); // 'abc'
console.log(term.termType); // 'Literal'
console.log(term.language); // ''
console.log(term.datatype); // namedNode('http://www.w3.org/2001/XMLSchema#double')
console.log(term.equals(term)); // true
```

### Creating variables

```typescript
const term: RDF.Variable = factory.variable('myVar');
console.log(term.value); // 'myVar'
console.log(term.termType); // 'Variable'
console.log(term.equals(term)); // true
```

### Getting the default graph

This will always produce the same default graph instance;
```typescript
const term: RDF.DefaultGraph = factory.defaultGraph();
console.log(term.value); // ''
console.log(term.termType); // 'DefaultGraph'
console.log(term.equals(term)); // true
```

### Creating quads

Create a triple in the default graph:
```typescript
const quad: RDF.Quad = factory.quad(
  factory.namedNode('ex:s'),
  factory.namedNode('ex:p'),
  factory.literal('o'),
);
console.log(term.subject); // An RDF.Term
console.log(term.predicate); // An RDF.Term
console.log(term.object); // An RDF.Term
console.log(term.graph); // An RDF.Term, in this case defaultGraph()
console.log(quad.equals(quad)); // true
```

Create a triple in a named graph:
```typescript
const quad: RDF.Quad = factory.quad(
  factory.namedNode('ex:s'),
  factory.namedNode('ex:p'),
  factory.literal('o'),
  factory.namedNode('ex:g'),
);
console.log(term.subject); // An RDF.Term
console.log(term.predicate); // An RDF.Term
console.log(term.object); // An RDF.Term
console.log(term.graph); // An RDF.Term
console.log(quad.equals(quad)); // true
```

Since a `Quad` is also a `Term`, it is possible to annotate `Quad`'s by nesting them:
```typescript
const quad: RDF.Quad = factory.quad(
  factory.quad(
    factory.namedNode('ex:s'),
    factory.namedNode('ex:p1'),
    factory.literal('o'),
  ),
  factory.namedNode('ex:p2'),
  factory.literal('o'),
);
```

### Copying terms

Create a deep copy of the given term:
```typescript
const term1 = factory.namedNode('ex:s');
const term1 = factory.fromTerm(term1);
```

This is useful if you need to transform terms from another data factory.

### Copying quads

Create a deep copy of the given quad:
```typescript
const quad1: RDF.Quad = factory.quad(
  factory.namedNode('ex:s'),
  factory.namedNode('ex:p'),
  factory.literal('o'),
);
const quad2 = factory.fromQuad(quad1);
```

This is useful if you need to transform quads from another data factory.

_Nested quads will be copied recursively to produce an actual deep copy._

## License
This software is written by [Ruben Taelman](http://rubensworks.net/).

This code is released under the [MIT license](http://opensource.org/licenses/MIT).
