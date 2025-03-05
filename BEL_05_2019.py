#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime 
from random import sample


# In[2]:


df=pd.read_csv(r"C:\Users\User\Downloads\Bel_05_2019.csv")


# In[3]:


df


# In[40]:


row1 = df.sample(n = 1000000)


# In[21]:


row1


# In[16]:


row1.sort_index(inplace=True)
row1


# In[18]:


row1.to_csv('Bel_05_2019.csv')


# In[4]:


df.drop('Unnamed: 0',axis=1,inplace=True)


# In[5]:


df.columns=['DateTime','street_identifier','count_truck','traffic_speed']


# In[6]:


df


# In[7]:


df.isnull().sum()


# In[8]:


df["DateTime"].fillna(df['DateTime'].ffill(),inplace=True)


# In[9]:


df.info()


# In[10]:


df.describe


# In[11]:


df['street_identifier']=df['street_identifier'].round(2)


# In[12]:


df['traffic_speed']=df['traffic_speed'].round(1)


# In[13]:


df


# In[14]:


df['DateTime']=pd.to_datetime(df['DateTime'])


# In[15]:


df['Year'] = df["DateTime"].dt.year
df['Month'] = df["DateTime"].dt.month_name()
df['Day'] = df["DateTime"].dt.day_name()

df['Hour'] = df["DateTime"].dt.hour
df['Minute'] = df["DateTime"].dt.minute
df['Second'] = df["DateTime"].dt.second


# In[16]:


df


# In[17]:


df.drop('DateTime',axis=1,inplace=True)


# In[18]:


df.to_csv('Bel_05_2019.csv')


# In[ ]:




