---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
execution:
  allow_errors: true
---

# Training

## About

A thematic type to describe potential training activities.  In Schema.org a Course
is a subtype of [CreativeWork](https://schema.org/CreativeWork) and [LearningResource](https://schema.org/LearningResource).

As defined from [https://schema.org/Course](https://schema.org/Course):

> Course: A description of an educational course which may be offered as distinct
> instances at which take place at different times or take place at different
> locations, or be offered through different media or modes of study. An
> educational course is a sequence of one or more educational events and/or
> creative works which aims to build knowledge, competence or ability of learners.

We can start by looking at a basic Course description.  

## Simple Course

A basic course might simply present the name and description of the course along 
with a few other key properties. 

```{literalinclude} ./graphs/course2.json
:linenos:
:emphasize-lines: 7, 10-15

```

```{code-cell}
:tags: [hide-input]

import json
from pyld import jsonld
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("./graphs/course2.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```

Here we can see the emphasized line 7 and lines 10-15 highlighting some
unique types.

_courseCode_:
The [courseCode](https://schema.org/courseCode) is used to provide the ID used by the provider for this course. 

_provider_:
The [provider](https://schema.org/provider) is the organization offering the course.
This property is from the CreativeWork supertype.  In this case the provider may
be of type Organization or Person.  For Ocean InfoHub these would be described in 
the [Experts and Institutions](../expinst/README.md) section.

```{note}
In this case you can see we use a simple @id in the provider property.  You can 
see this same @id used in the  [Experts and Institutions](../expinst/README.md) section.
By doing this, we connect this provider to the Organization described by that document.

As such these will be connected in the graph.  So there is no need to duplicate 
the information here.  This is a common graph pattern that allows us to simply 
connect resources.   If there was no existing Organization or Person resource you could
simply create one here.   However, you may also find it useful to create a given 
resource and link to it in the graph. 
```

## Detailed Course

There are a wide range of properties that can be used to describe a course. 
Many of these can be seen at the [Course](https://schema.org/Course) type as
the properties from Course and properties
from [LearningResource](https://schema.org/LearningResource).

We wont go into the details of each property here, but we will show a couple.

The example below present two.  

```{literalinclude} ./graphs/course1.json
:linenos:
:emphasize-lines: 4-9, 16, 23-56

```

```{code-cell}
:tags: [hide-input]

import json
from pyld import jsonld
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("./graphs/course1.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```

Line 16 shows the [_teaches_](https://schema.org/teaches) property.  It 
should be noted while this propery can point to simple text, it is 
also possible to leverage [DefinedTerm](https://schema.org/DefinedTerm).  This 
means a controlled vocabulary can be used to describe what the course 
teaches.  Ocean InfoHub provides some more information and links to further
information on defined term in
the [Keywords and Defined Terms](../terms/list.md) section. 

Lines 23-56 show using a [hasCourseInstance](https://schema.org/hasCourseInstance)
property to show instances where this course is being taught.  Also of note
in this example are the lines 4-9 in the context where we can type the
endDate and startDate as type dateTime.  By doing this we must provide the
dates in a format that is in line with the [XML Datatype] and in particular the
[ISO 8601 Data and Time Formats](https://www.w3.org/TR/xmlschema-2/#isoformats).

By doing this we can then later conduct searches on the graph that use date ranges
to allow us to find courses, or any resources, that are being taught in a
given time period.

## References

* [RDA Education and Training on handling of research data IG
](https://www.rd-alliance.org/groups/education-and-training-handling-research-data.html)
* [DC Tabular Application Profiles (DC TAP) - Primer](https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/)
* https://www.w3.org/TR/xmlschema11-2/
  * Use YYYY-MM-DDThh:mm:ss or YYYY-MM-DD
* [http://www.marinetraining.eu/](http://www.marinetraining.eu/)
  * [Example page](http://www.marinetraining.eu/node/1001)
* [https://oceanexpert.org/](https://oceanexpert.org/)
* [Example page](https://oceanexpert.org/event/2859)
* [OCTO](https://www.octogroup.org/)
* https://oceansummerschools.iode.org/ 
* https://octogroup.org/webinars/
* https://catalogue.odis.org/search/type=16 
* https://clmeplus.org/
