#!/usr/bin/env python
# coding: utf-8

# # pySHACL testing
# 
# Ocean Info Hub SHACL validation on S3(minio) objects
# 
# ## Flow
# 
# * get an object (use the dask notebook)
# * process the object against OIH SHACL shapes
# 

# In[1]:


get_ipython().run_cell_magic('capture', '', "!pip install pyshacl\n!pip install 'PyLD>=2.0.3'\n!pip install flatten_json\n!pip install 'fsspec>=0.3.3'\n!pip install s3fs\n!pip install boto3\n!pip install seaborn\n!pip install dask")


# In[2]:


def label_status (row):
  result = row['http://www.w3.org/ns/shacl#resultSeverity']
  if result == "nan":
    return "NA" 
  elif "Warning" in result:
    return "Warning"
  elif "Violation" in result:
    return "Violation"  
  else:
    return result

def source_shape (row):
  result = row['http://www.w3.org/ns/shacl#sourceShape']
  if type(result) is list: 
    return result[0]['@id']
  else:
    return "NA"


# ## Gleaner Data
# 
# First lets load up some of the data Gleaner has collected.  This is just simple data graph objects and not any graphs or other processed products from Gleaner. 

# In[3]:


# Set up our S3FileSystem object
import s3fs 

oss = s3fs.S3FileSystem(
      anon=True,
      key="",
      secret="",
      client_kwargs = {"endpoint_url":"https://oss.collaborium.io"}
   )


# In[4]:


# Create the Dask tasks..   created..  not run..  
import json
import dask, boto3
import dask.dataframe as dd

@dask.delayed()
def read_a_file(fn):
    # or preferably open in text mode and json.load from the file
    with oss.open(fn, 'rb') as f:
        #return json.loads(f.read().replace('\n',' '))
        return json.loads(f.read().decode("ascii", "ignore").replace('\n',' '))

# List of buckets to work with..   if you don't know them, you could print out above
buckets = ['gleaner/summoned/oceanexperts'] 
filenames = []

for d in range(len(buckets)):
  print("indexing {}".format(buckets[d]))
  f = oss.ls(buckets[d])
  filenames += f

#filenames = oss.cat('gleaner/summoned/opentopo', recursive=True)
output = [read_a_file(f) for f in filenames]
print(len(filenames))
# print(filenames)


# In[13]:


get_ipython().run_cell_magic('time', '', 'from pyshacl import validate\nfrom os import path\nfrom pandas import json_normalize\nimport pandas as pd\nimport json\nimport rdflib\nimport seaborn as sns\nimport matplotlib.pyplot as plt\n\ngldf = pd.DataFrame(columns=["id", "status", "shape"])\n\nfor ndx in range(len(output)):\n# for ndx in range(10):\n    \n  if "/.jsonld" not in filenames[ndx] :\n    try:\n      jld = output[ndx].compute()  ## Now pull from dask..   In REAL version, move this logic into Dask!  to get the parallel approach\n    except:\n      print(filenames[ndx])\n      print("Doc has bad encoding")\n\n    jd = json.dumps(jld, sort_keys=True, indent=4)\n        \n    try:\n      conforms, v_graph, v_text = validate(jd, \n                shacl_graph=\'./oih_learning.ttl\', \n                data_graph_format="json-ld", \n                shape_graph_format="ttl", \n                inference=\'none\', \n                serialize_report_graph="json-ld")\n      \n      gd = v_graph.decode("ascii") \n      df = pd.DataFrame(json.loads(gd))\n      conforms = df["http://www.w3.org/ns/shacl#conforms"]\n      tf = conforms[0][0][\'@value\']\n\n      if "False" in str(tf):\n        df[\'http://www.w3.org/ns/shacl#resultSeverity\'] = df[\'http://www.w3.org/ns/shacl#resultSeverity\'].astype(str)\n        df[\'ID\'] = filenames[ndx] #  \'Object:{}\'.format(ndx) \n        df[\'Status\'] = df.apply (lambda row: label_status(row), axis=1)\n        df[\'Shape\'] = df.apply (lambda row: source_shape(row), axis=1)\n\n        data = [df["ID"], df["Status"], df[\'Shape\']]\n        headers = ["id", "status", "shape"]\n        df3 = pd.concat(data, axis=1, keys=headers)\n        gldf = gldf.append(df3, ignore_index=True)\n      elif "True" in str(tf):\n        df[\'ID\'] = filenames[ndx] #  \'Object:{}\'.format(ndx) \n        df[\'Status\'] = "Valid"\n        df[\'Shape\'] = "AllPassed"\n\n        data = [df["ID"], df["Status"], df[\'Shape\']]\n        headers = ["id", "status", "shape"]\n        df3 = pd.concat(data, axis=1, keys=headers)\n        gldf = gldf.append(df3, ignore_index=True)  \n    \n#       print("------------------")\n#       print(conforms)\n#       print(v_graph)\n#       print(v_text)\n\n    except:\n      print("ERROR")\n      df = pd.DataFrame()\n      df[\'ID\'] = filenames[ndx] #  \'Object:{}\'.format(ndx) \n      df[\'Status\'] = "ErrorProcessing"\n      df[\'Shape\'] = "ErrorProcessing"\n\n      data = [df["ID"], df["Status"], df[\'Shape\']]\n      headers = ["id", "status", "shape"]\n      df3 = pd.concat(data, axis=1, keys=headers)\n      gldf = gldf.append(df3, ignore_index=True)\n      print("PySHACL decode error: {}",format(filenames[ndx]))\n')


# In[14]:


gldf.info() 
gldf.head(5)


# In[15]:


pd.value_counts(gldf['shape'])


# In[16]:


pd.value_counts(gldf['shape']).plot.barh()
plt.xticks(rotation=45)


# In[ ]:




