
# coding: utf-8

# In[21]:

import numpy as np
import scipy as sp
import scipy.stats


# ## Приклад 1

# In[ ]:

N = 9 # номер варіанту
sigma = 9
c = 3.4 


# $\sigma = 9$ - середньоквадратичне відхилення
# 
# $\gamma = 0.999$ - надійність

# In[121]:

x = np.array([3, 5, 7, 9])
ni = list(map(lambda f: f(N), [lambda x: x, lambda x: 2*x, lambda x: x+5, lambda x: x+1]))
n = sum(ni)
ni


# ### Середнє значення

# $\overline{x} = \frac{\sum x_i \cdot n_i}{n}$

# In[126]:

x_ = sum(x*ni) / n
x_


# ### Шуканий інтервал надійності

# $\left(\overline{x}-c_{\gamma} \frac{\sigma}{\sqrt{n}}; \overline{x}+c_{\gamma} \frac{\sigma}{\sqrt{n}}\right)$

# In[124]:

x_ - c * sigma / np.sqrt(n), x_ + c * sigma / np.sqrt(n)

