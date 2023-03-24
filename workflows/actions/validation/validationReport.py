#!/usr/bin/env python
# coding: utf-8

# # SHACL Simple
#
# SHACL validation examples
#
# It should be noted here that SHACL validation is not a service OIH offers.  Rather,
# the validation is a capacity that the OIH architectural approach facilities.  Further
# this validation follows W3C recommendations as describted in
# [https://www.w3.org/TR/shacl/](https://www.w3.org/TR/shacl/).
#
# * [SHACL Playground](https://shacl.org/playground/)
# * [pySHACL](https://github.com/rdflib/pyshacl)
# * [kglab SHACL validation with pySHACL](https://derwen.ai/docs/kgl/ex5_0/)
#
# dgurl = "http://ossapi.oceaninfohub.org/public/graphs/summonededmo_v1_release.rdf"
# sgurl =  "https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/code/notebooks/validation/shapes/oih_search.ttl"
#

# Imports
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)  ## remove pandas future warning

# pyshack sends output to log along with the vars.  This suppresses that
import logging, sys
logging.disable(sys.maxsize)

from urllib.request import urlopen
import kglab
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import time, io, os
from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
import argparse
from minio import Minio
from rdflib import Graph, plugin

# Unused...   kept as reference for now
# from rdflib import Dataset
# from rdflib.serializer import Serializer
# import boto3
# # from reportlab.rl_config import defaultPageSize
# from reportlab.platypus.tables import Table

# Process each line of nq and make nt (total HACK!   replace with
# proper rdflib approach when I figure it out)
def popper(input):
    lines = input.decode().split('\n') # Split input into separate lines
    modified_lines = []

    for line in lines:
        segments = line.split(' ')

        if len(segments) > 3:
            segments.pop()   # Remove the last two segment
            segments.pop()
            new_line = ' '.join(segments) + ' .'
            modified_lines.append(new_line)

    result_string = '\n'.join(modified_lines)

    return(result_string)

def publicurls(client, bucket, prefix):
    urls = []
    objects = client.list_objects(bucket, prefix=prefix, recursive=True)
    for obj in objects:
        result = client.stat_object(bucket, obj.object_name)

        if result.size > 0:  #  how to tell if an objet   obj.is_public  ?????
            url = client.presigned_get_object(bucket, obj.object_name)
            # print(f"Public URL for object: {url}")
            urls.append(url)

    return urls

def main():
    # Initialize args  parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datagraph", help="datagraph to check")
    parser.add_argument("-s", "--shapegraph", help="shacl shape graph to use")
    parser.add_argument("-n", "--name", help="name of the validation run, spatial, core, funding")

    args = parser.parse_args()
    dgurl = args.datagraph
    sgurl = args.shapegraph
    valname = args.name

    # Get the public URLs from an object store as a source for the validation
    client = Minio("ossapi.oceaninfohub.org:80",  secure=False) # Create client with anonymous access.
    urls = publicurls(client, "public", "graph")

    #  need to parse out the name from the release graph and the base name of the shacl shape used
    pattern = r"summoned(.*?)_v1"
    match = re.search(pattern, dgurl)  # Use re.search() to extract the text between "summoned" and "_v1"
    source = "unknown"

    if match:
       # Access the matched text using group(1)
       source = match.group(1)
    else:
       print("No match found.")
       raise "unable to match on provider name via regex"

    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

    isValid = validate(sgurl, dgurl, source, valname, date_time)

    # TODO, remove this stupid logic hold over.  If isValid is true, then no issues are found
    # no heatmap or csv is made.   I can just test that here and call buildReport or not and remove the
    # ib boolean from the buildReport logic (since I only call when False).  However, it would be good to
    # still make a report for all passed to let people know, so need to modify the logic here
    buildReport(isValid, sgurl, source, valname, date_time)

def validate(sgurl, dgurl, source, valname, date_time):
    namespaces = {
        "shacl":   "http://www.w3.org/ns/shacl#" ,
        "schema": "https://schema.org/"
        }

    kg = kglab.KnowledgeGraph(
        name = "Schema.org based datagraph",
        base_uri = "https://example.org/id/",
        namespaces = namespaces,
        )

    sf = urlopen(sgurl)
    sg = sf.read()

    df = urlopen(dgurl)
    dg = df.read()

    # print(dg)
    r = popper(dg)

    fna = []   # array to hold errors
    try:
        g = Graph().parse(data=r, format='nt')
        r = g.serialize(format='nt')
        # print(r)
        kg.load_rdf_text(r)
    except Exception as e:
        # code = x.status_code
        # dtype = info.get_content_type()
        print("Exception: {}\n --".format(str(e)))
        # print("An exception occurred with {}".format(fn))
        # fna.append(fn)
        # TODO  should just bail at this point (raise exception)
        raise e

    conforms, report_graph, report_text = kg.validate(
        shacl_graph=sg,
        shacl_graph_format="ttl"
    )

    kg.load_rdf_text(data=report_graph.save_rdf_text(), format="ttl")

    # print(report_graph.save_rdf_text())

    sparql = """
    SELECT  ?severity  ?constraint ?path ?message (STR(?focus) AS ?focusURL) ?path ?value
      WHERE {
        ?id rdf:type shacl:ValidationResult .
        ?id shacl:focusNode ?focus .
        ?id shacl:resultMessage ?message .
        ?id shacl:resultSeverity ?severity .
        ?id shacl:sourceConstraintComponent ?constraint .
        OPTIONAL {
            ?id shacl:resultPath ?path .
        }
        OPTIONAL {
            ?id shacl:value ?value .
        }
      }
    """

    pdf = kg.query_as_df(sparql)
    df = pdf  #.to_pandas()  #  including .to_pandas() breaks with papermill for reasons unknown at this time if to_pandas() is used, needed in my kglab conda env

    ib = True

    if 'severity' in df.columns:
        dfc = df.groupby('severity').count().reset_index().rename(columns={'path': 'Count'})
        ctst = pd.crosstab(df['message'], df['severity'],  margins = False , margins_name = 'Totals')

        s1 = str("Checking {} object(s)".format(len(dg) ))
        print(s1)
        print(ctst)

        sns.set(rc={'figure.figsize':(11.7,8.27)})
        sns.heatmap(ctst, annot=True, fmt=".0f", cmap = sns.cm.crest)
        plt.savefig('../../output/validation/{}_{}_heatmap_{}.png'.format(source, valname, date_time))
    else:
        print("No severity column found, all SHACL validations must have passed OR a processing error occurred upstream")
        ib = False

    # Save CSV
    df.to_csv("../../output/validation/{}_{}_table_{}.csv".format(source, valname, date_time))

    return ib

