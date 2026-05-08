# Local Contexts Projects

## About
On the [Local Contexts Hub](https://localcontextshub.org), the term "Local Contexts
Projects" is used to describe the context where Labels or Notices are being applied.
Examples of Local Contexts Projects include: a website, university syllabus, dissertation,
publication, dataset, museum exhibition, archival record, item in a collection, library
database, photography collection, voucher specimen, or metadata about a record.

## Example: Local Contexts Project Graph
The following graph represents a basic record we might use for a Local Contexts Project.

As Ocean InfoHub is leveraging Schema.org, we are using [schema.org/Project](https://schema.org/Project)
for this type. Any of the properties of Project seen there are valid to use in such a record.

```{literalinclude} ../../../odis-in/dataGraphs/thematics/projects/graphs/localContexts-project-example.json
:linenos:
```
```{note}
Additional properties can be added to this graph depending on the Labels or Notices applied to the Local Contexts Project.
```

### Details: Identifier(s)
When a Project is created in the Local Contexts Hub, it will automatically be assigned
a UUID. This is the first identifier that is required to be included with the Project
information. When creating an LC Project, there are three other external IDs that can
be added to a Project's metadata: Provider's ID, DOI and GUID. These external IDs are
optional.

```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": "Project",
    "@id": "https://example.org/permanentUrlToThisJsonDoc",
    "name": "Example Project Title",
    "foundingDate": "2024-09-23T15:00:00.000Z",
    "url": "https://localcontextshub.org/projects/00000000-00000000-00000000-00000000",
    "description": "Local Contexts Project Description.",
    "sameAs": "https://localcontextshub.org/projects/00000000-00000000-00000000-00000000",
    "identifier": [
        {
            "@id": "https://localcontextshub.org/projects/00000000-00000000-00000000-00000000",
            "@type": "PropertyValue",
            "propertyID": "https://localcontextshub.org/projects",
            "url": "https://localcontextshub.org/projects/00000000-00000000-00000000-00000000",
            "value": "00000000-00000000-00000000-00000000"
        },
        {
            "@type": "PropertyValue",
            "value": "Providers_ID"
        },
        {
            "@id": "https://doi.org/10.5066/F7VX0DMQ",
            "@type": "PropertyValue",
            "propertyID": "https://registry.identifiers.org/registry/doi",
            "url": "https://doi.org/10.5066/F7VX0DMQ",
            "value": "doi:10.5066/F7VX0DMQ"
        },
        {
            "@type": "PropertyValue",
            "value": "Alternate_GUID"
        }
    ]
}
```

### Details: Contact Point
The contact person for a Local Contexts Project.

```json
    "contactPoint": {
        "@type": "ContactPoint",
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "contactType": "Local Contexts Project Contact Point"
    }
```

### Details: Geographic Metadata (WIP)
The geographic metadata for a Local Contexts Project. This is currently being added
to the Local Contexts Hub. Subject to change.
```{note}
Keep in mind that some geographical information may be sensitive. Always confirm with
Indigenous communities first before sharing. As an alternative, the restricted metadata
block can be used in collaboration with Indigenous communities.
```

```json
    "areaServed": [
        {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        },
    ]
```

#### Restrictive Geographic Information
```json
    "areaServed": [
        {
            "@type": "Place",
            "name": "Textual name of the area served",
            "description": "Description of the area served, and measures needed to request access.",
            "publicAccess": "False",
            "isAccessibleForFree": "False"
        }
    ]
```
