# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:04:58 2021
@author: Lachlan Houston(s214593) og Frederik Ravnborg(s204078)
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# 1: Data load function:
# =============================================================================
def dataLoad(filename):
    # Importing the data as a matrix using the panda module
    while (True):
        try:
            data = pd.read_csv(filename, header=None, delimiter=' ', usecols=[0,1,2])
            
        except OSError:
            print("An incorrect input was given, please try again"," ",sep='\n')
            
        else:
            print("A file has been found and loaded")
            # Calculating the number of rows in the matrix
            datanp = np.array(data)
            shape = np.shape(datanp)
            nr_rows = shape[0]
        
            # Creating a for loop that goes through each row
            for i in range(nr_rows):
                
                # Removing rows with a temperature smaller than 10 or greater than 60
                if data.loc[i,0] < 10 or data.loc[i,0] > 60:
                    print("Row ",i," contains an errornous temperature (",data.loc[i,0],") and has been removed")
                    data = data.drop(i,axis=0)
                
                # Removing rows with negative growth rate    
                elif data.loc[i,1] <0:
                    print("Row ",i," contains an errornous growth rate (",data.loc[i,1],") and has been removed")
                    data = data.drop(i,axis=0)
                
                # Removing rows with bacteria ID not matching either 1, 2, 3 or 4
                elif data.loc[i,2] not in [1,2,3,4]:
                    print("Row ",i," contains an errornous bacteria ID (",data.loc[i,2],") and has been removed")
                    data = data.drop(i,axis=0)
                    
            data = data.reset_index(drop=True)
            return data
        break
    
    

# =============================================================================
# 2: Data statistic function:
# =============================================================================
# The Data statistic function is defined, where data from file and a string 'statistics' are input:
def dataStatistics(data, statistic):

    # Local variables are defined
    selection = 0
    cold = 0
    hot = 0
    t = 0
    
    # Data is put into a Numpy Array
    statData = np.array(data)
    dim = np.shape(statData)
    
    # List of different commands that can be called
    commands = np.array(["mean temperature", "mean growth rate", "std temperature", "std growth rate", "rows", "mean cold growth rate","mean hot growth rate"])
    
    # A while loop that runs until a correct input has been given.
    while(selection == 0):
        
        # Input is gathered from user and afterwards lowercased
        print("\nPlease select the data that you'd like to calculate. You have the option of selecting the following: \nMean Temperature \nMean Growth rate \nStd Temperature \nStd Growth rate \nRows \nMean Cold Growth rate \nMean Hot Growth rate")
        statistic = input()
        statistic = statistic.lower()
        
        # A for loop that checks whether a input has been given and if it is correct
        for i in range(len(commands)):
            
            # If a correct input has been given, this checks which input and assigns a value to 'selection', that corrosponds to the value location of the string in commands array
            # Also breaks the loop
            if statistic == commands[i]:
                selection = i+1
                print(commands[i], "has been selected")
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
                t += 1
                
        # Finds the mean of the values collected
        try:
            result = cold/t
            
        except ZeroDivisionError:
            print("There are no elements in the list")
            result = 0
    
    # This handles the Mean Hot Growth rate
    if selection == 7:
        
        # Loop that loops through and finds the elements where the temperature is higher than 50
        
        for i in range(len(statData)):
            if statData[i,0] >= 50:
                
                # Stores the Growth rate data in one variable
                hot += statData[i,1]
                
                # Keeps count of how many element that fit the requirements
                t += 1
                
        # Finds the mean of the values collected
        try:
            result = hot/t
            
        except ZeroDivisionError:
            print("There are no elements in the list")
            result = 0

    # The number generated through the equations are returned as the float 'results'
    return result

# =============================================================================
# 3: Data plot function:
# =============================================================================
def dataPlot(data):
    
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
    
    return("Generate data plots from file data has been selected\n\nThe first plot shows how many of each bacteria type there is in the dataset.\nThe second plot shows graphs representing growth rate by temperature for each selected bacteria type.")


# =============================================================================
# Main Script:
# =============================================================================

# Variables are declared
exitScript = False
specifiedData = False

# =============================================================================
# A loop is initiated that doesn't close until the user specifically closes the program
# =============================================================================
while exitScript == False:
    print(" ","You have the following options of funtions to call:"," ", "1) Load data from file","2) Generate statitistics from file data","3) Generate data plots from file data","4) Quit the program", 
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
        safeData = data
        
        
        # Checks if data has been loaded yet
        if specifiedData == True:
            
            # statistics is defined as an empty string
            statistic = " "
            
            # Variables for interval selecting
            length = len(data)
            xLower = 0
            xUpper = 100
            numberofRemovals = 0
            
            strings = np.array(["Temperature","Growth rate","Bacteria type","All"])
            
            while (True):
                print("Do you want to apply an interval to the data you select?", "1) Yes", "2) No",sep='\n')
                intervalSelection = input()
                intervalSelection = intervalSelection.lower()
                
                if intervalSelection == "1" or intervalSelection == "yes":
                    
                    while (True):
                        print("You have the option to create intervals based on the following types of data:","1) Temperature","2) Growth rate","3) Bacteria type","Please choose which data you want to access:", sep='\n')
                        
                        try:
                            choiceofData = input()
                            choiceofDataInt = int(choiceofData) - 1
                            
                        except ValueError:
                            print("An incorrect input was given, please try again"," "," ",sep='\n')
                            
                        else:
                            
                            print("You have chosen ",strings[choiceofDataInt],"as data")
                            break
                            
                    if choiceofData == "1" or choiceofData == "2":
                        print("Please select desired lower limit")
                        xLower = float(input())
                        print(xLower)
                        
                        print("Please selected desired upper limit")
                        xUpper = float(input())
                        print(xUpper)
                        
                        print("Your interval has been set to", xLower, "< data <", xUpper)
                        
                        # Creating a for loop that goes through each row
                        for i in range(length):
                        
                        # Removing rows with a data lower or higher than the given interval
                            if data.loc[i,choiceofDataInt] < xLower or data.loc[i,choiceofDataInt] > xUpper:
                                data = data.drop(i,axis=0)
                                numberofRemovals += 1
                                
                        print("A total of ", numberofRemovals, "rows have been removed from the dataset, and ", length - numberofRemovals, "remain.")
                
                        
                    elif choiceofData == "3":
                        print("Please input the Bacteria ID")
                        bacteriaID = int(input())
                        
                        # Creating a for loop that goes through each row
                        for i in range(length):
                            if data.loc[i,choiceofDataInt] != bacteriaID:
                                    data = data.drop(i,axis=0)
                                    numberofRemovals += 1
                    
                        print("A total of ", numberofRemovals, "rows have been removed from the dataset, and", length - numberofRemovals, "remain.")
                        
                    
                    break
                    
                elif intervalSelection == "2" or intervalSelection == "no":
                    print("No interval has been added")
                    xLower = 0
                    xUpper = 100
                    
                    break
                
                else:
                    print("You have entered an incorrect input, please try again"," ",sep='\n')
            
            # Output from dataStatistics is printed here
            print("The result is:", dataStatistics(data, statistic))
            
            data = safeData
        
        # If data has not been loaded, the loop restarts
        elif specifiedData == False:
            print("The file of data has not yet been input, please load data (Option 1)")
        
    # Choice number 3; calls the dataPlot function
    elif choice == "3" or choice == "plots" or choice == "generate data plots from file data":
        
        # Checks if data has been loaded yet
        if specifiedData == True:
            print(dataPlot(data))
            
        # If data has not been loaded, the loop restarts
        elif specifiedData == False:
            print("The file of data has not yet been input, please load data (Option 1)")
        
        
    # Choice number 4; ends the program
    elif choice == "4" or choice == "quit" or choice == "quit the program":
        
        # Changes exitScript to True and therefore closes the loop and ends the program
        print("Ending program.")
        exitScript = True
        
    else:
        print("You have entered an incorrect input, please try again")
