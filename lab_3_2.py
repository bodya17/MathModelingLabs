
# coding: utf-8

# In[9]:

import numpy as np
import scipy as sp
import scipy.stats


# In[10]:

N = 9


# In[11]:

x = [2 + N/10, 2.1 + N/10, 1.9 + N/10, 2.15 + N/10, 2.23 + N/10, 2.2+N/10]


# In[12]:

x


# In[24]:

n = len(x)
n


# In[25]:

x_ = np.mean(x)
x_ # середнє значення


# In[41]:

s = np.std(x)
s # відхилення


# In[42]:

t = 2.571 # з таблиці розподілу Стюдента


# ### Обчислюємо 0,95-надійний інтервал для математичного сподівання
# $\left(\overline{x}-t_{\gamma,n-1} \frac{S}{\sqrt{n}}
# ; \overline{x}+t_{\gamma,n-1} \frac{S}{\sqrt{n}}\right)$

# In[44]:

(x_ - t * s / np.sqrt(n-1), x_ + t * s / np.sqrt(n-1))


# ### Обчислюємо 0,95-надійний інтервал для дисперсії $\sigma^2 = D\xi$
# $\left(\frac{n\cdot s^2}{\chi^2_{\frac{1+\gamma}{2}, n-1}}; \frac{n\cdot s^2}{\chi^2_{\frac{1-\gamma}{2}, n-1}}\right)$

# In[45]:

t1 = scipy.stats.chi2.isf((1-0.95)/2, n-1)
t1


# In[46]:

t2 = scipy.stats.chi2.isf((1+0.95)/2, n-1)
t2


# ### Шуканий інтервал надійності для дисперсії

# In[48]:

n * s**2 / t1, n * s**2 / t2


# In[ ]:



