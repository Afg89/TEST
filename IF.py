#!/usr/bin/env python
# coding: utf-8

# In[24]:


age = 27
isDrunk = True
isRestrictedArea = False


# In[25]:


if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult, you can buy alcohol")
else:
    print("Sorry, you can't buy alcohol")
    



# In[26]:


#LABORKI


# In[64]:


minLike = 500
minShare = 200

actualLike = 600
actualShare = 100


# In[65]:


if actualLike >= minLike and actualShare >= minShare:
    print("We made it, start promo!")
else:
    print("Sorry, try again tommorow!")


# In[42]:


#LABORKI 2


# In[70]:


isWeekend = True
isPizzaOrdered = True
isBigDrinkOrdered = True


# In[71]:


if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("Congratulations, you receive a bonus voucher for free burger")
else:
    print("Sorry, promotion is valid only during non-weekend days")


# In[55]:


#LABORKI 3


# In[61]:


diskSize = 45
diskSizeUsed = 1
fileSize = 12.3


# In[62]:


if diskSize - diskSizeUsed >= fileSize:
    print("You can download the file")
else:
    print("Sorry, not enough disk space!")


# In[ ]:




