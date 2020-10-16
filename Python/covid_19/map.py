#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib
import geopandas as gpd
import PIL
import io


# In[2]:


data=pd.read_csv('time_series_covid19_confirmed_global.csv')


# # group the data by country

# In[3]:


data=data.groupby('Country/Region').sum()


# # drop the 'Lat' and 'Long' column

# In[4]:


data=data.drop(columns=['Lat','Long'])
data.head()


# # create transpose of the data

# In[5]:


data_transposed=data.T
data_transposed.head()


# # printing the map

# In[6]:


world=gpd.read_file('World_Map.shp')


# # checking the name of the countries for boath data and world

# In[7]:


# for index,row in data.iterrows():
#     if index not in world['NAME'].to_list():
#         print(index+' : not in list')
#     else:
#         pass


# In[8]:


world.replace('United States','US',inplace=True)
world.replace('Taiwan','Taiwan*',inplace=True)
world.replace('Syrian Arab Republic','Syria',inplace=True)


# In[9]:


merge=world.join(data,on='NAME',how='right')


# # plot

# In[ ]:


image_frames=[]
for dates in merge.columns.to_list()[2:238]:  #238
    ax=merge.plot(column=dates,
                 cmap='OrRd',
                 figsize=(15,15),
                 legend=True,
                 scheme='user_defined',
                 classification_kwds={'bins':[10,20,50,100,500,1000,5000,500000]},
                 edgecolor='black',
                 linewidth=0.4)
    ax.set_title('Confirmed C-19 Cases'+dates,fontdict={'fontsize':25},pad=10.5)
    ax.set_axis_off()
    ax.get_legend().set_bbox_to_anchor((0.18,0.6))
    img=ax.get_figure()
    f=io.BytesIO()
    img.savefig(f,format='png',bbox_inches='tight')
    f.seek(0)
    image_frames.append(PIL.Image.open(f))
    
#gif animation
image_frames[0].save('c-19 map.gif',format='GIF',
                    append_images=image_frames[1:],
                    save_all=True,duration=300,
                    loop=3
                    )

f.close()

# In[ ]:




