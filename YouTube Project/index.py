# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:50:48 2020

@author: Hacker
"""
import pandas as pa
import numpy as ny

data = pa.read_csv('D:/PROJECT/Machnie-Learning/YouTube Project/CAvideos.csv')

data

NullData = data.isnull()
NullData

videoPublishedTime = data[['publish_time']]

videoPublishedTime.dropna (inplace= True)

videoPublishedTime['publish_time'] = videoPublishedTime['publish_time'].str.split("T", n = 1, expand = True) 
videoPublishedTime