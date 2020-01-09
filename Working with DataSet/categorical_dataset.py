

import pandas as pd
import numpy as np

data = pd.read_csv('E:/python/ML/Working with DataSet/dataset/adler.csv')
data

n = data.isnull()
n

data_mode = data.mode()
data_mode


fill_mode =  data.fillna(data.mode())
fill_mode
