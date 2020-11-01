#!/usr/bin/env python
# coding: utf-8

# # write a program to find the given string in the root directory that contains a text file
# # 1. In a recursive manner (case in sensitive )
# # 2. only in the root directory
# # use command line arguments.
# # program_name -ri string root_dir (recursive)
# # program_name -si string root_dir (root director )
# # The output which file and line contains the string

# In[1]:


import os
root="G:\\LetsUpgrade\\Project"
for root,dir,files in os.walk(root):
  for s in files:
    path=root+"\\"+s
    print(path)

def check_string_in_file(f, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False
    with open(f) as myFile:
        for num, line in enumerate(myFile, 1):
             if lookup in line:
               print('found at line:', num)


# In[ ]:




