#!/usr/bin/env python
# coding: utf-8

# In[17]:


number = 1
previousNumber = 0

while number < 50:
    print(previousNumber,"+", number,"=", number+previousNumber)
    previousNumber=number
    number+=1


# In[46]:


import random
myNumber = random.randint(0,20)
trials = 0
guess = -1

print("Hello! Let's play a game! Try to guess my number")


while guess != myNumber:

    guess = int(input())
    trials+=1

    if guess== myNumber:
        print("Congratulation! My number is:", myNumber, "You quessed it with", trials, "trial(s)")
    elif guess > myNumber:
        print("Sorry, my number is lower than", guess,  "try again!")
    else: 
        print("Sorry, my number is higher than", guess, "try again!")

     



# In[ ]:




