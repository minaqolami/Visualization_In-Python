#!/usr/bin/env python
# coding: utf-8

# jalase 13

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x = np.linspace(0,2,100)


# In[3]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2)
plt.show()


# In[4]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2)
plt.plot(x, x)
plt.plot(x, x ** 3)
plt.show()


# In[5]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2, label = "quadratic")
plt.plot(x, x, label = "linear")
plt.plot(x, x ** 3, label = "cubic")

plt.legend()
plt.show()


# In[6]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2, label = "quadratic")
plt.plot(x, x, label = "linear")
plt.plot(x, x ** 3, label = "cubic")

plt.legend(loc = "lower right")
plt.show()


# In[7]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2, label = "quadratic", color = "red")
plt.plot(x, x, label = "linear")
plt.plot(x, x ** 3, label = "cubic", color = "pink")

plt.legend(loc = "lower right")
plt.show()


# In[9]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2, label = "quadratic", color = "red")
plt.plot(x, x, label = "linear")
plt.plot(x, x ** 3, label = "cubic", color = "pink")
plt.title("simple plot")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.legend(loc = "lower right")
plt.show()


# In[10]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2, label = "quadratic", color = "red",linestyle="--")
plt.plot(x, x, label = "linear",linestyle="-.")
plt.plot(x, x ** 3, label = "cubic", color = "pink")
plt.title("simple plot")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.legend(loc = "lower right")
plt.show()


# In[11]:


fig = plt.figure(figsize = (6,6))
plt.plot(x, x ** 2, label = "quadratic", color = "red",linestyle="--")
plt.plot(x, x, label = "linear",linestyle="-.")
plt.plot(x, x ** 3, label = "cubic", color = "pink",linewidth=5)
plt.title("simple plot")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.legend(loc = "lower right")
plt.show()


# Sup plot

# In[13]:


x1=np.linspace(0,5)
x2=np.linspace(0,2)

y1=np.sin(2*np.pi*x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
plt.plot(x1,y1,color="yellow")

plt.subplot(2,1,2)
plt.plot(x2,y2,color="silver")
plt.show()


# Annotate chart

# In[25]:


years=[1960,1970,1980,1990,2000]
Iranpop=[21.91,28.51,38.94,56.54,66.16]
Turkpop=[27.74,38.44,43.98,53.92,63.24]


# In[28]:


plt.plot(years,Iranpop )
plt.plot(years,Turkpop,linestyle="--", color="red" )
plt.title("iran vs turkey")
plt.xlabel("year")
plt.ylabel("population")
plt.show()


# In[ ]:





# bar chart

# In[36]:


days=[j for j in range(1,11)]
rain_values=[5,266,299,290,125,85,144,130,113,204]


# In[37]:


plt.bar(days,rain_values)

plt.title("Rain value")
plt.xlabel("days")
plt.ylabel("rains")
plt.show()


# In[1]:





# In[38]:


x=np.random.normal(0,1,1024)
y=np.random.normal(0,1,1024)


# In[45]:


plt.scatter(x,y, color="yellow",s=5)
plt.title("scotter plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# In[2]:


import pandas as pd


# In[5]:


data=pd.read_csv(f"‪F:\DSB\Ex\SmartPhones (1).csv")


# In[16]:


data


# Seobrn library

# In[17]:


import seaborn as sns


# In[ ]:


sns.boxplot(x="Company",y="Ram",data=data)


# In[ ]:


sns.boxplot(x="Company",y="Ram",data=data,hue="OS")


# In[ ]:


sns.stripplot(x="OS",y="Capacity",data=data,size=10)


# In[57]:


sns.pairplot(data,hue="OS")


# In[59]:


tips=sns.load_dataset("tips")
tips


# In[63]:


sns.catplot(x="total_bill",y="day",kind="bar",hue="time",data=tips)


# In[65]:


sns.relplot(x="total_bill",y="tip",data=tips)


# In[66]:


sns.relplot(x="total_bill",y="tip",data=tips,col="day", hue="sex")


# In[67]:


sns.lmplot(x="total_bill",y="tip",data=tips,col="day", hue="sex")


# In[69]:


sns.jointplot(x="total_bill",y="tip",data=tips, kind="reg")


# In[71]:


planets=sns.load_dataset("planets")


# In[72]:


planets


# In[74]:


sns.countplot(x="year", data=planets)


# In[75]:


sns.heatmap(tips.corr(),vmin=-1,vmax=1,annot=True)


# In[77]:


flights=sns.load_dataset("flights")


# In[78]:


flights


# In[79]:


sns.heatmap(flights.corr(),vmin=-1,vmax=1,annot=True)


# In[86]:


sns.countplot(x="passengers", data=flights)


# In[ ]:





# In[ ]:





# In[85]:


sns.relplot(x="passengers",y="year",data=flights,hue="month")


# In[88]:


get_ipython().system('pip install plotly')


# In[89]:


import plotly.express as px


# In[90]:


df=px.data.iris()


# In[91]:


df


# In[93]:


px.scatter(df,x="sepal_width",y="sepal_length",color="species")


# In[ ]:




