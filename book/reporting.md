# Index Reporting Products

## About

The indexing code also provides a report for every indexing event, and stores all historical reports 
to allow groups to see both the current and historical activity.

There are four reports:

1) Load Report: A summary of URLs accessed and the result of the indexing on those URLs
2) Graph statistics: A report on the various counts of properties in the graph including
   3) triple count
   4) type count
   5) keyword count
   6) variable count
   7) version count
8) Identifier statistics: A document used internal to the indexer for resolving objects
9) Bucket URL relations: Assocates sitemap URLs with the internal content hash for those objects.  Used to resolve back to the JSON-LD indexed from the sitemap URL used.


## Examples


### Load Report

```json
{
  "source": "bodc",
  "graph": null,
  "sitemap": "https://api.linked-systems.uk/sitemap_pap_api.xml",
  "date": "2024-11-03",
  "bucket": "gleaner",
  "s3store": "ossapi.provisium.io",
  "sitemap_geturls_time": 1.5531907081604004,
  "s3_geturls_time": 6.186345815658569,
  "sitemap_count": 1525,
  "summoned_count": 1495,
  "missing_sitemap_summon_count": 48,
  "missing_sitemap_summon": [
    "This will be a list of URLs that could not be indexed that are present in the sitemap",
     "https://api.linked-systems.uk/api/schema-org/cruise/17223",
    "https://api.linked-systems.uk/api/schema-org/cruise/17778",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148062",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148117",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148129",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148572",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148627",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148688",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148720",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148130",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148191",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148209",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148142",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148615",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148105",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148178",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148210",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148584",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148676",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148098",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148719",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148559",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148652",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148560",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148603",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148639",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148664",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148640",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148166",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148049",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148050",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148732",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148037",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148707",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148074",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148086",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148596",
    "https://api.linked-systems.uk/api/schema-org/dataset/2148154",
    "https://api.linked-systems.uk/api/schema-org/dataset/1876699",
    "https://api.linked-systems.uk/api/schema-org/dataset/1876675",
    "https://api.linked-systems.uk/api/schema-org/dataset/1876663",
    "https://api.linked-systems.uk/api/schema-org/dataset/1848188",
    "https://api.linked-systems.uk/api/schema-org/dataset/1876687",
    "https://api.linked-systems.uk/api/schema-org/dataset/1848176",
    "https://api.linked-systems.uk/api/schema-org/dataset/1876638",
    "https://api.linked-systems.uk/api/schema-org/dataset/1876626",
    "https://api.linked-systems.uk/api/schema-org/dataset/1876651",
    "https://api.linked-systems.uk/api/schema-org/dataset/1836556"
  ],
  "extra_in_summon_count": 0,
  "extra_in_summon": []
}

```

### Graph stats count

This is an abbreviated return without the following stats: kw_count, variable_vount, version_count, graph_size_count

```json
{
  "version": 0,
  "repo": "bodc",
  "date": "2024-11-03",
  "reports": [
    {
      "report": "triple_count",
      "processing_time": 4.727750539779663,
      "length": 1,
      "data": [
        {
          "tripelcount": 113535
        }
      ]
    },
    {
      "report": "dataset_count",
      "processing_time": 0.7654769420623779,
      "length": 1,
      "data": [
        {
          "datasetcount": 1441
        }
      ]
    },
    {
      "report": "type_count",
      "processing_time": 40.18188548088074,
      "length": 19,
      "data": [
        {
          "type": "https://schema.org/PropertyValue",
          "scount": 9555
        },
        {
          "type": "https://schema.org/Person",
          "scount": 1494
        },
        {
          "type": "https://schema.org/Place",
          "scount": 1441
        },
        {
          "type": "https://schema.org/DataDownload",
          "scount": 1337
        },
        {
          "type": "https://schema.org/Event",
          "scount": 827
        },
        {
          "type": "https://schema.org/GeoShape",
          "scount": 802
        },
        {
          "type": "https://schema.org/Role",
          "scount": 751
        },
        {
          "type": "https://schema.org/Dataset",
          "scount": 744
        },
        {
          "type": "https://schema.org/GeoCoordinates",
          "scount": 638
        },
        {
          "type": "https://schema.org/MonetaryGrant",
          "scount": 592
        },
        {
          "type": "http://www.opengis.net/ont/sf#Point",
          "scount": 456
        },
        {
          "type": "https://schema.org/Occupation",
          "scount": 54
        },
        {
          "type": "https://schema.org/BoatTrip",
          "scount": 36
        },
        {
          "type": "http://www.opengis.net/ont/sf#LineString",
          "scount": 21
        },
        {
          "type": "https://schema.org/BoatTerminal",
          "scount": 17
        },
        {
          "type": "https://schema.org/Organization",
          "scount": 11
        },
        {
          "type": "https://schema.org/Geoshape",
          "scount": 1
        },
        {
          "type": "https://schema.org/DataCatalog",
          "scount": 1
        },
        {
          "type": "https://schema.org/CreativeWork",
          "scount": 1
        }
      ]
    }
  ]
}

```


### Identifier stats

```json
{
    "Source": {
        "0": "bodc",
        "1": "bodc",
        "2": "bodc",
        "3": "bodc"
    },
    "Identifiertype": {
        "0": "filesha",
        "1": "identifiersha",
        "2": "identifiersha",
        "3": "identifiersha"
    },
    "Matchedpath": {
        "0": null,
        "1": "$.identifier",
        "2": "$.url",
        "3": "$['@id']"
    },
    "Uniqueid": {
        "0": 18,
        "1": 697,
        "2": 1,
        "3": 779
    },
    "Example": {
        "0": [
            "0f42136bd480f56953d376a2ce2683c49f217ffe",
            "1b2c2c63490af11f036383734b7f16ee963009d8",
            "2443635a969c37ba8a42f208a29f43fc486629a5",
            "30a6f19211a32753c275bc5c0d607f37153125a4",
            "349e2d2402891a94889a8c4fe6d92a8ff7862bbe"
        ],
        "1": [
            "0017b0da950872eb00e6c5aea7a75e8caac12045",
            "0039c857a0decd99f5e1cefa220f181ca221084d",
            "004b538cb93e11b1a315db7ef959eb1d37d956c2",
            "00e415e891b85e6f43af82768916ab718c1dd68f",
            "010770e8bdb6a5cab7c850113c49cc0bdb1c393f"
        ],
        "2": [
            "2a8f3089afc0f70a685fb528a02769271ead47aa"
        ],
        "3": [
            "0017db03993726ddb6e469973ed75cbc031ca2f1",
            "00684a14e05df2280e72cc74bdb128600281db3d",
            "00d435e452c05551bac1498557b6783f631eef5c",
            "012b0ce895f5e30c07c5043d0cf10aa707477394",
            "01552ba15760f00752d888250d9583611abcf312"
        ]
    }
}
```

## Bucket utils


bucketutil_urls.csv



Here is the data converted to Markdown format:

| File | URL | Identifier | Timestamp |
| --- | --- | --- | --- |
| 0017b0da950872eb00e6c5aea7a75e8caac12045.jsonld | https://api.linked-systems.uk/api/schema-org/dataset/1989632 | identifiersha | 2024-11-03 19:47:40+00:00 |
| 0017db03993726ddb6e469973ed75cbc031ca2f1.jsonld | https://api.linked-systems.uk/api/schema-org/event/1922826 | identifiersha | 2024-11-03 19:46:22+00:00 |
| 0039c857a0decd99f5e1cefa220f181ca221084d.jsonld | https://api.linked-systems.uk/api/schema-org/dataset/2051818 | identifiersha | 2024-11-03 19:47:34+00:00 |
| 004b538cb93e11b1a315db7ef959eb1d37d956c2.jsonld | https://api.linked-systems.uk/api/schema-org/dataset/2107726 | identifiersha | 2024-11-03 19:47:17+00:00 |
| 00684a14e05df2280e72cc74bdb128600281db3d.jsonld | https://api.linked-systems.uk/api/schema-org/event/2148781 | identifiersha | 2024-11-03 19:43:36+00:00 |
| 00d435e452c05551bac1498557b6783f631eef5c.jsonld | https://api.linked-systems.uk/api/schema-org/event/1171036 | identifiersha | 2024-11-03 19:43:28+00:00 |
| 00e415e891b85e6f43af82768916ab718c1dd68f.jsonld | https://api.linked-systems.uk/api/schema-org/dataset/2048860 | identifiersha | 2024-11-03 19:47:34+00:00 |
| 010770e8bdb6a5cab7c850113c49cc0bdb1c393f.jsonld | https://api.linked-systems.uk/api/schema-org/dataset/2051867 | identifiersha | 2024-11-03 19:47:42+00:00 |
| 012b0ce895f5e30c07c5043d0cf10aa707477394.jsonld | https://api.linked-systems.uk/api/schema-org/event/2148062 | identifiersha | 2024-11-03 19:43:23+00:00 |
| 013156cbb63315b231af8c492e0caccd3e5518b0.jsonld | https://api.linked-systems.uk/api/schema-org/dataset/2048755 | identifiersha | 2024-11-03 19:47:38+00:00 |
| 01552ba15760f00752d888250d9583611abcf312.jsonld | https://api.linked-systems.uk/api/schema-org/event/1170893 | identifiersha | 2024-11-03 19:43:33+00:00 |
| 016d78c7fbf1f2c4bd2aaad0b82b875bad1ca618.jsonld | https://api.linked-systems.uk/api/schema-org/event/895651 | identifiersha | 2024-11-03 19:42:56+00:00 |
| 01ac23e5bdeadd686c46f86c7bdee55f29791ef0.jsonld | https://api.linked-systems.uk/api/schema-org/dataset/1347247 | identifiersha | 2024-11-03 19:47:06+00:00 |
| 01af6f77527d109ebc4e5f2d42ef4fb6023bb814.jsonld | https://api.linked-systems.uk/api/schema-org/event/1816844 | identifiersha | 2024-11-03 19:45:52+00:00 |
| 01bf9e7489bf245ca9754c328afdc40b8376e46a.jsonld | https://api.linked-systems.uk/api/schema-org/event/2004125 | identifiersha | 2024-11-03 19:45:24+00:00 |


In the object store, this is in CSV like the following example


Example 15 lines only
```csv
0017b0da950872eb00e6c5aea7a75e8caac12045.jsonld,https://api.linked-systems.uk/api/schema-org/dataset/1989632,identifiersha,2024-11-03 19:47:40+00:00
0017db03993726ddb6e469973ed75cbc031ca2f1.jsonld,https://api.linked-systems.uk/api/schema-org/event/1922826,identifiersha,2024-11-03 19:46:22+00:00
0039c857a0decd99f5e1cefa220f181ca221084d.jsonld,https://api.linked-systems.uk/api/schema-org/dataset/2051818,identifiersha,2024-11-03 19:47:34+00:00
004b538cb93e11b1a315db7ef959eb1d37d956c2.jsonld,https://api.linked-systems.uk/api/schema-org/dataset/2107726,identifiersha,2024-11-03 19:47:17+00:00
00684a14e05df2280e72cc74bdb128600281db3d.jsonld,https://api.linked-systems.uk/api/schema-org/event/2148781,identifiersha,2024-11-03 19:43:36+00:00
00d435e452c05551bac1498557b6783f631eef5c.jsonld,https://api.linked-systems.uk/api/schema-org/event/1171036,identifiersha,2024-11-03 19:43:28+00:00
00e415e891b85e6f43af82768916ab718c1dd68f.jsonld,https://api.linked-systems.uk/api/schema-org/dataset/2048860,identifiersha,2024-11-03 19:47:34+00:00
010770e8bdb6a5cab7c850113c49cc0bdb1c393f.jsonld,https://api.linked-systems.uk/api/schema-org/dataset/2051867,identifiersha,2024-11-03 19:47:42+00:00
012b0ce895f5e30c07c5043d0cf10aa707477394.jsonld,https://api.linked-systems.uk/api/schema-org/event/2148062,identifiersha,2024-11-03 19:43:23+00:00
013156cbb63315b231af8c492e0caccd3e5518b0.jsonld,https://api.linked-systems.uk/api/schema-org/dataset/2048755,identifiersha,2024-11-03 19:47:38+00:00
01552ba15760f00752d888250d9583611abcf312.jsonld,https://api.linked-systems.uk/api/schema-org/event/1170893,identifiersha,2024-11-03 19:43:33+00:00
016d78c7fbf1f2c4bd2aaad0b82b875bad1ca618.jsonld,https://api.linked-systems.uk/api/schema-org/event/895651,identifiersha,2024-11-03 19:42:56+00:00
01ac23e5bdeadd686c46f86c7bdee55f29791ef0.jsonld,https://api.linked-systems.uk/api/schema-org/dataset/1347247,identifiersha,2024-11-03 19:47:06+00:00
01af6f77527d109ebc4e5f2d42ef4fb6023bb814.jsonld,https://api.linked-systems.uk/api/schema-org/event/1816844,identifiersha,2024-11-03 19:45:52+00:00
01bf9e7489bf245ca9754c328afdc40b8376e46a.jsonld,https://api.linked-systems.uk/api/schema-org/event/2004125,identifiersha,2024-11-03 19:45:24+00:00

```