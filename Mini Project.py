#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


f0=pd.read_csv("Downloads/Mini project 2/F0.csv")
f0


# In[11]:


f1=pd.read_csv("Downloads/Mini project 2/F1.csv")
f2=pd.read_csv("Downloads/Mini project 2/F2.csv")
f3=pd.read_csv("Downloads/Mini project 2/F3.csv")
f4=pd.read_csv("Downloads/Mini project 2/F4.csv")
f5=pd.read_csv("Downloads/Mini project 2/F5.csv")
f6=pd.read_csv("Downloads/Mini project 2/F6.csv")
f7=pd.read_csv("Downloads/Mini project 2/F7.csv")
f8=pd.read_csv("Downloads/Mini project 2/F8.csv")
print("F1\n",f1)
print("F2\n",f2)
print("F3\n",f3)
print("F4\n",f4)
print("F5\n",f5)
print("F6\n",f6)
print("F7\n",f7)
print("F8\n",f8)


# In[31]:


mca=pd.read_csv("Downloads/Mini project 2/Monte Carlo_200.csv")
mca.head(12)


# In[42]:


mca.columns


# In[35]:


df=pd.read_csv("Downloads/Mini project 2/Monte Carlo_200.csv", usecols=["Frequency"])
df

