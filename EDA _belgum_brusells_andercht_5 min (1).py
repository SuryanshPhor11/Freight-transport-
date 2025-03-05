#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime 


# In[2]:


df_5=pd.read_csv(r"F:\New folder (3)\New folder\bxlbeland_05min_2019 (1).csv")


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[4]:


# pip install plotly


# # MONTHWISE TRAFFIC

# In[4]:


month_traffic=df_5.groupby('Month')['count_truck'].sum()
fig = px.bar(x=month_traffic.index, y=month_traffic.values,labels=dict(x="Month_name", y="sum_traffic"))
fig.show()


# # AREA GRAPH

# In[5]:


fig = px.area(x=month_traffic.index, y=month_traffic.values,labels=dict(x="Month_name", y="sum_traffic"))
fig.show()


# # DAYWISE TRAFFIC

# In[6]:


day_traffic=df_5.groupby('Day')['count_truck'].sum()


# In[7]:


fig = px.bar(x=day_traffic.index, y=day_traffic.values,labels=dict(x="Day_name", y="traffic"))
fig.show()


# # STREETWISE TRAFFIC

# In[9]:


street_traffic=df_5.groupby('street')['count_truck'].sum()


# In[10]:


sns.barplot(x=street_traffic.index, y=street_traffic.values,color='g')
plt.xlabel('street',color='r',size=21)
plt.ylabel('traffic',color='r',size=21)
street_traffic


# # WEEKNUMER OF YEAR TRAFFIC

# In[11]:


plt.figure(figsize=(20,10))
weekdays_traffic=df_5.groupby('weekdays')['count_truck'].sum()
sns.barplot(x=weekdays_traffic.index, y=weekdays_traffic.values,color='orange')
plt.xlabel('week_no',size=21,color='b')
plt.ylabel('traffic',size=21,color='r')


# In[12]:


# d['date'] = pd.to_datetime(d['DateTime']).dt.date
# d['time'] = pd.to_datetime(d['DateTime']).dt.time


# In[13]:


df_5['Date']=pd.to_datetime(df_5['DateTime'],utc=True).dt.date


# In[14]:


df_5['year']=pd.to_datetime(df_5['DateTime'],utc=True).dt.year


# # DAY_TIME TRAFFIC

# In[15]:


d=df_5[(df_5['Hour']>=6) & (df_5['Hour']<=18)]


# In[16]:


plt.figure(figsize=(20,10))
day_time=d.groupby('Hour')['count_truck'].sum()
plt.bar(day_time.index,day_time.values,color='y')

for i in range(len(day_time.index)): # 0 to 9
    plt.text(day_time.index[i],day_time.values[i],day_time.values[i],ha='center',color='r')

plt.show()


# # NIGHT_TIME(6PM to 5AM) TRAFFIC

# In[17]:


d1=df_5[(df_5['Hour']>18) | (df_5['Hour']<=5)]
d1


# In[18]:


night_time=d1.groupby('Hour')['count_truck'].sum()
sns.barplot(night_time.index,night_time.values)
plt.xlabel('Hour',color='b',fontsize=15)
plt.ylabel('Sum of traffic',color='b',fontsize=15)
plt.title('Night traffic traffic',color='r',fontsize=15)

# for i in range(len(night_time.index)): # 0 to 9
#     plt.text(night_time.index[i],night_time.values[i],night_time.values[i],ha='center',color='r')

# plt.show()
night_time


# In[19]:


sns.pairplot(df_5)


# In[20]:


df_5.Date.nunique()


# # DATE WISE TRAFFIC

# In[13]:


date_traffic=df_5.groupby('Date')['count_truck'].sum()
fig = px.bar(x=date_traffic.index, y=date_traffic.values,labels=dict(x="Dates", y="sum_traffic"))
fig.show()


# In[ ]:





# In[22]:


df_5.groupby('Date').agg({'count_truck':'sum'}).plot.bar(figsize=(20,5), alpha=0.5)
plt.show()


# # weeked traffic datewise

# In[23]:


wd=df_5[(df_5['Day']=='Sunday' )| (df_5['Day']=='Saturday' )]


# In[24]:


wd.groupby('Date').agg({'count_truck':'sum'}).plot.bar(figsize=(20,5), alpha=0.5)
plt.show()


# # weekdays traffic Date wise:

# In[9]:


week_d=df_5[(df_5['Day']=='Monday' )| (df_5['Day']=='Tuesday' )|(df_5['Day']=='Wednesday' )|(df_5['Day']=='Thrusday' )|(df_5['Day']=='Friday' )]


