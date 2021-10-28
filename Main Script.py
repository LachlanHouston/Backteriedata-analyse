# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:04:58 2021

@author: Lachlan Houston(s214593) og Frederik Ravnborg(s204078)
"""
import math
import numpy as np
import panda as pd

# 1: Data load Funktion:
def dataLoad(filename):

    data = pd.read_csv("test.txt", header=None, delimiter=' ', usecols=[0,1,2])
    datanp = np.array(data)
    shape = np.shape(datanp)
    nr_rows = shape[0]
    
    for i in range(nr_rows):
        if data.loc[i,0] < 10 or data.loc[i,0] > 60:
            data = data.drop(i,axis=0)
            
        elif data.loc[i,1] <0:
            data = data.drop(i,axis=0)
        
        elif data.loc[i,2] not in [1,2,3,4]:
            data = data.drop(i,axis=0)
    return data

# 2: Data statistik funktion:
def dataStatistics(data, statistic):
    
    
    result = 0
    return result

# 3: Data plot funktion:
def dataPlot(data):
    
    
    return
    
# 4: Hoved-script:
