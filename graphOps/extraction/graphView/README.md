# Graph View

## About

Building off the core product, the code here generates files that can be
used in graph visualization.

The core targets for output include [GML](https://en.wikipedia.org/wiki/Graph_Modelling_Language)
and some of the following column based encodings. 

These could pair wise such as

| source | target |
|--------|--------|
| a      | b      |
| c      | b      |
| b      | d      |

An example of this can be seen in the London Tube Map at [Example Data | Graphia](https://graphia.app/example-data.html).

We could imagine a more complex relationship to express with something like:

| Subject IRI | Name | predicate | object literal |   |   |
|-------------|------|-----------|----------------|---|---|
|             |      |           |                |   |   |
|             |      |           |                |   |   |
|             |      |           |                |   |   |

