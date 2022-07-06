#!/usr/bin/env python
# coding: utf-8

# In[1]:


countries= ["PL","GB","USA"]


# In[2]:


print(countries)


# In[4]:


print(countries[1])


# In[5]:


countries[1]="DE"


# In[6]:


print(countries)


# In[7]:


countries.append("FR")


# In[9]:


countries.insert(4,"ESP")


# In[10]:


print(countries)


# In[11]:


countries.sort()


# In[12]:


print(countries)


# In[13]:


countries.reverse()


# In[15]:


print(countries)


# In[16]:


print(countries.pop(3))


# In[17]:


print(countries)


# In[19]:


countries.index("DE")


# In[20]:


countries.append("DE")


# In[21]:


print(countries)


# In[22]:


print(countries.count("DE"))


# In[24]:


newList=["NL","PT"]


# In[25]:


countries.extend(newList)


# In[26]:


print(countries)


# In[30]:


print(countries.sort())


# In[31]:


countries.sort()


# In[38]:


print(countries)


# In[40]:


countries = ['USA', 'PL', 'FR', 'DE', 'DE', 'NL', 'PT']


# In[41]:


print(countries)


# In[42]:


countriesCopy = countries.copy()


# In[43]:


print(countriesCopy)


# In[44]:


countries.clear()


# In[45]:


print(countries)
print(countriesCopy)


# In[46]:


#LABORKI


# In[51]:


hitsTitles = ["BROTHERS IN ARMS", "BOHEMIAN RHAPSODY", "STAIRWAY TO HEAVEN", "RIDER ON THE STORM", "WISH YOU WERE HERE"]


# In[53]:


hitsTitles.append("CHILD IN TIME")
hitsTitles.append("AGAIN") 


# In[54]:


hitsTitles.insert(2, "HOTEL CALIFORNIA")


# In[55]:


print(hitsTitles)


# In[56]:


hitsTitles.insert(0, "THE SOUND OF SILENCE")


# In[57]:


print(hitsTitles)


# In[58]:


print(hitsTitles.index("HOTEL CALIFORNIA"))


# In[59]:


hitsTitles.remove("HOTEL CALIFORNIA")


# In[60]:


hitsTitles[0]="ENJOY THE SILENCE"


# In[79]:


hitsToRead = hitsTitles.copy()
print(hitsToRead)


# In[80]:


hitsToRead.reverse()
print(hitsToRead)


# In[81]:


hitsToRead.sort()
print(hitsToRead)


# In[82]:


print(hitsToRead.pop(0))
print(hitsToRead.pop(1))
print(hitsToRead)


# In[84]:


additionalSongs= ["NOTHING COMPARES 2 U", "WISH YOU WERE HERE"]


# In[86]:


hitsToRead.extend(additionalSongs)
print(hitsToRead)


# In[89]:


print("\"WISH YOU WERE\" HERE będzie zagrane", hitsToRead.count("WISH YOU WERE HERE"), "razy")
print("natomiast \"RIDERS ON THE STORM\" będzie zagrane", hitsToRead.count("RIDERS ON THE STORM"), "razy")


# In[91]:


# koniec audycji
hitsToRead.clear()
print(hitsToRead)

