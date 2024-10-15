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

In addition to the mappings below, the Label records can also be added to `usageInfo`, `ethicsPolicy`, or `publishingPrinciples` fields based on when or how the data was gathered, used, or shared.

| Label Type | usageInfo | ethicsPolicy | publishingPrinciples |
| --- | :---: |  :---: | :---: |
| TK Attribution Label | X |  | X |
| TK Clan Label | X | X | X |
| TK Multiple Communities | X | X | X |
| TK Community Voice |  |  |  |
| TK Creative | X |  | X |
| TK Verified | X |  | X |
| TK Non-Verified |  |  |  |
| TK Seasonal | X | X |  |
| TK Women General | X | X |  |
| TK Women Restricted | X | X |  |
| TK Men General | X | X |  |
| TK Men Restricted | X | X |  |
| TK Culturally Sensitive | X | X |  |
| TK Secret/Sacred | X | X |  |
| TK Open to Commercialization | X |  | X |
| TK Non-Commercial | X |  | X |
| TK Community Use Only | X | X | X |
| TK Outreach | X |  | X |
| TK Open to Collaboration | X |  | X |
| BC Provenance | X |  | X |
| BC Multiple Communities | X |  | X |
| BC Clan | X | X | X |
| BC Consent Verified | X | X | X |
| BC Consent Non-Verified | X | X | X |
| BC Research Use | X |  | X |
| BC Open to Collaboration | X |  | X |
| BC Open to Commercialization | X |  | X |
| BC Outreach | X |  | X |
| BC Non-Commercial | X |  | X |

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

### TK Attribution <!-- Done -->
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
```{seealso}
See also:  [TK Attribution](https://localcontexts.org/label/tk-attribution/)
```

### TK Clan, TK Family and TK Multiple Communities <!-- Done* -->
<!-- PL wants to check if we can map agents in order based on a dedicated description of their role https://www.w3.org/TR/json-ld/#sets-and-lists -->
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

