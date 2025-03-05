#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df_30=pd.read_csv(r"bxlbeand_30min_2019.csv")


# In[4]:


df_30


# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[6]:


month_traffic=df_30.groupby('Month')['count_truck'].sum()
fig = px.bar(x=month_traffic.index, y=month_traffic.values,labels=dict(x="Month_name", y="sum_traffic"))
fig.show()


# In[7]:


fig = px.area(x=month_traffic.index, y=month_traffic.values,labels=dict(x="Month_name", y="sum_traffic"))
fig.show()


# In[8]:


month_traffic_mean=df_30.groupby('Month')['count_truck'].mean()


# In[9]:


fig = px.area(x=month_traffic_mean.index, y=month_traffic_mean.values,labels=dict(x="Month_name", y="traffic"))
fig.show()


# In[10]:


day_traffic=df_30.groupby('Day')['count_truck'].sum()


# In[11]:


fig = px.bar(x=day_traffic.index, y=day_traffic.values,labels=dict(x="Day_name", y="traffic"))
fig.show()


# In[12]:


street_traffic=df_30.groupby('street')['count_truck'].sum()


# In[13]:


fig = px.bar(x=street_traffic.index, y=street_traffic.values,labels=dict(x="Streets", y="traffic"))
fig.show()


# In[14]:


sns.barplot(x=street_traffic.index, y=street_traffic.values,color='g')
plt.xlabel('street')
plt.ylabel('traffic')


# In[16]:


df_30.head(1)


# In[17]:


plt.figure(figsize=(20,10))
weekdays_traffic=df_30.groupby('weekdays')['count_truck'].sum()
sns.barplot(x=weekdays_traffic.index, y=weekdays_traffic.values,color='orange')
plt.xlabel('week_no')
plt.ylabel('traffic')


# In[18]:


d=df_30.head(5)
d


# In[19]:


d['date'] = pd.to_datetime(d['DateTime']).dt.date
d['time'] = pd.to_datetime(d['DateTime']).dt.time


# In[20]:


d


# In[21]:


import datetime


# In[22]:


df_30['DateTime']=pd.to_datetime(df_30['DateTime'])


# In[23]:


df_30.isna().sum()


# In[24]:


df_30.fillna(method='ffill',inplace=True)


# In[25]:


df_30.isna().sum()


# In[26]:


d=df_30[(df_30['Hour']>=6) & (df_30['Hour']<=29)]


# In[27]:


d.head(3)


# In[28]:


day_time=d.groupby('Hour')['count_truck'].sum()
sns.barplot(day_time.index,day_time.values)


# In[29]:


df_30['Hour'].unique()


# In[31]:


d1=df_30[(df_30['Hour']>29) | (df_30['Hour']<=5)]
d1


# In[32]:


night_time=d1.groupby('Hour')['count_truck'].sum()
sns.barplot(night_time.index,night_time.values)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




