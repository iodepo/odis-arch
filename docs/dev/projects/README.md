# XXX

## References


## Vocabulary resources


## Metadata elements of interest


## Notes


What defines a project?  From Schema.org:

> An enterprise (potentially individual but typically
> collaborative), planned to achieve a particular aim. Use properties from
> Organization, subOrganization/parentOrganization to indicate project sub-structures.

### Functional interest

* find collaborators
* find project gaps
* who funds what (semantic grouping)
* find duplications of funding (who is doing things already done)
* ID regional trends (what is important where) and then compare and contrast

### Notes

* [EurOcean](http://www.kg.eurocean.org/)
  * National projects in native languages
  * Use: [SeaDataNet](https://www.seadatanet.org/Metadata)
    * https://imdis.seadatanet.org/content/download/122068/file/2_1_IMDIS_2018_submission_61.pdf
    * https://www.rd-alliance.org/group/research-metadata-schemas-wg/wiki/enabling-global-data-discovery-through-structured-data
  * They have to deal with no common structure among the databases for descriptions
  * Set of fields have been aligned on with IDs
  * keywords to identify marine projects
  * Relationship with CORDIS
  * Understand the unit of knowledge being developed that can be transferred
    * How to describe unit of knowledge (ref: http://www.kg.eurocean.org/KOs)
* [ODIDO](http://www.ioc-africa.org/projects)
  * Set of parameters defined
    * Project Name
    * Country
    * Funds Source
    * Executing Agency
    * Focal Area
    * Start Date
    * End Date
    * Contact
    * Total Grant
    * Thematic Areas
    * Website
    * LME Region
    * Lead Implementing Agency
  * Current UI is a list.  Needs a way to ensure this can be crawed as a collection
    * Leverage https://schema.org/ItemList on a master index list page
* How many resources have spatial coverage
* What went in (people, funds, etc) and output (kg docs, etc)

### Ref

* https://schema.org/Project
  
### Questions

* Are these reseach projects?
  * https://schema.org/FundingAgency
  * https://schema.org/ResearchProject
* As distinct from institution above, correct?

I've used research project:  https://opencoredata.org/id/csdco/res/YUFL
