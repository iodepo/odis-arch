# OIH Qlever Test Instance

## About

This document describes the use of [qlever-control](https://github.com/ad-freiburg/qlever-control)
to work with the ODIS-OIH graph.

The pre-requisist for using this approach include python and docker.  Once statisfied you
will need to:

```bash
pip install qlever
```

You will find extensive documentation at the github repo above for the various
qlever commands.  What follows is a short example using the ODIS resources and
configuration files.

Make sure the command ```qlever``` is now in your PATH variable.  You may need
to modify your path variable to ensure it is.

First, create a working directory for the ODIS graph to live in on your system.
Call this anything you wish, here I will use ```odis-oih-graph```.

Then change directory, cd, into that new directory and run the
following commands from there.

```bash
wget http://ossapi.oceaninfohub.org/public/Qleverfile-odis
qlever -q Qleverfile-odis get-data         # Download the dataset
qlever -q Qleverfile-odis index            # Build index data structures for this dataset
qlever -q Qleverfile-odis start            # Start a QLever server using that index
qlever -q Qleverfile-odis ui               # Launch the QLever UI
```

The raw SPARQL endpoint should be on port 7019 if you wish to use your own
SPARQL client.   See [GleanerIO Architype Tooling](https://github.com/gleanerio/archetype/blob/master/docs/tooling.md)
for some references to clients and other related tooling.

If you also ran the UI command, you should get

```
The QLever UI should now be up at http://localhost:8176 ...You can log in as QLever UI admin with username and password "demo"
```

and be able to see the UI on port 8176.
