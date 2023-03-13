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

# Imports

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)  ## remove pandas future warning

from urllib.request import urlopen
import kglab
from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import pandas as pd
import seaborn as sns
from rdflib import Graph  #, plugin
import matplotlib.pyplot as plt
import boto3

# pyshack sends output to log along with the vars.  This suppresses that
import logging, sys
logging.disable(sys.maxsize)

import time, io
from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.platypus.tables import Table
from reportlab.platypus import SimpleDocTemplate
import argparse


# could also do anonymous read of a public bucket and loop and read
# each source in there.  Then apply the supplied shape.
# need name of the source and and the shape run (ie, geo, goihgeneral, etc.)


# Initialize args  parser
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--datagraph", help="datagraph to check")
parser.add_argument("-s", "--shapegraph", help="shacl shape graph to use")
# parser.add_argument("-f", "--file", help="Optional name of CSV file to save results to")

args = parser.parse_args()

dgurl = args.source
sgurl = args.name
# file = args.file

# dgurl = "http://ossapi.oceaninfohub.org/public/graphs/summonededmo_v1_release.rdf"
# sgurl =  "https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/code/notebooks/validation/shapes/oih_search.ttl"

namespaces = {
    "shacl":   "http://www.w3.org/ns/shacl#" ,
    "schema": "https://schema.org/"
    }

kg = kglab.KnowledgeGraph(
    name = "Schema.org based datagraph",
    base_uri = "https://example.org/id/",
    namespaces = namespaces,
    )


now = datetime.now()
date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

sf = urlopen(sgurl)
sg = sf.read()

df = urlopen(dgurl)
dg = df.read()

fna = []   # array to hold errors
try:
    g = Graph().parse(dg, format='n3')
    result = g.serialize(format='ttl')# .decode('utf-8')
    kg.load_rdf_text(result)
except:
    print("An exception occurred with {}".format(fn))
    fna.append(fn)

conforms, report_graph, report_text = kg.validate(
    shacl_graph=sg,
    shacl_graph_format="ttl"
)

kg.load_rdf_text(data=report_graph.save_rdf_text(), format="ttl")

sparql = """
SELECT  ?severity  ?constraint ?path ?message ?focus ?path ?value
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

if 'severity' in df.columns:
    dfc = df.groupby('severity').count().reset_index().rename(columns={'path': 'Count'})
    ctst = pd.crosstab(df['message'], df['severity'],  margins = False , margins_name = 'Totals')

    s1 = str("Checking {} object(s)".format(len(dg) ))
    print(s1)
    print(ctst)

    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.heatmap(ctst, annot=True, fmt=".0f", cmap = sns.cm.crest)
    plt.savefig('../../output/validation/heatmap_{}.png'.format(date_time))
else:
    print("No severity column found, all SHACL validations must have passed OR a processing error occurred upstream")


# Save CSV
df.to_csv("../../output/validation/validationReport_{}.csv".format(date_time))

# build report

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
doc = SimpleDocTemplate("../../output/validation/report_{}.pdf".format(date_time),pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

# use for object store
# doc = SimpleDocTemplate(stream,pagesize=letter,
#                         rightMargin=72,leftMargin=72,
#                         topMargin=72,bottomMargin=18)

logo = '../../output/validation/heatmap_{}.png'.format(date_time)
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
for part in fna:
    ptext = '%s' % part.strip()
    Story.append(Paragraph(ptext, styles["Code"]))

Story.append(Spacer(1, 12))

ptext = 'This is a validation report using pySHACL to process the provided data graphs \
        against the noted shape graph.  A heat map of the results is seen below to provide \
        a quick over view.  However, the details are easier to leverage from the generated \
        CSV document that will come with this report. '

Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

Story.append(Paragraph(s1, styles["Justify"]))
Story.append(Spacer(1, 12))

# Story.append(Paragraph(str(ctst), styles["Code"]))
# Story.append(Spacer(1, 12))

# Add the image
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
        that accompany this report:  validationReport_{}.csv '.format(date_time)

Story.append(Paragraph(ptext, styles["Justify"]))

# make our document
doc.build(Story)

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
