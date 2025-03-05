#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from datetime import datetime


# In[2]:


And1=pd.read_csv(r"D:\project 2\archive (2)\And_05min_0101_0103_2019.csv")


# In[3]:


And1


# In[5]:


And1.columns=['DateTime','street_traffic','count_truck','traffic_speed']


# In[6]:


And1


# In[7]:


And1.info()


# In[8]:


And1.describe


# In[9]:


And1.head()


# In[10]:


And1.isnull().sum()


# In[11]:


And1["DateTime"].fillna(And1['DateTime'].ffill(),inplace=True)


# In[12]:


And1.tail()


# In[13]:


And1.isnull().sum()


# In[14]:


count = (And1['DateTime'] == 0).sum()


# In[15]:


count


# In[16]:


count = (And1['street_traffic'] == 0).sum()


# In[17]:


count


# In[18]:


count = (And1['count_truck'] == 0).sum()


# In[19]:


count


# In[20]:


count = (And1['traffic_speed'] == 0).sum()


# In[21]:


count


# In[22]:


And1[~(And1['street_traffic'] == 0)].all(axis=1)


# In[23]:


street_traffic_col =And1['street_traffic']
street_traffic_col.replace(to_replace = 0, value = street_traffic_col.mean(), inplace=True)


# In[24]:


count_truck_col =And1['count_truck']
count_truck_col.replace(to_replace = 0, value = count_truck_col.mean(), inplace=True)


# In[25]:


traffic_speed_col =And1['traffic_speed']
traffic_speed_col.replace(to_replace = 0, value = traffic_speed_col.mean(), inplace=True)


# In[26]:


And1


# In[27]:


And1.to_csv('And_5min_0101_2019.csv')

