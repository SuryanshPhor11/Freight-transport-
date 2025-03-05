#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
from datetime import datetime


# In[50]:


and1=pd.read_csv(r"D:\python project\archive (2)\And_05min_0101_0103_2019.csv")
and2=pd.read_csv(r"D:\python project\archive (2)\And_05min_0506_1610_2021.csv")
and3=pd.read_csv(r"D:\python project\archive (2)\And_05min_1303_0606_2021.csv")
and4=pd.read_csv(r"D:\python project\archive (2)\And_15min_0101_0103_2019.csv")
and5=pd.read_csv(r"D:\python project\archive (2)\And_15min_0506_1610_2021.csv")
and6=pd.read_csv(r"D:\python project\archive (2)\And_15min_1303_0606_2021.csv")
and7=pd.read_csv(r"D:\python project\archive (2)\And_30min_0101_0103_2019.csv")
and8=pd.read_csv(r"D:\python project\archive (2)\And_30min_0506_1610_2021.csv")
and9=pd.read_csv(r"D:\python project\archive (2)\And_30min_1303_0606_2021.csv")


# In[51]:


and1.columns=['DateTime','street_identifier','count_truck','traffic_speed']


# In[52]:


and1


# In[7]:


and1.isnull().sum()


# In[8]:


and1.info()


# In[7]:


and1.describe


# In[53]:


and1["DateTime"].fillna(and1['DateTime'].ffill(),inplace=True)


# In[55]:


and1.set_index('DateTime',inplace=True)


# In[56]:


and1


# In[57]:


and1=and1.tz_localize(tz='Europe/Brussels')


# In[58]:


and1.reset_index(inplace=True)


# In[59]:


and1['street_identifier']=and1['street_identifier'].round(2)
and1['traffic_speed']=and1['traffic_speed'].round(1)


# In[54]:


and1['DateTime']=pd.to_datetime(and1['DateTime'])


# In[60]:


and1['Month'] =and1["DateTime"].dt.month_name()
and1['Day'] =and1["DateTime"].dt.day_name()

and1['Hour'] = and1["DateTime"].dt.hour
and1['Minute'] =and1["DateTime"].dt.minute
and1['weekdays'] =and1["DateTime"].dt.week
and1['street']='Anderlecht'


# In[61]:


and1


# In[62]:


and2.columns=['DateTime','street_identifier','count_truck','traffic_speed']
and3.columns=['DateTime','street_identifier','count_truck','traffic_speed']
and4.columns=['DateTime','street_identifier','count_truck','traffic_speed']
and5.columns=['DateTime','street_identifier','count_truck','traffic_speed']
and6.columns=['DateTime','street_identifier','count_truck','traffic_speed']
and7.columns=['DateTime','street_identifier','count_truck','traffic_speed']
and8.columns=['DateTime','street_identifier','count_truck','traffic_speed']


# In[63]:


and2


# In[64]:


and2.info()


# In[38]:


and2.describe


# In[65]:


and2.isnull().sum()


# In[67]:


and2.set_index('DateTime',inplace=True)
and2=and2.tz_localize(tz='US/Eastern')
and2=and2.tz_convert(tz='Europe/Brussels')


# In[70]:


and2


# In[69]:


and2['street_identifier']=and2['street_identifier'].round(2)
and2['traffic_speed']=and2['traffic_speed'].round(1)


# In[66]:


and2['DateTime']=pd.to_datetime(and2['DateTime'])


# In[71]:


and2.reset_index(inplace=True)


# In[72]:


and2


# In[73]:


and2['Month'] =and2["DateTime"].dt.month_name()
and2['Day'] =and2["DateTime"].dt.day_name()

and2['Hour'] = and2["DateTime"].dt.hour
and2['Minute'] =and2["DateTime"].dt.minute
and2['weekdays'] = and2["DateTime"].dt.week
and2['street']='Anderlecht'


# In[74]:


and2


# In[75]:


and3


# In[76]:


and3.info()


# In[77]:


and3.describe


# In[78]:


and3.isnull().sum()


# In[80]:


and3.set_index('DateTime',inplace=True)
and3=and3.tz_localize(tz='Europe/Brussels')


# In[81]:


and3


# In[83]:


and3['street_identifier']=and3['street_identifier'].round(2)
and3['traffic_speed']=and3['traffic_speed'].round(1)


# In[79]:


and3['DateTime']=pd.to_datetime(and3['DateTime'])


# In[82]:


and3.reset_index(inplace=True)


# In[84]:


and3['Month'] =and3["DateTime"].dt.month_name()
and3['Day'] =and3["DateTime"].dt.day_name()

and3['Hour'] = and3["DateTime"].dt.hour
and3['Minute'] =and3["DateTime"].dt.minute
and3['weekdays'] = and3["DateTime"].dt.week
and3['street']='Anderlecht'


# In[85]:


and3


# In[87]:


and12=pd.concat([and2,and3])


# In[89]:


and12.to_csv('and_05_2021.csv')


# In[39]:


and4


# In[68]:


and4.info()


# In[69]:


and4.describe


# In[70]:


and4.isnull().sum()


# In[41]:


and4.set_index('DateTime',inplace=True)
and4=and4.tz_localize(tz='US/Eastern')
and4=and4.tz_convert(tz='Europe/Brussels')


# In[43]:


and4['street_identifier']=and4['street_identifier'].round(2)
and4['traffic_speed']=and4['traffic_speed'].round(1)


# In[40]:


and4['DateTime']=pd.to_datetime(and4['DateTime'])


# In[42]:


and4.reset_index(inplace=True)


# In[44]:


and4['Month'] =and4["DateTime"].dt.month_name()
and4['Day'] =and4["DateTime"].dt.day_name()

and4['Hour'] = and4["DateTime"].dt.hour
and4['Minute'] =and4["DateTime"].dt.minute
and4['weekdays'] = and4["DateTime"].dt.week


# In[45]:


and4


# In[79]:


and4.drop('DateTime',axis=1,inplace=True)


# In[46]:


and4.to_csv('and_15_2019.csv')


# In[82]:


and5


# In[83]:


and5.info()


# In[84]:


and5.describe


# In[85]:


and5.isnull().sum()


# In[86]:


and5["DateTime"].fillna(and5['DateTime'].ffill(),inplace=True)


# In[88]:


and5.set_index('DateTime',inplace=True)
and5=and5.tz_localize(tz='US/Eastern')
and5=and5.tz_convert(tz='Europe/Brussels')


# In[89]:


and5['street_identifier']=and5['street_identifier'].round(2)
and5['traffic_speed']=and5['traffic_speed'].round(1)


# In[87]:


and5['DateTime']=pd.to_datetime(and5['DateTime'])


# In[91]:


and5.reset_index(inplace=True)


# In[92]:


and5['Year'] =and5["DateTime"].dt.year
and5['Month'] =and5["DateTime"].dt.month_name()
and5['Day'] =and5["DateTime"].dt.day_name()

and5['Hour'] = and5["DateTime"].dt.hour
and5['Minute'] =and5["DateTime"].dt.minute
and5['Second'] = and5["DateTime"].dt.second


# In[93]:


and5.drop('DateTime',axis=1,inplace=True)


# In[106]:


and6.info()


# In[107]:


and6.isnull().sum()


# In[108]:


and6["DateTime"].fillna(and6['DateTime'].ffill(),inplace=True)


# In[112]:


and6['street_identifier']=and6['street_identifier'].round(2)
and6['traffic_speed']=and6['traffic_speed'].round(1)


# In[109]:


and6['DateTime']=pd.to_datetime(and6['DateTime'])


# In[113]:


and6.reset_index(inplace=True)


# In[114]:


and6['Year'] =and6["DateTime"].dt.year
and6['Month'] =and6["DateTime"].dt.month_name()
and6['Day'] =and6["DateTime"].dt.day_name()

and6['Hour'] = and6["DateTime"].dt.hour
and6['Minute'] =and6["DateTime"].dt.minute
and6['Second'] = and6["DateTime"].dt.second


# In[115]:


and6.drop('DateTime',axis=1,inplace=True)


# In[116]:


and11=pd.concat([and5,and6])


# In[117]:


and11.to_csv('and_15_2021.csv')


# In[118]:


and7.info()


# In[120]:


and7.describe


# In[121]:


and7.isnull().sum()


# In[123]:


and7["DateTime"].fillna(and7['DateTime'].ffill(),inplace=True)


# In[125]:


and7.set_index('DateTime',inplace=True)
and7=and7.tz_localize(tz='US/Eastern')
and7=and7.tz_convert(tz='Europe/Brussels')


# In[134]:


and7


# In[126]:


and7['street_identifier']=and7['street_identifier'].round(2)
and7['traffic_speed']=and7['traffic_speed'].round(1)


# In[129]:


and7.reset_index(inplace=True)


# In[130]:


and7['DateTime']=pd.to_datetime(and7['DateTime'])


# In[131]:


and7['Year'] =and7["DateTime"].dt.year
and7['Month'] =and7["DateTime"].dt.month_name()
and7['Day'] =and7["DateTime"].dt.day_name()

and7['Hour'] = and7["DateTime"].dt.hour
and7['Minute'] =and7["DateTime"].dt.minute
and7['Second'] = and7["DateTime"].dt.second


# In[132]:


and7.drop('DateTime',axis=1,inplace=True)


# In[133]:


and7.to_csv('and_30_2019.csv')


# In[95]:


and8.info()


# In[135]:


and8.isnull().sum()


# In[136]:


and8["DateTime"].fillna(and8['DateTime'].ffill(),inplace=True)


# In[138]:


and8.set_index('DateTime',inplace=True)
and8=and8.tz_localize(tz='US/Eastern')
and8=and8.tz_convert(tz='Europe/Brussels')


# In[139]:


and8['street_identifier']=and8['street_identifier'].round(2)
and8['traffic_speed']=and8['traffic_speed'].round(1)


# In[137]:


and8['DateTime']=pd.to_datetime(and8['DateTime'])


# In[140]:


and8.reset_index(inplace=True)


# In[141]:


and8['Year'] =and8["DateTime"].dt.year
and8['Month'] =and8["DateTime"].dt.month_name()
and8['Day'] =and8["DateTime"].dt.day_name()

and8['Hour'] = and8["DateTime"].dt.hour
and8['Minute'] =and8["DateTime"].dt.minute
and8['Second'] = and8["DateTime"].dt.second


# In[142]:


and8.drop('DateTime',axis=1,inplace=True)


# In[144]:


and9


# In[145]:


and9.columns=['DateTime','street_identifier','count_truck','traffic_speed']


# In[146]:


and9.info()


# In[147]:


and9.describe


# In[148]:


and9.isnull().sum()


# In[149]:


and9["DateTime"].fillna(and9['DateTime'].ffill(),inplace=True)


# In[109]:


and9['street_identifier']=and9['street_identifier'].round(2)
and9['traffic_speed']=and9['traffic_speed'].round(1)


# In[153]:


and9.reset_index(inplace=True)


# In[154]:


and9['DateTime']=pd.to_datetime(and9['DateTime'])


# In[155]:


and9['Year'] =and9["DateTime"].dt.year
and9['Month'] =and9["DateTime"].dt.month_name()
and9['Day'] =and9["DateTime"].dt.day_name()

and9['Hour'] = and9["DateTime"].dt.hour
and9['Minute'] =and9["DateTime"].dt.minute
and9['Second'] = and9["DateTime"].dt.second


# In[156]:


and12=pd.concat([and8,and9])


# In[158]:


and12.drop('DateTime',axis=1,inplace=True)


# In[159]:


and12.to_csv('and_30_2021.csv')

