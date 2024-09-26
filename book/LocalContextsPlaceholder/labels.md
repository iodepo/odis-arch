# Local Contexts Labels

## About
The [Local Contexts Labels](https://localcontexts.org/labels/) are tools for Indigenous communities and local organizations. Developed through sustained partnership and testing within Indigenous communities across multiple countries, the Labels allow communities to express local and specific conditions for sharing and engaging in future research and relationships in ways that are consistent with already existing community rules, governance, and protocols for using, sharing, and circulating knowledge and data. The Labels provide a practical application of the CARE Principles for Indigenous Data Governance. By establishing Indigenous cultural authority, the Labels clarify Indigenous and local community rights, interests, and relationships to collections and/or data.

There are two categories of Labels that are used within the Hub: Traditional Knowledge (TK) Labels and Biocultural (BC) Labels. The **Traditional Knowledge (TK) Labels** identify and clarify community-specific rules and responsibilities regarding access and future use of traditional knowledge. The **Biocultural (BC) Labels** define community expectations about the appropriate use of biocultural collections and data.

```{warning}
Although there may be similar fields used for multiple Labels, each Label should still be represented as the text for that Label may have different indications or restrictions that should be acknowledged.
```

## Example: Local Contexts Label Graph
The following graph represents a basic record we might use for a Local Contexts Label.

As Ocean InfoHub is leveraging Schema.org we are using schema.org/CreativeWorks for this type. Any of the properties of Label seen there are valid to use in such a record.

```{literalinclude} ../../../odis-in/dataGraphs/thematics/CreativeWork/graphs/local-contexts-label.json
:linenos:
```
Label records should be added to a base dataset's metadata or to a Local Contexts Project metadata. Each Label below will indicate what section(s) that Label's record should be added to.

## Example: Community Agent Graph
The only required information here is `type` and `name`. All other fields are optional and should be added by the Community. We are using [schema.org/Organization](https://schema.org/Organization) for this type. Any of the properties of Organization seen there are valid to use in such a record.

```json
{
    "@type": "Organization",
    "name": "Example Community Name",
    "description": "Community description.",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "New York, New York, United States",
        "postalCode": "12345",
        "streetAddress": "123 Example Avenue"
    },
    "areaServed": {
        "@type": "AdministrativeArea",
        "name": "Lenapehoking"
    },
    "contactPoint":{
        "@type": "ContactPoint",
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "contactType": "Community Contact Point"
    }
}
```
```{note}
Organization used here just as a way to represent an Indigenous community. In this case the following definition is used:
    Community: Local Contexts uses “community” to inclusively refer to Indigenous Peoples around the world who may be organized and self-governed as Nations, First Nations, Tribes, Confederations, Land Councils, and similar collective groups with ancestral ties to the lands and natural resources where they live, occupy, or from which they have been displaced. For more information, visit our [Community FAQ section](https://localcontexts.org/support/frequently-asked-questions/#communities).
```

## Traditional Knowledge (TK) Labels

### TK Attribution
Added to the dataset.

```json
{
    ...
    "subjectOf" :{
        "correction": {
            "@type": "CorrectionComment",
            *include Label Mapping*
        }
    }
}
```

### TK Clan, TK Family, TK Multiple Communities
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "potentialAction": {
        "@type": "ControlAction",
        "actionStatus": "ActiveActionStatus",
        "agent": [
            {
                "@type": "Organization",
                "name": "Example Community Name"
            }
        ]
    }
}
```

For the TK Multiple Communities Label, the `agent` property should be included for all communities added to the Label.

```{seealso}
For [schema.org/agent](https://schema.org/agent), see Community Agent for additional optional information.
```

### TK Community Voice
Added to the Local Contexts Project metadata.

```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": "Project",
    "@id": "https://example.org/id/XYZ",
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
        }
    ],
    "potentialAction": {
        "@type": "InviteAction",
        "agent": [
            {
                "@type": "Organization",
                "name": "Example Community Name"
            }
        ],
        "name": [
            {
                "@language": "en",
                "@value": "TK Community Voice - English Label Title"
            }
        ],
        "description": [
            {
                "@language": "en",
                "@value": "Customized English Label text."
            }
        ],
        "actionStatus": "ActiveActionStatus",
        "object": {
            "@type": "Organization",
            "name": "Example Community Name"
        }
    }
}
```

### TK Creative
Added to the dataset.

```json
{
    ...
    "creditText": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "publishingPrinciples": {
        *include Label Mapping*
    }
}
```

### TK Verified (NEED TO REVIEW)
This Label will be added in two places.

Added to the dataset.

```json
{
    ...
    "@type": "AssessAction",
    "agent": {
        "@type": "Organization",
        "name": "Example Community Name"
    }
}
```

Added to the Local Contexts Project metadata.

```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": "Project",
    "@id": "https://example.org/id/XYZ",
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
        }
    ],
    "hasCertification": {
        "@type": "Certification",
        "issuedBy": {
            "@type": "Organization",
            "name": "Example Community Name"
        },
        "certificationStatus": "CertificationActive"
        *include Label Mapping*
    }
}
```


### TK Non-Verified (NEED TO REVIEW)
This Label will be added in two places.

Added to the dataset.

```json
{
    ...
    "@type": "AssessAction",
    "agent": {
        "@type": "Organization",
        "name": "Example Community Name"
    }
}
```

Added to the Local Contexts Project metadata.

```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": "Project",
    "@id": "https://example.org/id/XYZ",
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
        }
    ],
    "hasCertification": {
        "@type": "Certification",
        "issuedBy": "Example Community Name",
        "certificationStatus": "CertificationActive"
        *include Label Mapping*
    }
}
```


### TK Seasonal


### TK Woman General


### TK Woman Restricted


### TK Men General


### TK Men Restricted


### TK Culturally Sensitive


### TK Secret/Sacred


### TK Open to Commercialization


### TK Non-Commercial


### TK Community Use Only


### TK Outreach


### TK Open to Collaboration


## Biocultural (BC) Labels

### BC Provenance


### BC Multiple Communities


### BC Clan


### BC Consent Verified


### BC Consent Non-Verified


### BC Research Use


### BC Open to Collaboration


### BC Open to Commercialization


### BC Outreach


### BC Non-Commercial