# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:04:58 2020

@author: Student
"""
# -> this lib to access the file 
import pandas as pd

#
import sklearn as skl

# -> this lib is use to print the graph 
import matplotlib.pyplot as plt

name = ['sepal-length','speak-width','petal-length','petal-width','class']
dataset  =  pd.read_csv('E:/Machnie-Learning-master/Working with DataSet/dataset/iris.data',names=name)


# shape will give the total number of rows and columns in that dataset
data_shape = dataset.shape


# head will give the number of columns to display 
# syntax is DATASET_VARIABLE.head(NUMBER_OF_COLUMNS_TO_DISPLAY)
data_head = dataset.head(10)


# describe will give the complete decribation of that dataset
data_describe = dataset.describe()

# -> OUTPUT 
"""
       sepal-length  speak-width  petal-length  petal-width
       
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

"""


#classfy the column in size
data_groupby = dataset.groupby('class').size()

# plot is to show the column in graph form 
dataset.plot(kind='box' , subplots = True , layout = (2,2),sharex = False,sharey = False)
plt.show()

# this will show perticular column 
dataset.boxplot('sepal-length')
plt.show()

# -> hist() will give the bar graph for dataset 
dataset.hist()
plt.show()

# -> this will give the bar graph for perti
dataset.hist('petal-length')
plt.show()

plt.scatter(dataset)
plt.show()