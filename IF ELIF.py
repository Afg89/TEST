#!/usr/bin/env python
# coding: utf-8

# In[27]:


age = 22
isDrunk = True
isRestrictedArea = False


# In[28]:


if age < 18:
    print("Sorry, you are too young to buy alcohol")
else:
    if isDrunk:
        print("Sorry, you are drunk, we won\'t sell you alcohol")
    else:
        if isRestrictedArea:
            print("Sorry, you can\'t buy alcohol in this area - it\'s forbidden")
        else:
                print("We can sell you alcohol, what is your need?")


# In[29]:


if age <18:
    print("Sorry, you are too young to buy alcohol")
elif isDrunk:
    print("Sorry, you are drunk, we won\'t sell you alcohol")
elif isRestrictedArea:
    print("Sorry, you can\'t buy alcohol in this area - it\'s forbidden")
else:
    print("We can sell you alcohol, what is your need?")


# In[30]:


# LABORKI


# In[74]:


minLike = 500
minShare = 100

actualLike = 500
actualShare = 99


# In[75]:


if actualLike < minLike:
    print("Sorry, not enough likes, try again tommorow!")
else:
    if actualShare < minShare:
        print("Sorry, not enough shares, try again tommorow!")
    else:
            print("We made it, starting promo!")


# In[76]:


if actualLike >= minLike and actualShare >= minShare:
    print("We made it, starting promo!")
elif actualLike < minLike:
    print("Sorry, not enough likes, try again tommorow!")
elif actualShare < minShare:
    print("Sorry, not enough shares, try again tommorow!")


# In[77]:


# LABORKI 2


# In[110]:


isWeekend = False
isPizzaOrdered = False
isBigDrinkOrdered = False


# In[111]:


if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("Congratulations, you receive a bonus voucher for free burger")
else:
    if  isWeekend:
        print("Sorry, promotion is valid only during non-weekend days")
    else:
        print("To get a voucher for free burger conider buying a pizza or a big drink")
                    


# In[112]:


if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("Congratulations, you receive a bonus voucher for free burger")
elif isWeekend:
    print("Sorry, promotion is valid only during non-weekend days")
else:
    print("To get a voucher for free burger conider buying a pizza or a big drink")


# In[ ]:




