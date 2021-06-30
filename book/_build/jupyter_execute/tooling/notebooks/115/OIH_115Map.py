#!/usr/bin/env python
# coding: utf-8

# # OIH ISO 19139 to schema.org
# 
# Credit:
# 
# Steve Richards: https://github.com/usgin/metadataTransforms/tree/master/iso-19139-to-HTMLwSDO 
# 
# Refs:
# 
# * https://lxml.de/index.html
# * https://www.seadatanet.org/content/download/4534/file/CDI_ISO19139_full_example_12.2.0.xml 
# * https://raw.githubusercontent.com/usgin/metadataTransforms/master/iso-19139-to-HTMLwSDO/ISO19139ToSchemaOrgDataset1.0.xslt 
# 
# 

# In[1]:


get_ipython().system('pip install -q lxml')


# In[2]:


import lxml.etree as ET
import urllib.request


# In[3]:


get_ipython().system('wget https://raw.githubusercontent.com/usgin/metadataTransforms/master/iso-19139-to-HTMLwSDO/ISO19139ToSDODatasetStandalone1.0.xslt')


# In[6]:


dom = ET.parse("./CDI_ISO19139_full_example_12.2.0.xml")
xslt = ET.parse("./ISO19139ToSDODatasetStandalone1.0.xslt") ## convert to JSON-LD schema.org voc
transform = ET.XSLT(xslt)
newdom = transform(dom)


# In[7]:


print (newdom)

