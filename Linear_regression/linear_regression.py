# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:32:13 2020

@author: Hacker
"""
import pandas as pd

data = pd.read_csv('D:/PROJECT/Machnie-Learning/Linear_regression/employee.csv')

mean_data = data.mean()

mean_data_x = mean_data[0]

mean_data_y = mean_data[1]

mean_data_x_sqr = mean_data_x **2
 
constant = (mean_data_x_sqr * mean_data_y)/mean_data_x_sqr

x = data['exp'][0]
y = data['salary'][0]

# y = m x + c
# y = (x-x')^2*(y-y')/(x-x')^2

m = (y - constant)/x 

perdicated_y = m * 4.6 + constant