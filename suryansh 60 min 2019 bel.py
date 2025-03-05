#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[6]:


df1=pd.read_csv(r"F:\New folder (2)\bel 60min_2019.csv")


# In[7]:


df1


# In[8]:


df1['date'] = pd.to_datetime(df1['DateTime']).dt.date
df1['time'] = pd.to_datetime(df1['DateTime']).dt.time


# In[9]:


df=df1.sample(n=1500000)


# In[10]:


df.sort_index(inplace=True)
df


# In[11]:


s=df.groupby('street_identifier')['count_truck','traffic_speed'].mean().round(2)


# In[12]:


s


# In[13]:


x=s.tail(5)
street_traffic=x.groupby('street_identifier')['count_truck'].sum()
sns.barplot(x=street_traffic.index, y=street_traffic.values,color='g')
plt.xlabel('street_id',color='r',size=21)
plt.ylabel('traffic',color='r',size=21)
street_traffic


# In[32]:


d=s.tail(20)
grouped_data = d.groupby('street_identifier')['count_truck'].sum().reset_index()
plt.plot(grouped_data['street_identifier'], grouped_data['count_truck'])
plt.title('Count of Trucks by Street')
plt.xlabel('Street ID')
plt.ylabel('Count of Trucks')
plt.show()


# In[27]:


d=df.sample(n=1000)
r=d.head(10)
r.plot( 'Day' , 'street_identifier' )

