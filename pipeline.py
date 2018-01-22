
# coding: utf-8

# ## Pipeline
# <br\>
# Please ensure that the most updated working metadata extraction files are saved as 
# <i>
# * `packageEX.py`, 
# * `resourceEX.py`, 
# * `schema.py`, 
# * `joinSRC.py`, 
# * `zipcsv.py`
# * `sendmail.py`
# </i> in the same directory as <i>`pipeline.py`</i>
# <br\>
# <br\>
# ##### IMPORTANT: DO NOT AMEND THE ABOVE PY FILES DIRECTLY!!! DEVELOPE THROUGH JUPYTER NOTEBOOK FOR CONSISTENCY AND DOCUMENTATION

# Step 1: Run DGS Package Metadata Extraction
# <br\>
# In this step, we are importing the package metadata extraction function. This first step is important as the data from DGS will be crawlled and stored as a dictionary `dgs_crawl`. This dictionary is used by all other extraction functions (ie Resource and Schema).

# In[1]:


import packageEX as step1

step1.write_pkg_metadata()


# Step 2: Run DGS Resource Metadata Extraction
# <br\>
# In this step, we are importing the resource metadata extraction function.

# In[2]:


import resourceEX as step2

step2.write_resource_metadata()


# Step 3: Run DGS Schema Metadata Extraction
# <br\>
# In this step, we are importing the schema metadata extraction function.

# In[3]:


import schemaEX as step3

step3.write_schema_metadata()


# Step 4: Left join Package csv to Resource csv

# In[4]:


import joinSRC as step4

step4.joinsrc()


# Step 5: Zip up the joined csv file for sending

# In[5]:


import zipcsv as step5

step5.zipcsv()


# Step 6: Send email to list of recepients. In this step, the send mail function is already built in. So no function is called in this step.

# In[6]:


import sendmail as step6

