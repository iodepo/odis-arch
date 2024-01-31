# Releaser

## About

This code is used to make a public snapshot of the current
set of graphs in .../graphs/latest into public/graphs.

It should do this as a snapshot set, make a prefix like:

```bash
 python releaser.py --source s3://nas.lan:49153/gleaner.oih/graphs/latest --output s3://nas.lan:49153/public/graphs/test1
```


### DEPRECATED   the following is no longer the pattern, date the prefix, not the object
For the latest *_release.nq
```bash
public/graphs/odisgraph_v1_[DATE]
```
and

For the latest *_prov.nq
```bash
public/graphs/odisgraph_v1_prov_[DATE]
```
