#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv('london_merged.csv')


# In[3]:


df.head(5)


# In[4]:


#Exploring the data


# In[6]:


df.shape


# In[7]:


df.info


# In[8]:


df


# In[ ]:


#Counting the unique values in weather_code


# df.weather_code.value_counts()

# In[10]:


df.season.value_counts()


# In[11]:


df = df.rename(columns = {'timestamp' : 'time',
                          'cnt': 'count',
                          't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
})


# In[12]:


df.head()


# In[15]:


# changing the humidity values to percentage (i.e. a value between 0 and 1)
df.humidity_percent = df.humidity_percent / 100


# In[16]:


df.head()


# In[18]:


# creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}


# In[19]:


df.head()


# In[20]:


# changing the seasons column data type to string
df.season = df.season.astype('str')
# mapping the values 0-3 to the actual written seasons
df.season = df.season.map(season_dict)

# changing the weather column data type to string
df.weather = df.weather.astype('str')
# mapping the values to the actual written weathers
df.weather = df.weather.map(weather_dict)


# In[21]:


df.head()


# In[24]:


# writing the final dataframe to an excel file that we will use in our Tableau visualisations. The file will be the 'london_bikes_final.xlsx' file and the sheet name is 'Data'
df.to_excel('london_bikes_final.xlsx', sheet_name='Data')


# In[25]:


FileLink("london_bikes_final.xlsx")


# In[27]:


from IPython.display import FileLink

# Write your pandas dataframe to a csv
df.to_excel

FileLink("london_bikes_final.xlsx")


# In[ ]:




