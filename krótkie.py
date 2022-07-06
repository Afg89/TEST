#!/usr/bin/env python
# coding: utf-8

# In[1]:


tax = (4, 7,8,23)


# In[2]:


print(tax)


# In[4]:


print(tax[2])


# In[5]:


print(max(tax))


# In[6]:


taxList = list(tax)
print(taxList)


# In[7]:


taxList.append(30)


# In[8]:


newTax = tuple(taxList)


# In[9]:


print(newTax)


# In[10]:


(tax1, tax2, tax3, tax4) = tax


# In[11]:


print(tax1, tax2, tax3, tax4)


# In[17]:


a=1
b=10
print("a =", a, "\tb =", b)


# In[18]:


#temp = a
#a= b
#b = temp
print("a =", a, "\tb =", b)


# In[19]:


(a,b)=(b,a)
print("a =", a, "\tb =", b)


# In[20]:


#LABORKI


# In[27]:


marketing = ["loyality program", "client promotion", "market research"]
print(marketing)


# In[28]:


marketing.append("public relations")
print(marketing)


# In[36]:


marketing[3]


# In[37]:


marketing.insert(2, "investor relations")
print(marketing)


# In[38]:


emailMarketing = marketing.copy()
print(marketing)
print(emailMarketing)


# In[39]:


emailMarketing.sort()
print(emailMarketing)


# In[40]:


internalEmails = ["internal communication"]


# In[42]:


emailMarketing.extend(internalEmails)
print(emailMarketing)


# In[43]:


newList = tuple(emailMarketing)
print(newList)


# In[ ]:




