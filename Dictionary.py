#!/usr/bin/env python
# coding: utf-8

# In[5]:


countryLeaders={"PL":"Duda", "US":"Biden"}


# In[6]:


print(countryLeaders)


# In[7]:


print(countryLeaders["US"])


# In[9]:


countryLeaders["DE"] = "Schulz"
print(countryLeaders)


# In[11]:


countryLeaders.setdefault("FR", "Macron")
print(countryLeaders)


# In[13]:


print(countryLeaders.get("RU"))


# In[15]:


newLeaders = {"RU": "Putin", "DE" : "Merkel"}


# In[16]:


countryLeaders.update(newLeaders)
print(countryLeaders)


# In[17]:


# LABORKI


# In[41]:


channels = { "Google" : 1480, "Email" : 300, "Natural Traffic" : 440, "TV Spot" : 700}
print(channels)


# In[42]:


print(channels["Email"])


# In[43]:


channelsUpdate = {"Natural Traffic":520, "News":600}


# In[44]:


channels.update(channelsUpdate)
print(channels)


# In[45]:


print(channels.keys())


# In[46]:


print(channels.pop("Email"))
print(channels)


# In[ ]:




