#!/usr/bin/env python
# coding: utf-8

# In[1]:


for number in range(1,21):
    if number %2 == 0:
        print ("Number %2d is %s" % (number,"even"))
    else:
        print ("Number %2d is %s" % (number,"odd"))


# In[2]:


stringA = "+---+---+---+---+"
stringB = "|   |   |   |   |"


# In[20]:


for number in range(9):
    print(stringA)


# In[19]:


for number in range(10):
    if number %2 == 0:
        print(stringB)
    else: 
        print(stringA)


# In[12]:


for number in range (1,10):
    print( number * "x")


# In[18]:


for number in range(10):
    if number %2 == 0:
        print (number * "x")
    else:
        print (number * "o")


# In[ ]:




