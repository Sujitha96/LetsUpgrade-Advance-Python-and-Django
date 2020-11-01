#!/usr/bin/env python
# coding: utf-8

# # How to make object as callable video __call__
# # from collections import Counter

# In[2]:


from collections import Counter
class MyCounter(Counter):
  def __call__(self,Counter):
    self.Counter=Counter
    print(Counter)
        
co1 = MyCounter()
co1("intel")


# In[ ]:




