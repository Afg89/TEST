#!/usr/bin/env python
# coding: utf-8

# In[1]:


helloMessage = "Hello %s!"


# In[4]:


print(helloMessage %"Kate")
print(helloMessage %"Chris")


# In[5]:


helloMessage = "Hello {0:s}!"


# In[6]:


print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))


# In[7]:


helloMessage = "%s has %d %s"


# In[10]:


print(helloMessage % ("Kate", 1, "animal"))
print(helloMessage %("Chris", 100000, "$"))


# In[11]:


helloMessage = " {0:s} has {1:d} {2:s}"


# In[12]:


print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, "$"))


# In[19]:


line = "{0:20s} costs {1:6d} €"


# In[20]:


print(line.format("ICE CREAM",3))
print(line.format("TRIP TO VENICE",119))
print(line.format("PIZZA HAWAII",6))


# In[21]:


line = "{0:20s} {1:6d} "


# In[22]:


print(line.format("ICE CREAM",3))
print(line.format("TRIP TO VENICE",119))
print(line.format("PIZZA HAWAII",6))


# In[ ]:




