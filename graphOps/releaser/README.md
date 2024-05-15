# Releaser

## About

This code is used to make a public snapshot of the current
set of graphs in .../graphs/latest into public/graphs.

It should do this as a snapshot set, make a prefix like:

```bash
 python releaser.py --source s3://nas.lan:49153/gleaner.oih/graphs/latest \
                    --zeros
                    --sourcematch release \
                    --output s3://nas.lan:49153/public/graphs/test1
```

if --zeros, the other flags, other than source, are ignored and the command will now
return a list of items in --source that have a zero length

## TODO

- make a version that can list/report 0 length objects
- mode the code to convert the nq to nt

public/
public/assets
public/assets/15022024/
public/graphs
public/graphs/15022024/nq
public/graphs/15022024/nt
public/graphs/15022024/kuzu



```bash
 python releaser.py --source s3://ossapi.oceaninfohub.org/gleaner.oih/graphs/latest \
                    --sourcematch release \
                    --output s3://ossapi.oceaninfohub.org/commons/ODIS-KG-MAIN/latest
```

```bash
 python releaser.py --source s3://ossapi.oceaninfohub.org/gleaner.oih/graphs/latest --zeros
```
