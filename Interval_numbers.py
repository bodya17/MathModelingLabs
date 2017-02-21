
# coding: utf-8

# In[2]:

from mpmath import mpi


# In[3]:

a = mpi([0,1])


# In[4]:

def f0(x):
    return x**2 - x


# In[5]:

def f1(x):
    return x*(x - 1)


# In[6]:

def f2(x):
    return 1/4 - (x - 1/2)**2


# In[7]:

def f3(x):
    return 1/4 - (x - 1/2)*(x - 1/2)


# In[8]:

a / a


# In[9]:

f1(a)


# In[10]:

f2(a)


# In[11]:

f3(a)


# In[12]:

a = mpi([2, 4])
b = mpi([1, 3])


# In[15]:

a - b


# In[ ]:



