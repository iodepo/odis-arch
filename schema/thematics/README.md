# README

## About

Documentation on implementing schema.org for the Ocean Info Hub (OIH) to facilitate the indexing and discovery
of resources.  The approach leverages schema.org which is a community effort and widely
implemented.

## Thematic Profiles

These profiles represent reference implementation of schema.org Types related to the identified ODIS thematic areas.  
They provide a set of minimal elements and notes on more detailed elements.  

These are not final and will evolve with community input.  As this process moves forward we will implement
versioning the profiles to provide stable implementations providers can reliably leverage in their workflows.

1. [Experts and Institutions](./expinst/README.md)
2. [Documents](./docs/README.md)
3. [Projects](./projects/README.md)
4. [Training](./training/README.md)
5. [Vessels](./vessels/README.md)
6. [Spatial](./spatial/README.md)
7. [Services](./services/README.md)



    ```
    {
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
"provider": {
    "@id": "https://www.sample-data-repository.org",
    "@type": "Organization",
    "legalName": "Sample Data Repository Office",
    "name": "SDRO",
    "sameAs": "http://www.re3data.org/repository/r3dxxxxxxxxx",
    "url": "https://www.sample-data-repository.org"
  },
  "publisher": {
    "@id": "https://www.sample-data-repository.org"
  }
}
    ```
