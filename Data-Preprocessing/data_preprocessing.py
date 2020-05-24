# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:52:31 2020

@author: Hacker
"""
# importing library 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.preprocessing import Imputer
# importing the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values


# Tacking care of missing data

imputer = Imputer(missing_values = 'NaN', strategy = 'mean',axis = 0)
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])