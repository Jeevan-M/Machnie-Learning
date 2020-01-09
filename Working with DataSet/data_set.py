# -*- coding: utf-8 -*-

import pandas as pa 
import numpy as np

"""
-> reading the file using pandas lib 
-> read function is used to read the file
   
     syntaz:-
            { read_fileformat('file path')}  
"""
data  = pa.read_csv('E:/python/ML/dataset/mark.csv')

# printing the csv file 
data

# isnull is used to check the whather the dataset having the null value or not 

n = data.isnull()
n

"""
-> fillna is used to fill the null valued in the dataset

    syntax:-
        variable_name.fillna(Replace data)

"""
fill = data.fillna(0)
fill


# means function is used to find the means for the dataset
data_mean = data.mean()
data_mean
fill_mean =  data.fillna(data_mean)
fill_mean

#-> Single line code for mean
temp_mean = data.fillna(data.mean())


# median function is used to find the median for the dataset
data_median = data.median()
data_median
fill_median = data.fillna(data_median)
fill_median




