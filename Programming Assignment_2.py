#!/usr/bin/env python
# coding: utf-8

# # Programming Assignment_2

# # 1. Write a Python program to convert kilometers to miles?

# In[1]:


def km_to_miles():
    try:
        km=int(input("Enter Distance/Length in Kilometers: "))
        miles=km*0.621371
        return miles
    except Exception as e:
        print(e)


# In[2]:


km_to_miles()


# # 2. Write a Python program to convert Celsius to Fahrenheit?

# In[5]:


def temperture_convert():
    try:
        C=int(input("Enter temperature in Celsius: "))
        F=(C*(9/5))+32
        return F
    except Exception as e:
        print(e)


# In[6]:


temperture_convert()


# # 3. Write a Python program to display calendar?

# In[13]:


import calendar
def calendar_show():
    try:
        yyyy=int(input("Enter Year in YYYY Format: "))
        mm=int(input("Enter Month in MM Format: "))
        print(calendar.month(yyyy,mm))
    except Exception as e:
        print(e)
    


# In[15]:


calendar_show()


# # 4. Write a Python program to solve quadratic equation?

# In[30]:


import cmath
def quadr():
    try:
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        c=int(input("Enter value of c: "))
        print("Problem statement will be: {0}x2+{1}x+{2}=0".format(a,b,c))
        d=(b**2)-(4*a*c)
        sq_d=cmath.sqrt(d)
        sol1=(-b+sq_d)/(2*a)
        sol2=(-b-sq_d)/(2*a)
        print("Solutions are {0} and {1}".format(sol1,sol2))
    except Exception as e:
        print(e)


# In[36]:


quadr()


# # 5.Write a Python program to swap two variables without temp variable?

# In[37]:


def swap():
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        try:
            a=a+b
            b=a-b
            a=a-b
            print("a={0} and b={1}".format(a,b))
        except Exception as e:
            print(e)


# In[38]:


swap()


# In[ ]:




