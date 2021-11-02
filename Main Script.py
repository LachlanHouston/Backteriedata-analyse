# -*- coding: utf-8 -*-
"""
Project 1 - Bacteria Data Analysis

Due: 11/11/2021

By: Lachlan Houston (s214593) & Frederik Ravnborg (s204078)
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1: Data Load function

# The Data Load function is defined, where the input is a file
def dataLoad(filename):
    # Importing the data as a matrix using the panda module
    data = pd.read_csv(filename, header=None, delimiter=' ', usecols=[0,1,2])
    
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
        
        # Removing rows with bacteria type not matching either 1, 2, 3 or 4
        elif data.loc[i,2] not in [1,2,3,4]:
            data = data.drop(i,axis=0)
    return data

data = dataLoad("test.txt")
statistic = " "


# 2: Data Statistic function

# The Data Statistic function is defined, where data from file and a string 'statistics' are input
def dataStatistics(data, statistic):
    
    # Data is put into a Numpy Array
    statData = np.array(data)

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
        print("Please select the data that you'd like to calculate. You have the option of selecting the following: \nMean Temperature \nMean Growth rate \nStd Temperature \nStd Growth rate \nRows \nMean Cold Growth rate \nMean Hot Growth rate")
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
        result = np.mean(statData[:,selection-1])

    
    # This handles Standard Temperature & Standard Growth Rate
    if selection == 3 or selection == 4:
        result = np.std(statData[:,selection-3])


    # This informs the amount of rows in the data
    if selection == 5:
        dim = np.shape(statData)
        result = dim[0]
    
    # This handles the Mean Cold Growth rate
    if selection == 6:
        
        # Loop that loops through the data and finds the elements where the temperature is lower than 20
        for i in range(len(statData)):
            if statData[i,0] <= 20:
                
                # Stores the Growth rate data in one variable
                cold += statData[i,1]
                
                # Keeps count of how many elements that fit the requirements
                x += 1
                
        # Finds the mean of the values collected
        result = cold/x
    
    # This handles the Mean Hot Growth rate
    if selection == 7:
        
        # Loop that loops through and finds the elements where the temperature is higher than 50
        for i in range(len(statData)):
            if statData[i,0] >= 50:
                
                # Stores the Growth rate data in one variable
                hot += statData[i,1]
                
                # Keeps count of how many element that fit the requirements
                x += 1
                
        # Finds the mean of the values collected
        result = hot/x
        
    # The number generated through the equations are returned as the float 'results'
    return result

print(dataStatistics(data, statistic))


# 3: Data Plot function

# The Data Plot function is defined, where data returned from the Data Load function is the input
def dataPlot(data):
    data = dataLoad("test.txt")
    
    # Creating an array containing all the bacteria types
    bacteria_type = np.array(data[2])
    
    # Computing how many occurences each bacteria has in bacteria_type
    b1 = np.sum(bacteria_type == 1)
    b2 = np.sum(bacteria_type == 2)
    b3 = np.sum(bacteria_type == 3)
    b4 = np.sum(bacteria_type == 4)
    
    # Defining the x and y axis
    x = ['1', '2', '3', '4']
    y = np.array([b1,b2,b3,b4])
    
    # Designing and running the plot
    plt.bar(x[0], y[0], color="g")
    plt.bar(x[1], y[1], color="b")
    plt.bar(x[2], y[2], color="y")
    plt.bar(x[3], y[3], color="r")
    plt.title("Number of each bacteria type")
    plt.xlabel("Bacteria type")
    plt.ylabel("Number of bacteria")
    plt.xlim([-0.5, 3.5])
    plt.ylim([0, np.max(y)+3])
    plt.show()
    
    # Creating a variable containing the number of rows in the dataset
    datanp = np.array(data)
    shape = np.shape(datanp)
    nr_rows = shape[0]
    
    # Creating a zero array for the x- and y-axis for each bacteria type with the correct length
    x1 = np.zeros(b1)
    x2 = np.zeros(b2)
    x3 = np.zeros(b3)
    x4 = np.zeros(b4)
    y1 = np.zeros(b1)
    y2 = np.zeros(b2)
    y3 = np.zeros(b3)
    y4 = np.zeros(b4)
    
    
    x = 0
    y = 0
    w = 0
    z = 0
    
    # This for loop fills the zero arrays with the temperature values on the x-axis and growth rate on the y-axis for each bacteria type seperately
    for i in range(nr_rows):
        
        # Bacteria type 1
        if datanp[i,2] == 1:
            x1[y] = datanp[i,0]
            y1[y] = datanp[i,1]
            y += 1
        
        # Bacteria type 2
        if datanp[i,2] == 2:
            x2[x] = datanp[i,0]
            y2[x] = datanp[i,1]
            x += 1
        
        # Bacteria type 3
        if datanp[i,2] == 3:
            x3[w] = datanp[i,0]
            y3[w] = datanp[i,1]
            w += 1
        
        # Bacteria type 4
        if datanp[i,2] == 4:
            x4[z] = datanp[i,0]
            y4[z] = datanp[i,1]
            z += 1
    
    # Sorting the elements on the x-coordinate lists and arranging the elements in the y-coordinate lists correspondingly, so that the x-y pairs are kept
    sort1 = x1.argsort()
    x1 = x1[sort1]
    y1 = y1[sort1]
    
    sort2 = x2.argsort()
    x2 = x2[sort2]
    y2 = y2[sort2]
    
    sort3 = x3.argsort()
    x3 = x3[sort3]
    y3 = y3[sort3]
    
    sort4 = x4.argsort()
    x4 = x4[sort4]
    y4 = y4[sort4]
    
    # Designing and running the plot
    plt.plot(x1, y1, color="g")
    plt.plot(x2, y2, color="b")
    plt.plot(x3, y3, color="C1")
    plt.plot(x4, y4, color="r")
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.xlim([0, 60])
    plt.legend(["Bacteria 1", "Bacteria 2", "Bacteria 3", "Bacteria 4"], loc ="upper left")
    plt.show()


# 4: Main Script

# Variables are declared
exitScript = False
specifiedData = False

# =============================================================================
# A loop is initiated that doesn't close until the user specifically closes the program
# =============================================================================
while exitScript == False:
    print(" ","You have the following options of funtions to call:", "1) Load data from file","2) Generate statitistics from file data","3) Generate data plots from file data","4) Quit the program", 
          "Please type what you want to do:",sep='\n')
    
    # Choice contains the input that correlates to what the user wants to access
    choice = input()
    choice = choice.lower()
    print(" ")
    
    # Choice number 1; calls the dataLoad function
    if choice == "1" or choice == "load data" or choice == "load data from file":
        
        print("Please input the name of the file you want to load:")
        
        # Name of file the user wants to access, requires entering the filetype
        name = input()
        print(" ")
        
        # Changes specifiedData to record that data has been selected
        specifiedData = True
        
        # Stores the data so dataStatistics can access it later
        data = dataLoad(name)
        
    # Choice number 2; calls the dataStatistics function
    elif choice == "2" or choice == "statistics" or choice == "generate statistics from file data":
        
        # Checks if data has been loaded yet
        if specifiedData == True:
            
            # statistics is defined as an empty string
            statistic = " "
            
            # Output from dataStatistics is printed here
            print("The results are:", dataStatistics(data, statistic))
        
        # If data has not been loaded, the loop restarts
        elif specifiedData == False:
            print("The file of data has not yet been input, please load data (Option 1)")
        
    # Choice number 3; calls the dataPlot function
    elif choice == "3" or choice == "plots" or choice == "generate data plots from file data":
        print(None)
        
    # Choice number 4; ends the program
    elif choice == "4" or choice == "quit" or choice == "quit the program":
        
        # Changes exitScript to True and therefore closes the loop and ends the program
        print("Ending program.")
        exitScript = True
        
    else:
        print("You have entered an incorrect input, please try again")


