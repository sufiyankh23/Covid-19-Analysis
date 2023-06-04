#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("SpotifyFeatures.csv")
data.head()


# In[4]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


data.describe().transpose()


# In[7]:


# most popular songs

data.sort_values("popularity",ascending=False).head(10)


# In[8]:


# least popular songs

data.sort_values("popularity",ascending=True).head(10)


# In[9]:


data["duration_ms"] = data["duration_ms"].apply(lambda x : round(x/1000))
data.drop("duration_ms",inplace=True,axis=1)


# In[10]:


data.head(2)


# In[ ]:




