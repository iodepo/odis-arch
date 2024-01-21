# Book Building

## About

The OIH book is built using Jupyter book.  This allows us to mix in executed and 
interactive elements while allow a static version in PDF or other formats to be built.

What follows are some notes on how to build the book and some repository layout 
conventions we use.  

## Overview

The complete overview of the branch relations follows

![overview](./images/branches.svg)

## Book Building Workflow

The Ocean InfoHub book is based on the Jupyter Book framework.  This framework can render Markdown 
and Jupyter Notebooks into HTML for distribution over the web.  The OIH book has two main 
constituents. One is the Markdown or Notebook content, the other is the graph content.  The Markdown
and Notebooks are maintained in the odis-arch/bookRev1 directory.  The graph content
is composed of JSON-LD representations of data graph and SHACL shapes.  This in the repository 
odis-in, however, this is likely to change.  The structure of this build allows the location of these 
two elements to change location.  The odis-in repository is a submodule in the odis-arch repository.
Information on Git submodules can be found at: https://git-scm.com/book/en/v2/Git-Tools-Submodules


![book only](./images/bookBuilding.svg)

### Example Flow

1) Contributors can work on edits in their own branches
2) These can merged into Master as a means to share contributions for eventual publishing
3) Once a master branch Book directory is in a status where the contributors wish to publisher an update, 
   a merge (or rebase) into the _publication_ branch can take place
4) On such an action, the GitHUb Actions will be triggered and a build will take place with a merge
   into the branch _gh_pages_ which are then published via GitHub Pages to the domain [book.oceaninfohub.org](book.oceaninfohub.org).

Note:  All the steps in 4 are automatic based on the trigger event
Note:  No edits or commits should be done in the _publication_ branch by contributors.  It should only be updated via merge/rebase
Note:  No edits or commits should be done in the _gh_pages_ branch by contributors.  It should only be updated via GitHub Actions

Contributors can also build and view the book locally by using the following command either in their own
branches or in Master.  

Install dependencies:
```Bash
pip install -U jupyter-book
```

You will also beed to use the [requirements.txt](https://github.com/iodepo/odis-arch/blob/master/book/requirements.txt)
file to install required elements.

```Bash
cd ./book
pip install -r requirements.txt
```

from inside the _book_ directory use:
```bash
jupyter-book clean . --all; jupyter-book build .;
```


