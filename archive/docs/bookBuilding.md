# Book Building

## About

The OIH book is built using Jupyter book.  This allows us to mix in exectuted and 
interactive elements while allow a static version in PDF or other formats to be built.

What follows are some not on how to build the book and some repository layout 
conventions we use.  


## Overview

The complete overview of the branch relations follows

![overview](./images/branches.svg)

## Book Building Workflow

We can look at only the sections related to the active book updating

![book only](./images/bookBuilding.svg)

## Notes

```bash
jupyter-book clean . --all; jupyter-book build .;
```
