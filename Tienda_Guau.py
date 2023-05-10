#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


pwd


# In[6]:


get_ipython().system('cd D:')


# In[13]:


_2019 = pd.read_csv("d:/TIENDA/Data/2019.csv", sep =";")


# In[14]:


_2020 = pd.read_csv("d:/TIENDA/Data/2020.csv", sep =";")


# In[15]:


_2021 = pd.read_csv("d:/TIENDA/Data/2021.csv", sep =";")


# In[16]:


_2022 = pd.read_csv("d:/TIENDA/Data/2022.csv", sep =";")


# In[17]:


frames = [_2019,_2020,_2021,_2022]


# In[18]:


datos = pd.concat(frames)


# In[22]:


datos.sample(20)


# In[20]:


datos.columns


# In[32]:


len(datos.CodigoFamilia.unique())


# In[34]:


len(datos.CodigoSubfamilia.unique())


# In[35]:


len(datos.CodigoProveedor.unique())


# In[36]:


len(datos.CodigoArticulo.unique())


# In[38]:


len(datos.CodigodelCliente.unique())


# In[41]:


datos.FechaPedido.sample(5)


# In[42]:


datos.FechaPedido = pd.to_datetime(datos.FechaPedido)


# In[43]:


datos.FechaEntrega = pd.to_datetime(datos.FechaEntrega)


# In[70]:


from datetime import datetime, timedelta


# In[71]:


datos['tiempo'] = (datos.FechaEntrega - datos.FechaPedido) / timedelta(days=1)


# In[72]:


datos['tiempo'].dtypes


# In[73]:


datos.head(10)


# In[74]:


datos.tiempo.max()


# In[75]:


datos.tiempo.mean()


# In[76]:


datos.tiempo.min()


# In[77]:


datos.FechaEntrega.max()


# In[79]:


datos.FechaPedido.max()


# In[80]:


datos.FechaEntrega.min()


# In[81]:


datos.FechaPedido.min()


# In[83]:


datos.tiempo.value_counts()


# In[84]:


datos.FechaEntrega.head(5)


# In[85]:


datos.FechaPedido.head(5)


# In[ ]:




