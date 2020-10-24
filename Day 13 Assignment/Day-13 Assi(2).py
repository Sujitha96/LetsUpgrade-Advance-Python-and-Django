#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
rep=os.walk('C:\\Users\\Sujji\\Assignment')
d1={}
for r,d,f in rep:
    for file in f:
        d1.setdefault(file,[]).append(r)
file_name=input('Enter the file name:')
for k,v in d1.items():
    if file_name.lower() in k.lower():
        for i in v:
            print(i)
            print('-'*50)
import os
print(os.getcwd())
os.chdir("G:\\LetsUpgrade\\test")
print(os.getcwd())

for file in os.listdir("."):
    if file.endswith(".png"):
        first_name=file.rsplit(".",1)[0]
        new_name=first_name+".jpg"
        print(new_name)
        os.rename(file,new_name)


# In[ ]:




