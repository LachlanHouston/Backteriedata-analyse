# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:04:58 2021

@author: Lachlan Houston(s214593) og Frederik Ravnborg(sxxxxxx)
"""
import math
import numpy as np
import panda as pd

# 1: Data load function:
def dataLoad(filename):
    # Importing the data as a matrix using the panda module
    data = pd.read_csv("test.txt", header=None, delimiter=' ', usecols=[0,1,2])
    
    # Calculating the number of rows in the matrix
    datanp = np.array(data)
    shape = np.shape(datanp)
    nr_rows = shape[0]
    
    # Creating a for loop that goes through each row
    for i in range(nr_rows):
        
        # Removing rows with a temperature smaller than 10 or greater than 60
        if data.loc[i,0] < 10 or data.loc[i,0] > 60:
            data = data.drop(i,axis=0)
        
        # Removing rows with negative growth rate    
        elif data.loc[i,1] <0:
            data = data.drop(i,axis=0)
        
        # Removing rows with bacteria ID not matching either 1, 2, 3 or 4
        elif data.loc[i,2] not in [1,2,3,4]:
            data = data.drop(i,axis=0)
    return data

data = dataLoad("test.txt")
statistic = " "

# 2: Data statistik function:
# The Data statistic function is defined, where data from file and a string 'statistics' are input:
def dataStatistics(data, statistic):
    
    # Data is put into a Numpy Array
    datanp = np.array(data)

    # Local variables are defined
    selection = 0
    cold = 0
    hot = 0
    x = 0
    
    # List of different commands that can be called
    commands = np.array(["mean temperature", "mean growth rate", "std temperature", "std growth rate", "rows", "mean cold growth rate","mean hot growth rate"])
    
    # A while loop that runs until a correct input has been given.
    while(selection == 0):
        
        # Input is gathered from user and afterwards lowercased
        print("Please select the data that you'd like to calculate, you have the option of selecting the following: mean temperature, mean growth rate, std temperature, std growth rate, rows, mean cold growth rate, and mean hot growth rate")
        statistic = input()
        statistic = statistic.lower()
        
        # A for loop that checks whether a input has been given and if it is correct
        for i in range(len(commands)):
            
            # If a correct input has been given, this checks which input and assigns a value to 'selection', that corrosponds to the value location of the string in commands array
            # Also breaks the loop
            if statistic == commands[i]:
                selection = i+1
                print(commands[i], " has been selected")
                break
            
        # If an incorrect input has been given, selection will remain equal to 0, and the while loop starts again
        if selection == 0:
            print("Wrong input, please input a correct name")

    # This set of if-statements handle each equation, and are called based on which value selection has.
    # This handles Mean Temperature & Mean Growth Rate
    if selection == 1 or selection == 2:
        result = np.mean(datanp[:,selection-1])

    
    # This handles Standard Temperature & Standard Growth Rate
    if selection == 3 or selection == 4:
        result = np.std(datanp[:,selection-3])


    # This informs the amount of rows in the data
    if selection == 5:
        dim = np.shape(datanp)
        result = dim[0]
    
    # This hanldes the Mean Cold Growth rate
    if selection == 6:
        
        # Loop that loops through the data and finds the elements where the temperature is lower than 20
        for i in range(len(datanp)):
            if datanp[i,0] <= 20:
                
                # Stores the Growth rate data in one variable
                cold += datanp[i,1]
                
                # Keeps count of how many elements that fit the requirements
                x += 1
                
        # Finds the mean of the values collected
        result = cold/x
    
    # This handles the Mean Hot Growth rate
    if selection == 7:
        
        # Loop that loops through and finds the elements where the temperature is higher than 50
        for i in range(len(datanp)):
            if datanp[i,0] >= 50:
                
                # Stores the Growth rate data in one variable
                hot += datanp[i,1]
                
                # Keeps count of how many element that fit the requirements
                x += 1
                
        # Finds the mean of the values collected
        result = hot/x
        
    # The number generated through the equations are returned as the float 'results'
    return result

print(dataStatistics(data, statistic))

# 3: Data plot function:
def dataPlot(data):
    # Insert your code here
    return
    
# 4: Hoved-script:
