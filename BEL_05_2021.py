#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np
from random import sample
import datetime


# In[3]:


df=pd.read_csv(r'D:\python project\archive (2)\Bel_05min_0506_1610_2021.csv')
df1=pd.read_csv(r'D:\python project\archive (2)\Bel_05min_1303_0606_2021.csv')


# In[4]:


df.columns=['datetime','street_identifier','traffic_count','traffic_speed']


# In[5]:


df1.columns=['datetime','street_identifier','traffic_count','traffic_speed']


# In[6]:


df1


# In[7]:


row1 = df.sample(n = 1000000)


# In[8]:


row2 = df1.sample(n = 1000000)


# In[9]:


df3=pd.concat([row1,row2])


# In[10]:


row3=df3.sample(n=1200000)


# In[11]:


row3


# In[18]:


row3.sort_index(inplace=True)
row3


# In[12]:


row3.info()


# In[13]:


row3.describe


# In[14]:


row3.isnull().sum()


# In[15]:


row3['street_identifier']=row3['street_identifier'].round(2)


# In[16]:


row3['traffic_speed']=row3['traffic_speed'].round(1)


# In[17]:


row3


# In[18]:


row3.sort_index(inplace=True)
row3


# In[20]:


row3['datetime']=pd.to_datetime(row3['datetime'])


# In[23]:


row3['Year'] =row3["datetime"].dt.year
row3['Month'] =row3["datetime"].dt.month_name()
row3['Day'] = row3["datetime"].dt.day_name()

row3['Hour'] = row3["datetime"].dt.hour
row3['Minute'] = row3["datetime"].dt.minute
row3['Second'] = row3["datetime"].dt.second


# In[24]:


row3


# In[26]:


row3.drop('datetime',axis=1,inplace=True)


# In[27]:


row3.to_csv('Bel_05_2021.csv')

