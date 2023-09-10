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

### Example Flow

1) Contributers can work on edits in their own branches
2) These can merged into Master as a means to share contributions for eventual publishing
3) Once a master banch Book directory is in a status where the contributers wish to publisher an update, 
   a merge (or rebase) into the _publication_ branch can take place
4) On such an action, the GitHUb Actions will be triggered and a build will take place with a merge
   into the branch _gh_pages_ which are then published via GitHub Pages to the domain [book.oceaninfohub.org](book.oceaninfohub.org).

Note:  All the steps in 4 are automatic basedon the trigger event
Note:  No edits or commits should be done in the _piublication_ branch by contributers.  It should only be updated via merge/rebase
Note:  No edits or commits should be done in the _gh_pages_ branch by contributers.  It should only be updated via GitHub Actions

Contributers can also build and view the book locally by using the following command either in their own
branches or in Master.  

```bash
jupyter-book clean . --all; jupyter-book build .;
```


