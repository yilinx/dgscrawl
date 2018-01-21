
# coding: utf-8

# Weekly automator
# 
# Performs a check daily of initialise the script weekly

# In[14]:


#!/usr/bin/python2.7

import datetime

d1 = datetime.date(2018,1,20)
d2 = datetime.date.today()

diff = d2-d1

if diff.days % 2 == 0:
    import pipeline
else:
    pass

