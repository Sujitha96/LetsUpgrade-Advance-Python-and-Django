#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
url="https://study-ccna.com/classes-of-ip-addresses/"
r=requests.get(url)
data_ip=r.text
ip=r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]"
list_ip=re.findall(ip,data_ip)
for each in list_ip:
  print(each)


# In[ ]:




