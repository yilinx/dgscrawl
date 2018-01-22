
# coding: utf-8

# Zip CSV
# 
# In this module, we will zip up the joined CSV file in prep for mail sending.

# In[4]:


# Check if the previous zip file exist. If so, remove it.

from pathlib2 import Path
import os
import unicodecsv as csv

filechk = ['DGS-extract.zip']

for ifile in filechk:
    my_file = Path(ifile)
    if my_file.is_file():
        os.remove(ifile)


# In[5]:


import datetime
import zipfile

# Prepares to zip the file
def zipcsv():
    zf = zipfile.ZipFile('DGS-extract.zip', mode='w')
    zf.write('pkg-resource.csv')
    zf.close()
    
    print "Complete zipping metadata!!"

    now = datetime.datetime.now()

     # Writes a log file upon success
    with open('log.txt','a') as f2:
        writer = csv.DictWriter(f2, fieldnames=['Date','Action'], encoding='utf-8')
        writer.writerow({'Date':now, 'Action':'zipcsv()'})
        f2.close()