See also:  [TK Clan](https://localcontexts.org/label/tk-clan/), [TK Family](https://localcontexts.org/label/tk-family/), or [TK Multiple Communities](https://localcontexts.org/label/tk-multiple-communities/)
```

### TK Community Voice <!-- Done -->
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

```{seealso}
See also:  [TK Community Voice](https://localcontexts.org/label/tk-community-voice/)
```

### TK Creative <!-- Done -->
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

```{seealso}
See also:  [TK Creative](https://localcontexts.org/label/tk-creative/)
```

### TK Verified <!-- Review -->
This Label will be added in two places.

Added to the dataset.

```json
{
    ...
    "@type": "AssessAction",
    "agent": {
        {
            "@type": "Organization",
            "name": "Example Community Name"
        }
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
        "certificationStatus": "CertificationActive",
        *include Label Mapping*
    }
}
```

```{seealso}
See also:  [TK Verified](https://localcontexts.org/label/tk-verified/)
```

### TK Non-Verified <!-- Review -->
Added to the dataset.

```json
{
    ...
    "hasCertification": {
        "@type": "Certification",
        "issuedBy": {
            "@type": "Organization",
            "name": "Example Community Name"
        },
        "certificationStatus": "CertificationInactive",
        *include Label Mapping*
    }
}
```

```{seealso}
See also:  [TK Non-Verified](https://localcontexts.org/label/tk-non-verified/)
```

### TK Seasonal <!-- Review -->
Added to a dataset.

```json
{
    ...
    "license": {
        *include Label Mapping*
    },
    "usageInfo": {
        *include Label Mapping*
    },
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
}
```

Added to a thing. As Ocean InfoHub is leveraging Schema.org we are using [schema.org/Thing](https://schema.org/Thing) for this type. Any of the properties of Thing seen there are valid to use in such a record.

```json
{
    "potentialAction": {
        "@type": "Action",
        "actionStatus": "PotentialActionStatus",
        "agent": [
            {
                "@type": "Organization",
                "name": "Example Community Name"
            }
        ],
        "startTime": "2024-09-23T15:00:00.000Z",
        "endTime": "2024-09-23T15:00:00.000Z",
        "location": {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        },
        "description": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels"
    }
}
```
The `agent` property here should be included if this action should only be done or performed by a community or other group/individual. The use of `startTime`, `endTime`, and `location` are optional. These are meant to represent the time of year or location of when and where the associated item can be used. This is determined by the Community applying the Labels.

```{seealso}
See also:  [TK Seasonal](https://localcontexts.org/label/tk-seasonal/)
```

### TK Woman General <!-- Done -->
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "peopleAudience" : {
        "suggestedGender": "Female"
    }
}
```

```{seealso}
See also:  [TK Woman General](https://localcontexts.org/label/tk-women-general/)
```

### TK Woman Restricted <!-- Done -->
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "peopleAudience" : {
        "requiredGender": "Female"
    },
    "audience": {
        "@type": "Audience",
        "name": "Example Community Name"
    }
}
```

```{seealso}
See also:  [TK Woman Restricted](https://localcontexts.org/label/tk-women-restricted/)
```

### TK Men General <!-- Done -->
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "peopleAudience" : {
        "suggestedGender": "Male"
    }
}
```

```{seealso}
See also:  [TK Men General](https://localcontexts.org/label/tk-men-general/)
```

### TK Men Restricted <!-- Done -->
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "peopleAudience" : {
        "requiredGender": "Male"
    },
    "audience": {
        "@type": "Audience",
        "name": "Example Community Name"
    }
}
```

```{seealso}
See also:  [TK Men Restricted](https://localcontexts.org/label/tk-men-restricted/)
```

### TK Culturally Sensitive <!-- Review -->
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels"
}
```

```{seealso}
See also:  [TK Culturally Sensitive](https://localcontexts.org/label/tk-culturally-sensitive/)
```

### TK Secret/Sacred <!-- Review -->
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "audience": {
        "@type": "Audience",
        "name": "Example Community Name"
    }
}
```

```{seealso}
See also:  [TK Secret/Sacred](https://localcontexts.org/label/tk-secret-sacred/)
```

### TK Open to Commercialization <!-- Review -->
Added to the dataset.

```json
{
    ...
    "usageInfo": {
        *include Label Mapping*
    },
    "license": {
        *include Label Mapping*
    },
    "offers": {
        "@type": "Offer",
        "offerBy": {
            {
                "@type": "Organization",
                "name": "Example Community Name"
            }
        },
        "category": "Service",
        "eligibleCustomerType": "PublicInstitution",
        "eligibleRegion": {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        },
        "ineligibleRegion": {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        }
    }
}
```
The use of `category`, `eligibleCustomerType`, `eligibleRegion`, and `ineligibleRegion` are optional. The use of [`category`](https://schema.org/category) should be based on the type of thing the Label is being applied on. The use of [`eligibleCustomerType`](https://schema.org/eligibleCustomerType) should be if there is a specific entity that the community is open to negotiating with. The use of [`eligibleRegion`](https://schema.org/eligibleRegion) or [`ineligibleRegion`](https://schema.org/ineligibleRegion) should be based on if there is a specific location or region that the community is or is not open to negotiating with.

These are meant to specify the type of data, item, etc. that the Label is being applied to and, thus, will be the thing that the community is requesting negotiations for commercial opportunities.

Any additional fields available to [schema.org/Offer](https://schema.org/Offer) can be added to `offers`.

```{seealso}
See also:  [TK Open to Commercialization](https://localcontexts.org/label/tk-commercial/)
```

### TK Non-Commercial <!-- Review -->
Added to the dataset.

```json
{
    ...
    "usageInfo": {
        *include Label Mapping*
    },
    "license": {
        *include Label Mapping*
    },
}
```

```{seealso}
See also:  [TK Non-Commercial](https://localcontexts.org/label/tk-non-commercial/)
```

### TK Community Use Only <!-- Review -->
Added to the dataset.

```json
{
    ...
    "conditionsOfAccess": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
    "audience": {
        "@type": "Audience",
        "name": "Example Community Name"
    }
}
```

```{seealso}
See also:  [TK Community Use Only](https://localcontexts.org/label/tk-community-use-only/)
```

### TK Outreach <!-- Review -->
Added to the dataset.

```json
{
    ...
    "usageInfo": {
        "about": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
        "educationalAlgnment": [
            "@type": "AlignmentObject",
            "alignmentType": "educationalSubject",
        ]
    }
}
```

```{seealso}
See also:  [TK Outreach](https://localcontexts.org/label/tk-outreach/)
```

### TK Open to Collaboration <!-- Review -->
Added to the dataset.

```json
{
    ...
    "offers": {
        "@type": "Offer",
        "offerBy": {
            {
                "@type": "Organization",
                "name": "Example Community Name"
            }
        },
        "category": "Collaboration",
        "eligibleCustomerType": "PublicInstitution",
        "eligibleRegion": {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        },
        "ineligibleRegion": {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        },
        "validFrom": "2024-09-23T15:00:00.000Z",
        "validThrough": "2024-09-23T15:00:00.000Z"
    }
}
```
Only the `type` and `offerBy` sections are required. The rest of the fields are optional. The use of [`category`](https://schema.org/category) should be based on offer being provided (in this case, collaboration). This can be edited to better match whatever the community is offering. The use of [`eligibleCustomerType`](https://schema.org/eligibleCustomerType) should be if there is a specific entity that the community is open to negotiating with. The use of [`eligibleRegion`](https://schema.org/eligibleRegion) or [`ineligibleRegion`](https://schema.org/ineligibleRegion) should be based on if there is a specific location or region that the community is or is not open to negotiating with. The use of [`validFrom`](https://schema.org/validFrom) and/or [`validThrough`](https://schema.org/validThrough) should be set if there is a timeframe when the community is interested in collaborating with others.

These are meant to specify the type of data, item, etc. that the Label is being applied to and, thus, will be the thing that the community is requesting negotiations for commercial opportunities.

Any additional fields available to [schema.org/Offer](https://schema.org/Offer) can be added to `offers`.

```{seealso}
See also:  [TK Open to Collaboration](https://localcontexts.org/label/tk-open-to-collaboration/)
```

## Biocultural (BC) Labels

### BC Provenance


```{seealso}
See also:  [BC Provenance](https://localcontexts.org/label/bc-provenance/)
```

### BC Multiple Communities and BC Clan <!-- Done* -->
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

For the BC Multiple Communities Label, the `agent` property should be included for all communities added to the Label.

```{seealso}
For [schema.org/agent](https://schema.org/agent), see Community Agent for additional optional information.

See also:  [BC Multiple Communities](https://localcontexts.org/label/bc-multiple-communities/) or [BC Clan](https://localcontexts.org/label/bc-clan/)
```

### BC Consent Verified


```{seealso}
See also:  [BC Consent Verified](https://localcontexts.org/label/bc-consent-verified/)
```

### BC Consent Non-Verified


```{seealso}
See also:  [BC Consent Non-Verified](https://localcontexts.org/label/bc-consent-non-verified/)
```

### BC Research Use


```{seealso}
See also:  [BC Research Use](https://localcontexts.org/label/bc-research-use/)
```

### BC Open to Collaboration <!-- Review -->
Added to the dataset.

```json
{
    ...
    "offers": {
        "@type": "Offer",
        "offerBy": {
            {
                "@type": "Organization",
                "name": "Example Community Name"
            }
        },
        "category": "Collaboration",
        "eligibleCustomerType": "PublicInstitution",
        "eligibleRegion": {},
        "ineligibleRegion": {},
        "validFrom": "2024-09-23T15:00:00.000Z",
        "validThrough": "2024-09-23T15:00:00.000Z"
    }
}
```
Only the `type` and `offerBy` sections are required. The rest of the fields are optional. The use of [`category`](https://schema.org/category) should be based on offer being provided (in this case, collaboration). This can be edited to better match whatever the community is offering. The use of [`eligibleCustomerType`](https://schema.org/eligibleCustomerType) should be if there is a specific entity that the community is open to negotiating with. The use of [`eligibleRegion`](https://schema.org/eligibleRegion) or [`ineligibleRegion`](https://schema.org/ineligibleRegion) should be based on if there is a specific location or region that the community is or is not open to negotiating with. The use of [`validFrom`](https://schema.org/validFrom) and/or [`validThrough`](https://schema.org/validThrough) should be set if there is a timeframe when the community is interested in collaborating with others.

These are meant to specify the type of data, item, etc. that the Label is being applied to and, thus, will be the thing that the community is requesting negotiations for commercial opportunities.

Any additional fields available to [schema.org/Offer](https://schema.org/Offer) can be added to `offers`.

```{seealso}
See also:  [BC Open to Collaboration](https://localcontexts.org/label/bc-open-to-collaboration/)
```

### BC Open to Commercialization <!-- Review -->
Added to the dataset.

```json
{
    ...
    "usageInfo": {
        *include Label Mapping*
    },
    "license": {
        *include Label Mapping*
    },
    "offers": {
        "@type": "Offer",
        "offerBy": {
            {
                "@type": "Organization",
                "name": "Example Community Name"
            }
        },
        "category": "Service",
        "eligibleCustomerType": "PublicInstitution",
        "eligibleRegion": {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        },
        "ineligibleRegion": {
            "@type": "Place",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 39.3280,
                "longitude": 120.1633
            },
            "name": "Textual name of the area served",
            "description": "Description of the area served"
        }
    }
}
```
The use of `category`, `eligibleCustomerType`, `eligibleRegion`, and `ineligibleRegion` are optional. The use of [`category`](https://schema.org/category) should be based on the type of thing the Label is being applied on. The use of [`eligibleCustomerType`](https://schema.org/eligibleCustomerType) should be if there is a specific entity that the community is open to negotiating with. The use of [`eligibleRegion`](https://schema.org/eligibleRegion) or [`ineligibleRegion`](https://schema.org/ineligibleRegion) should be based on if there is a specific location or region that the community is or is not open to negotiating with.

These are meant to specify the type of data, item, etc. that the Label is being applied to and, thus, will be the thing that the community is requesting negotiations for commercial opportunities.

Any additional fields available to [schema.org/Offer](https://schema.org/Offer) can be added to `offers`.

```{seealso}
See also:  [BC Open to Commercialization](https://localcontexts.org/label/bc-open-to-commercialization/)
```

### BC Outreach <!-- Review -->
Added to the dataset.

```json
{
    ...
    "usageInfo": {
        "about": "Customized Label Title: Customized Label text. https://localcontextshub.org/projects/00000000-00000000-00000000-00000000#labels",
        "educationalAlgnment": [
            "@type": "AlignmentObject",
            "alignmentType": "educationalSubject",
        ]
    }
}
```

```{seealso}
See also:  [BC Outreach](https://localcontexts.org/label/bc-outreach/)
```

### BC Non-Commercial <!-- Review -->
Added to the dataset.

```json
{
    ...
    "usageInfo": {
        *include Label Mapping*
    },
    "license": {
        *include Label Mapping*
    },
}
```

```{seealso}
See also:  [BC Non-Commercial](https://localcontexts.org/label/bc-non-commercial/)
```