# In[26]:


week_d.groupby('Date').agg({'count_truck':'sum'}).plot.line(figsize=(20,5), alpha=0.5)
plt.show()


# In[10]:


week_days_traffic=week_d.groupby('Date')['count_truck'].sum()
fig = px.area(x=week_days_traffic.index, y=week_days_traffic.values, labels=dict(x="Week day_Dateswise", y="sum_traffic"))
fig.show()
# week_days_traffic


# In[ ]:





# # Speed visualization

# In[11]:


month_traffic_speed=df_5.groupby('Month')['traffic_speed'].mean()
fig = px.bar(x=month_traffic_speed.index, y=month_traffic_speed.values,labels=dict(x="Monthly", y="Average_traffic_speed"))
fig.show()
month_traffic_speed


# # March is having more traffic

# # BUSYEST DAY ACCORDING TO SPEED:

# In[29]:


df_5.head(2)


# In[12]:


busyday=df_5.groupby('Day')['traffic_speed'].mean().round(2)
fig = px.bar(x=busyday.index, y=busyday.values,labels=dict(x="Day_name", y="traffic"))
fig.show()
busyday


# In[ ]:





# # Busyest Stree According to Speed

# In[31]:


busy_street=df_5.groupby('street')['traffic_speed'].mean().round(2)
sns.barplot(x=busy_street.index, y=busy_street.values,color='r')
plt.xlabel('street',color='r',size=21)
plt.ylabel('street_speed',color='r',size=21)
busy_street


# # which week of a year is having high speed

# In[32]:


plt.figure(figsize=(20,10))
busy_week=df_5.groupby('weekdays')['traffic_speed'].mean().round(2)
sns.barplot(x=busy_week.index, y=busy_week.values,color='y')
plt.xlabel('week_no',size=21,color='b')
plt.ylabel('year_week_speed',size=21,color='b')
busy_week


# # DAY_TIME SPEED [6AM to 6PM]

# In[33]:


d=df_5[(df_5['Hour']>=6) & (df_5['Hour']<=18)]
plt.figure(figsize=(20,10))
day_time_speed=d.groupby('Hour')['traffic_speed'].mean().round(2)
plt.bar(day_time_speed.index,day_time_speed.values,color='y')

for i in range(len(day_time.index)): # 0 to 9
    plt.text(day_time_speed.index[i],day_time_speed.values[i],day_time_speed.values[i],ha='center',color='r')

plt.show()


# # NIGHT_TIME(6PM to 5AM) SPEED:

# In[34]:


d1=df_5[(df_5['Hour']>18) | (df_5['Hour']<=5)]
night_time_speed=d1.groupby('Hour')['traffic_speed'].mean().round(2)
sns.barplot(night_time_speed.index,night_time_speed.values)
plt.xlabel('Hour',color='b',fontsize=15)
plt.ylabel('Average speed of truck',color='b',fontsize=15)
plt.title('Night traffic traffic',color='r',fontsize=15)
night_time_speed


# In[35]:


fig,ax=plt.subplots(figsize=(15,5))
sns.lineplot(night_time_speed.index,night_time_speed.values,color='b')

sns.lineplot(day_time_speed.index,day_time_speed.values,color='g')
ax.set_ylabel("traffic_speed")
ax.legend(title='Legend',labels=['Night_time','Day_time'])
plt.show()


# # WEEKEND SPEED:

# In[36]:


wd=df_5[(df_5['Day']=='Sunday' )| (df_5['Day']=='Saturday' )]
wd.groupby('Date').agg({'traffic_speed':'mean'}).plot.bar(figsize=(20,5), alpha=0.5)
plt.show()


# # weekdays Average_Speed Date wise:

# In[14]:


week_days_traffic=week_d.groupby('Date')['traffic_speed'].mean().round(2)
fig = px.bar(x=week_days_traffic.index, y=week_days_traffic.values, labels=dict(x="Week day_Dateswise", y="Average_Speed"))
fig.show()


# In[ ]:





# # STREET_ID wise Visualzation

# In[38]:


df_5.groupby('street_identifier')['count_truck','traffic_speed'].mean().round(2)


# In[39]:


df_5.head(5)


# In[40]:


s=df_5.groupby('street_identifier')['count_truck','traffic_speed'].mean().round(2)


# In[ ]:





# In[41]:


s


# In[43]:


ds=pd.read_csv(r"C:\Users\sinha\Desktop\7_30 batch\Belgium project\bxlbeand_30min_2019.csv")


# In[44]:


ds.isna().sum()