# build report
def buildReport(ib, sgurl, source, valname, date_time):
    #set up a stream
    stream = io.BytesIO()

    Story=[]

    styles = getSampleStyleSheet()
    HeaderStyle = styles["Heading1"]
    ParaStyle = styles["Normal"]
    PreStyle = styles["Code"]

    def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
        s = Spacer(0.2*inch, sep*inch)
        para = klass(txt, style)
        sect = [s, para]
        result = KeepTogether(sect)
        return result

    def pre(txt):
        s = Spacer(0.1*inch, 0.1*inch)
        p = Preformatted(txt, PreStyle)
        precomps = [s,p]
        result = KeepTogether(precomps)
        return result

    #  use for a file
    doc = SimpleDocTemplate("../../output/validation/{}_{}_{}.pdf".format(source, valname, date_time),pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    # use for object store
    # doc = SimpleDocTemplate(stream,pagesize=letter,
    #                         rightMargin=72,leftMargin=72,
    #                         topMargin=72,bottomMargin=18)

    if ib:
        logo = '../../output/validation/{}_{}_heatmap_{}.png'.format(source, valname, date_time)
        im = Image(logo, 4*inch, 3*inch)

    address_parts = ["RunID: {}".format(date_time), "Shape graph: {}".format(sgurl)]

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    # Create return address
    full_name = "Validation report"
    ptext = '%s' % full_name
    Story.append(Paragraph(ptext, styles["Heading1"]))

    # add date and time
    formatted_time = time.ctime()
    ptext = '%s' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    for part in address_parts:
        ptext = '%s' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = 'There were validation issues with the following resources.  They were not able to be checked'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    Story.append(Spacer(1, 12))

    ptext = 'This is a validation report using pySHACL to process the provided data graphs \
            against the noted shape graph.  A heat map of the results is seen below to provide \
            a quick over view.  However, the details are easier to leverage from the generated \
            CSV document that will come with this report. '

    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    # Story.append(Paragraph(s1, styles["Justify"]))
    # Story.append(Spacer(1, 12))

    # Story.append(Paragraph(str(ctst), styles["Code"]))
    # Story.append(Spacer(1, 12))

    # Add the image
    if ib:
        Story.append(im)

    ptext = 'For more information about validation please visit the project documentation.  \
            Details of the errors reported can be found in the shape file documentation page.'
    Story.append(Paragraph(ptext, styles["Justify"]))

    # Create return address
    Story.append(Spacer(1, 12))
    full_name = "Details"
    ptext = '%s' % full_name
    Story.append(Paragraph(ptext, styles["Heading1"]))

    ptext = 'Details of the detected violations and the associated reference node are found in the CSV \
            that accompany this report:  {}_{}_table_{}.csv '.format(source, valname, date_time)

    Story.append(Paragraph(ptext, styles["Justify"]))

    # make our document
    doc.build(Story)


if __name__ == '__main__':
    main()

## Look at Dave's code, he might have helper functions for this
## For now I am running as a github action so none of this is needed
## If run in Dagster or the like, this functionality might be nice to have
# write to S3 with buffer
#
# stream.seek(0)  # rewind the buffer
# pdf_buffer = stream.getbuffer()
#
# filename = "new.pdf"
# bucket_name = 'insert_bucket_name'
# object_name = bucket_name
#
# # Method 1: Object.put()
# s3 = boto3.resource('s3')
# object = s3.Object('my_bucket_name', 'my/key/including/filename.txt')
# object.put(Body=stream.getvalue())
#
# # Method 2: Client.put_object()
# client = boto3.client('s3')
# client.put_object(Body=stream.getvalue(), Bucket='my_bucket_name', Key='my/key/including/anotherfilename.txt')

# ## Write to S3
#
# convert the above to use stream buffer like in https://groups.google.com/g/django-users/c/Towha5_okco/m/mxFsycoHDQAJ?pli=1
#
# ```python
# from io import StringIO # python3; python2: BytesIO
# import boto3
#
# bucket = 'my_bucket_name' # already created on S3
# csv_buffer = StringIO()
# df.to_csv(csv_buffer)
# s3_resource = boto3.resource('s3')
# s3_resource.Object(bucket, 'df.csv').put(Body=csv_buffer.getvalue())
# ```

