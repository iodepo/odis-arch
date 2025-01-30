# Local Contexts Notices

## About
The [Local Contexts Notices](https://localcontexts.org/notices/) are tools for institutions and researchers to identify Indigenous collections and data and recognize Indigenous rights and interests in collections and data.  The Notices were developed to create pathways for partnership, collaboration, and support of Indigenous cultural authority. They activate researcher and institutional responsibility to identify potential Indigenous rights and interests in historical and future collections, also operationalizing the CARE Principles for Indigenous Data Governance.

There are two categories of Notices that are used within the Hub: Engagement and Disclosure Notices.

The **Engagement Notice** is used to indicate a researcher, institution, or service provider is committed to equitable engagement and ethical partnerships with Indigenous communities. This Notice is typically applied across a website, repository, etc. to indicate that the organization is committed to developing new modes of collaboration, engagement, and partnership over Indigenous collections and data that have colonial and/or problematic histories or unclear provenance.

The **Disclosure Notices** are used to identify Indigenous collections and data and to recognize there could be accompanying cultural rights, protocols, and responsibilities. The Disclosure Notices are for use by collecting institutions, data repositories, and organizations who engage in collaborative curation with Indigenous and other marginalized communities who have been traditionally excluded from processes of documentation and record keeping. The Notices are applied via Local Contexts Projects and can function as place-holders on collections, data, or in a sample field until a Label(s) is added by a community.

## Example: Local Contexts Notice Graph
The following graph represents a basic record we might use for a Local Contexts Notice.

As Ocean InfoHub is leveraging Schema.org we are using schema.org/CreativeWorks for this type. Any of the properties of Label seen there are valid to use in such a record.

```{literalinclude} ../../../odis-in/dataGraphs/thematics/CreativeWork/graphs/local-contexts-notice.json
:linenos:
```

Notice records should be added to a base dataset's metadata or to a Local Contexts Project metadata. Each Notice below will indicate what section(s) that Notices's record should be added to.

In addition to the mappings below, the Notice records can also be added to `usageInfo`, `ethicsPolicy`, or `publishingPrinciples` fields based on when or how the data was gathered, used, or shared.

| Label Type | usageInfo | ethicsPolicy | publishingPrinciples |
| --- | :---: |  :---: | :---: |
| Traditional Knowledge Notice |  | X |  |
| Biocultural Notice |  | X |  |
| Attribution Incomplete Notice |  |  |  |
| Open to Collaborate Notice |  |  |  |

## Engagement Notice

### Open to Collaborate Notice
Added to the dataset.

```json
{
    ...
    "offers": {
        "@type": "Offer",
        "offerBy": {
            {
                "@type": "Organization",
                "name": "Example Organization Name"
            }
        },
        "category": "Collaboration",
        "eligibleCustomerType": "Indigenous Communities",
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

## Disclosure Notices

### Traditional Knowledge (TK) Notice and Biocultural (BC) Notice
When including these Notices on a dataset, the Local Contexts Notice Graph should be placed within [schema.org/publishingPrinciples](https://schema.org/publishingPrinciples).

When including these Notices within [schema.org/Organization](https://schema.org/Organization), the Local Contexts Notice Graph should be placed within [schema.org/ethicsPolicy](https://schema.org/ethicsPolicy).

### Attribution Incomplete Notice
When including this Notice as an invitation for communities to engage, the Local Contexts Notice Graph should be placed within [schema.org/publishingPrinciples](https://schema.org/publishingPrinciples).

When including this Notice on a dataset, the Local Contexts Notice Graph should be placed within [schema.org/publishingPrinciples](https://schema.org/publishingPrinciples).

When including this Notice within [schema.org/Organization](https://schema.org/Organization), the Local Contexts Notice Graph should be placed within [schema.org/ethicsPolicy](https://schema.org/ethicsPolicy).