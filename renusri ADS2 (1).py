#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install wbgapi


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import wbgapi as wb
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[30]:


def world(a,b,c): #defining the function for creating a datafram
 data = wb.data.DataFrame(a, b, mrv = c)
 data_t = data.T
 worlddata = wb.data.DataFrame(a, mrv = c)
 return data_t, worlddata


# In[4]:


country_codes = ["CAN","GBR","CHN"] #country codes


# In[5]:


PG = {"SP.POP.GROW" : "POPULATION GROWTH(%)"}
CO2 = {"EN.ATM.CO2E.KT" : "CO2 EMISSION(KT)"}
NO = {"EN.ATM.NOXE.ZG" : "NITROUS OXIDE(%)"}
FOR = {"AG.LND.FRST.ZS" : "FOREST AREA(%)"}
UP = {"SP.URB.GROW" : "URBAN SP.URB.GROWPOPULATION"}


# In[6]:


indicator_ids = {"SP.POP.GROW","EN.ATM.CO2E.KT","EN.ATM.NOXE.ZG","AG.LND.FRST.ZS","SP.URB.GROW"}


# In[7]:


wb.series.info(indicator_ids)


# In[8]:


FOR_R, FOR_world = world(FOR.keys(),country_codes,30)


# In[9]:


CO2_R, CO2_world = world(CO2.keys(),country_codes,30)


# In[10]:


UP_R, UP_world = world(UP.keys(),country_codes,30)


# In[11]:


PG_R, PG_world = world(PG.keys(),country_codes,30)


# In[12]:


NO_R, NO_world = world(NO.keys(),country_codes,30)


# In[13]:


N =  NO_world.mean()
NO1 = pd.DataFrame(N)
NO1.reset_index(level=0, inplace=True)
NOA = NO1.rename(columns = {"index": "year", 0: "mean"})
NOA


# In[14]:


C = CO2_world.mean()
C1 = pd.DataFrame(C)
C1.reset_index(level=0, inplace=True)
CO2A = C1.rename(columns ={"index": "year", 0: "mean"})
CO2A


# In[15]:


UP = UP_world.mean()
UP1 = pd.DataFrame(UP)
UP1.reset_index(level=0, inplace=True)
UPA = UP1.rename(columns ={"index": "year", 0: "mean"})
UPA


# In[16]:


PG = PG_world.mean()
PG1 = pd.DataFrame(PG)
PG1.reset_index(level=0, inplace=True)
PGA = PG1.rename(columns ={"index": "year", 0: "mean"})
PGA


# In[17]:


FOR = FOR_world.mean()
FOR1 = pd.DataFrame(FOR)
FOR1.reset_index(level=0, inplace=True)
FORA = FOR1.rename(columns ={"index": "year", 0: "mean"})
FORA


# In[18]:


PG_R


# In[19]:


UP_R


# In[20]:


p=PG_R.rename(columns ={"index": "year", 0: "mean"})
pg_r = p.rename_axis("year")


# In[21]:


u=UP_R.rename(columns ={"index": "year", 0: "mean"})
up_r = u.rename_axis("year")


# In[22]:


n=NO_R.rename(columns ={"index": "year", 0: "mean"})
no_r = n.rename_axis("year")


# In[23]:


c=CO2_R.rename(columns ={"index": "year", 0: "mean"})
co2_r = c.rename_axis("year")


# In[24]:


f=FOR_R.rename(columns ={"index": "year", 0: "mean"})
for_r = f.rename_axis("year")


# In[25]:


# Making plot between CO2 and NO2
fig,ax=plt.subplots(figsize=[8,4])
color1="red"
color2="blue"
ax.plot(NOA["year"],NOA["mean"],marker="*",color=color1)
ax.set_ylabel("NITROUS GAS EMMISION(Kt)",color=color1,fontsize=12)
ax.set_xlabel("Year",color=color1,fontsize=12)
ax.tick_params(axis="y",labelcolor=color1)
plt.xticks(rotation=90)
ax1=ax.twinx()
ax1.plot(CO2A["year"],CO2A["mean"],color=color2,marker="o")
ax1.set_ylabel("CO2 GAS EMMISION(Kt)",color=color2,fontsize=12)
ax1.tick_params(axis="y",labelcolor=color1)
plt.margins(x=0)
plt.title("Time series plot of CO2 and Nitrous Oxide Emission")


# In[26]:


# Making plot between Population growth and Urban population
fig,ax=plt.subplots(figsize=[10,4])
color1="green"
color2="purple"
color3="red"
ax.plot(PGA["year"],PGA["mean"],marker="*",color=color1)
ax.set_ylabel("POPULATION GROWTH(annual %)",color=color1,fontsize=8)
ax.set_xlabel("Year",color=color1,fontsize=16)
ax.tick_params(axis="y",labelcolor=color1)
plt.xticks(rotation=90)
ax1=ax.twinx()
ax1.plot(UPA["year"],UPA["mean"],color=color2,marker=".")
ax1.set_ylabel("URBAN POPULATION(annual %)",color=color2,fontsize=8)
ax1.tick_params(axis="y",labelcolor=color1)
plt.margins(x=0)
plt.title("Time series plot pf Population growth (annual %) and Urban population (annual %)")


# In[27]:


fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
ax1.violinplot(CO2_R["GBR"], showmedians=True, points=10)
ax1.set_xticks([1])
ax1.set_ylabel("CO2 EMISSION")
ax1.set_xticklabels(["UK"])
ax2.violinplot(CO2_R["CHN"], showmedians=True, points=100)
ax2.set_xticks([1])
ax2.set_xticklabels(["CHINA"])
ax3.violinplot(CO2_R["CAN"], showmedians=True, points=500)
ax3.set_xticks([1])
ax3.set_xticklabels(["CANADA"])
plt.show()


# In[28]:


def box(x,y):
 fig = plt.figure(figsize = (4,3))
 ax = fig.add_axes([0,0,1,1])
 cc = ax.boxplot(x)
 ax.set_xlabel("countries")
 ax.set_ylabel("N02 emissions(% change)" )
 ax.set_title("N02 EMMISIONS COMPARISIONS")
 ax.set_xticks([1,2,3,4])
 ax.set_xticklabels(y)
 plt.show()
 return
rr = [NO_R["GBR"],NO_R["CHN"],NO_R["CAN"],NOA["mean"]]
ss = ["UNITED KINGDOM","CHINA","CANADA","WORLD"]
box(rr,ss)


# In[29]:


#heatmap for forest area
sr = np.random.RandomState(0)
FORA = pd.DataFrame(sr.rand(8, 8))
corr = FORA.corr()
plt.figure(figsize=(11,8))
sns.heatmap(corr,annot=True)
plt.show()


# In[ ]:




