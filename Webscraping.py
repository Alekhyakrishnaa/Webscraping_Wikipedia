#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests


# In[7]:


url='https://en.wikipedia.org/wiki/List_of_manufacturers_by_motor_vehicle_production'
page=requests.get(url)


# In[9]:


soup=BeautifulSoup(page.text,'html')
print(soup)


# In[11]:


soup.find_all('table')


# In[53]:


soup.find_all('table')[2]


# In[55]:


soup.find('table',class_='wikitable sortable')


# In[57]:


table=soup.find_all('table')[2]


# In[59]:


print(table)


# In[71]:


world_titles = table.find_all('th')


# In[73]:


world_titles


# In[79]:


world_table_titles=[ title.text.strip() for title in world_titles]
print(world_table_titles)


# In[81]:


import pandas as pd


# In[85]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[89]:


column_data = table.find_all('tr')


# In[102]:


for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)


# In[104]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data


# In[106]:


df


# In[110]:


df.to_csv(r'C:\Users\Akaliya\Downloads\output\carcompanies.csv',index = False)


# In[ ]:




