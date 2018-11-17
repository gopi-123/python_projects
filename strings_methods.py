
# coding: utf-8

# In[1]:


'''
string inbuilt methods - functions that belong to class String
syntax: "string".function()
''' 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:22:33 2018

@author: gopinath
"""


#format method
"Hi I am {}".format("name")


# In[2]:


#count number of a's in string
"Happy Birthday".count("a")


# In[3]:


#count number of a's in string
x="Happy Birthday Ganesh"
x.count("a")


# In[4]:


x = "HAPPY BIRTHDAY"

#lower method
x.lower()


# In[5]:


#x is immuatable, that is it cannot be changed but only it can be replaced
#x is still in Orignal Upper case
x


# In[6]:


x=x.lower()


# In[7]:


#x is immuatable, that is it cannot be changed but only it can be replaced
print(x)


# In[8]:


#capitalize
x.capitalize()


# In[9]:


#Title
x.title()


# In[10]:


#lowercase  -- gives condition TRUE OR FALSE
x.islower()


# In[11]:


#
x.isupper()


# In[12]:


#is alpha is false because space between HAPPY & BIRTHDAY is considered as digit
x.isalpha()




# In[13]:


#space is not alphabet its digit
" ".isalpha()


# In[14]:


"abv".isalpha()


# In[15]:


"1234".isdigit()


# In[16]:


x="Bonus"
#postion of o in string
x.index("o")


# In[17]:


x.find("ou")


# In[18]:


#Big O is missing
x.find("O")


# In[19]:


x.find("o")


# In[ ]:


#2 space + john  =6 characters
name =input("what is your name?")
print(len(name))


# In[ ]:


#strip fiction would remove all spaces
name =input("what is your name?").strip()
print(len(name))

