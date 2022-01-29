#!/usr/bin/env python
# coding: utf-8

# # Programming Assignment_1

# # Write a Python program to print &quot;Hello Python&quot;?

# In[1]:


print("Hello Python")


# # Write a Python program to do arithmetical operations addition and division.?

# In[11]:


def operation():   
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    try:
        add=a+b
        div=a/b
        return "Addition: ",add,"Division: ",div
    except:
        print("Division Error")


# In[12]:


operation()


# # Write a Python program to find the area of a triangle?

# In[13]:


def triangle_area(b,h):
    try:
        area=(b*h)/2
        return area
    except Exception as e:
        print(e)


# In[16]:


triangle_area(25,6)


# # Write a Python program to swap two variables?

# In[19]:


def swap(a,b):
    try:
        print("Before swap a =",a," b=",b)
        temp=a
        a=b
        b=temp
        print("After swap a =",a," b=",b)
    except Exception as e:
        print(e)


# In[20]:


swap(12,4)


# # Write a Python program to generate a random number?

# In[25]:


import random
def random_generator():
    print(random.randint(0,9))


# In[28]:


random_generator()


# In[ ]:




