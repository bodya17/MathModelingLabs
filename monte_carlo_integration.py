
# coding: utf-8

# ## find area under function $x^2$ in [0, 4]
# 

# In[2]:

import plotly
from plotly.graph_objs import Scatter
import numpy as np
import sympy


# In[3]:

plotly.offline.init_notebook_mode()


# In[4]:

x = sympy.Symbol('x')


# In[5]:

sympy.N(sympy.integrate(x*sympy.sin(x), (x, 0, 4))*1.0)


# In[6]:

N = 10000
start = 0
end = 16


# In[7]:

def f(x): return x**np.sin(x)


# In[8]:

x_rand = np.random.random(N)*16
y_rand = np.random.random(N)*16


# In[9]:

x_vals = np.linspace(start, end, 1000)


# In[ ]:




# In[10]:

plotly.offline.iplot([
    Scatter(x=x_rand, y=y_rand, mode="markers"),
    Scatter(x=x_vals, y=f(x_vals))
])


# In[11]:

def area():
    points = list(zip(x_rand, y_rand))
    under_curve = len(list(filter(lambda point: point[1] < f(point[0]), points))) # under curve and above x-axis
    return under_curve * (end - start) *16 / N


# In[12]:

area()


# In[13]:

# True value
sympy.N(sympy.integrate(x**sympy.sin(x), (x, start, end)) *1.0)


# In[14]:

points = list(zip(x_rand, y_rand))
under_curve = list(filter(lambda point: point[1] < f(point[0]), points)) # under curve and above x-axis


# In[16]:

x_under =list(map(lambda point: point[0], under_curve))


# In[18]:

y_under =list(map(lambda point: point[1], under_curve))


# In[20]:

plotly.offline.iplot([
    Scatter(x=x_under, y=y_under, mode="markers"), 
    Scatter(x=x_vals, y=f(x_vals))
])


# In[ ]:



