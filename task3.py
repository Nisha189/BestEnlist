#!/usr/bin/env python
# coding: utf-8

# In[2]:


d1={'a':1,'b':2}
d2={'c':3,'d':4}
d=d1.copy()
d.update(d2)
print(d)


# In[3]:


d={'a':1,'b':2,'c':3}
if 'b' in d:
    del d['b']
    print(d)


# In[4]:


l1=['Tamilnadu','Kerala','Karnataka']
l2=['Chennai','Trivandrum','Bangalore']
d=dict(zip(l1,l2))
print(d)


# In[5]:


s1=set([2,4,6,8,10,12,14])
print(len(s1))


# In[6]:


s1={2,4,6,8,10}
s2={8,9,10,11,12}
print(s1)
print(s2)
print(s1-s2)


# In[ ]:




