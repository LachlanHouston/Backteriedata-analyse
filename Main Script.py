"""
Project 1 - Bacteria Data Analysis
(02631) Introduction to Programming and Data processing
By: Lachlan Houston (s214593) og Frederik Ravnborg (s204078)
Due: 11/11/2021
"""
# Packages are imported and defined
import numpy as np
np.set_printoptions(suppress = True)
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# 1: Data Load function:
# @Frederik Ravnborg (s204078)
# =============================================================================
# The Data Load function is defined, where a file of the user's choice is input:
def dataLoad(filename):
    # Importing the data as a matrix using the panda module and handling wrong input
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
                    print("Row",i,"contains an errornous temperature (" + str(round(data.loc[i,0])) + ") and has been removed")
                    data = data.drop(i,axis=0)
                
                # Removing rows with negative growth rate    
                elif data.loc[i,1] <0:
                    print("Row",i,"contains an errornous growth rate (" + str(round(data.loc[i,1], 2)) + ") and has been removed")
                    data = data.drop(i,axis=0)
                
                # Removing rows with bacteria ID not matching either 1, 2, 3 or 4
                elif data.loc[i,2] not in [1,2,3,4]:
                    print("Row",i,"contains an errornous bacteria ID (" + str(data.loc[i,2]) + ") and has been removed")
                    data = data.drop(i,axis=0)
            
            # Resetting the indexes in the data                            
            data = data.reset_index(drop=True)
            return data
        break


# =============================================================================
# 2: Data Statistic function:
# @Lachlan Houston (s214593)
# =============================================================================
# The Data Statistic function is defined, where data from file and a string 'statistics' are input:
def dataStatistics(data, statistic):

    # Local variables are defined
    cold = 0
    hot = 0
    t = 0
    
    # Data is put into a Numpy Array
    statData = np.array(data)
    
       
    # Input is gathered from user and afterwards lowercased
    statisticChoice = statistic
    # statisticChoice = statisticChoice.lower()
    
    # Choice number 1 - computes the Mean Temperature
    if statisticChoice == "1" or statisticChoice == "mean temperature":
        try:
            result = np.mean(statData[:,0])
        except IndexError:
            result = 0
        
        result = round(result,3)

    # Choice number 2 - computes the Mean Growth Rate
    elif statisticChoice == "2" or statisticChoice == "mean growth rate":
        try:
            result = np.mean(statData[:,1])
        except IndexError:
            result = 0
        
        result = round(result,3)        
    
    # Choice number 3 - computes the Standard Deviation of the Temperature
    elif statisticChoice == "3" or statisticChoice == "std temperature":
        try:
            result = np.std(statData[:,0])
        except IndexError:
            result = 0
        result = round(result,3)
    
    # Choice number 4 - computes the Standard Deviation of the Growth rate
    elif statisticChoice == "4" or statisticChoice == "std growth rate":
        try:
            result = np.std(statData[:,1])
        except IndexError:
            result = 0
            
        result = round(result,3)

    # Choice number 5 - computes the number of rows
    elif statisticChoice == "5" or statisticChoice == "rows":
        result = np.shape(statData)[0]

    # Choice number 6 - computes the Mean Cold Growth rate
    elif statisticChoice == "6" or statisticChoice == "mean cold growth rate":
        
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
            result = round(result,3)
            
        except ZeroDivisionError:
            result = 0
    
    # Choice number 7 - computes the Mean Hot Growth rate       
    elif statisticChoice == "7" or statisticChoice == "mean hot growth rate":
            
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
            result = round(result,3)
            
        except ZeroDivisionError:
            result = 0
            
    else:
        result = 0

    # The number generated through the equations are returned as the float 'results'
    return result

# =============================================================================
# 3: Data Plot function:
# @Frederik Ravnborg (s204078)
# =============================================================================
def dataPlot(data):
    
    # Creating an array containing all the bacteria types
    bacteria_type = np.array(data[2])
    
    # Computing and storing how many occurences each bacteria has in bacteria_type
    b1 = np.sum(bacteria_type == 1)
    b2 = np.sum(bacteria_type == 2)
    b3 = np.sum(bacteria_type == 3)
    b4 = np.sum(bacteria_type == 4)
    
    # Defining the x-axis as bacteria type and the y-axis as the number of the corresponding bacteria
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
    
    # Creating a zero array for the x- and y-axes for each bacteria type with the correct length
    x1 = np.zeros(b1)
    x2 = np.zeros(b2)
    x3 = np.zeros(b3)
    x4 = np.zeros(b4)
    y1 = np.zeros(b1)
    y2 = np.zeros(b2)
    y3 = np.zeros(b3)
    y4 = np.zeros(b4)
    
    # Variables are defined
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
    
    # Sorting the elements on the x-coordinate lists and arranging the elements in the y-coordinate lists correspondingly, so the x-y pairs are kept
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
    


# =============================================================================
# Main Script:
# =============================================================================

# Variables are declared
# Variables that maintain access to the loop or parts within
exitScript = False
specifiedData = False

# Variables that save information on which interval filter are active or inactive
filterActive = False
filterTemp = False
filterGrowth = False
filterID = False

# Specific variables that contain data values in relation to filtering
xLowerTemp = 0
xUpperTemp = 0
xLowerGrowth = 0
xUpperGrowth = 0
bacteriaID = 0

statisticsStrings = np.array(["1","mean temperature","2","mean growth rate","3","std temperature","4","std growth rate","5","rows","6","mean cold growth rate","7","mean hot growth rate"])

# =============================================================================
# A loop is initiated that doesn't close until the user specifically closes the program
# @Frederik Ravnborg (s204078)
# =============================================================================
while exitScript == False:
    
    # If there is an active filter, this set of if statements shows which and the intervals/values
    if filterActive == True:
        print("\nA filter is currently applied to the data.")
        
        if filterTemp == True:
            print("Temperature has been filtered by the interval:", xLowerTemp, "< Temperature <", xUpperTemp)
            
        if filterGrowth == True:
            print("Growth rate has been filtered by the interval:", xLowerGrowth, "< Growth rate <", xUpperGrowth)
            
        if filterID == True:
            print("Bacteria type has been filtered to only include bacteria", bacteriaID)

    # Presents the user with options
    print(" ","You have the following options:"," ", "1) Load data from file","2) Apply filter to data", "3) Generate statistics from file data","4) Generate data plots from file data","5) Quit the program",sep='\n')
    
    # Only show "Remove filters" if an active filter is currently set to true
    if filterActive == True:
        print("6) Remove filters")
    print("\nPlease type what you want to do:")
    
    # Choice contains the input that correlates to what the user wants to access
    choice = input()
    choice = choice.lower()
    print(" ")
    
    # Choice number 1 - calls the dataLoad function
    if choice == "1" or choice == "load data" or choice == "load data from file":
        
        print("Please input the name of the file you want to load:")
        
        # Name of file the user wants to access, requires entering the filetype
        name = input()
        print(" ")
        
        # Changes specifiedData to record that data has been selected
        specifiedData = True
        
        # Stores the data so the functions can access it later
        data = dataLoad(name)
    
    
# =============================================================================
# Interval code:
# @Lachlan Houston (s214593)
# =============================================================================
    # Choice number 2 - applies a filter to the data
    elif choice == "2" or choice == "filter" or choice == "apply filter to data":
    
        #Checks whether data has been loaded
        if specifiedData == True:
            
            # Variables for interval selecting
            length = len(data)
            numberofRemovals = 0
            
            strings = np.array(["Temperature","Growth rate","Bacteria type"])

            while (True):
                
                # A loop that takes an input, and checks the validity of the input. The input must be convertable into an int
                while (True):
                    print("You have the option to create filters based on the following types of data:","1) Temperature","2) Growth rate","3) Bacteria type","\nPlease choose one:", sep='\n')
                    
                    try:
                        choiceofData = input()
                        choiceofDataInt = int(choiceofData) - 1
                        
                    except ValueError:
                        print("An incorrect input was given, please try again"," "," ",sep='\n')
                        
                    else:
                        try:
                            print("You have chosen to filter by " + strings[choiceofDataInt] + ".")
                            break
                        
                        except IndexError:
                            print("An incorrect input was given, please try again"," "," ",sep='\n')
                
                # If the input equals to either 1 or 2, an interval on either temperature or growth rate has been selected
                while (True):
                    if choiceofData == "1":
                        
                        try:
                            # Ask for lower limit in interval
                            print("Please select desired lower limit")
                            xLowerTemp = float(input())
                            print("Lower limit: " + str(xLowerTemp) + "\nPlease selected desired upper limit")
                            
                            # Ask for upper limit in interval
                            xUpperTemp = float(input())
                            print("Upper limit: " + str(xUpperTemp))
                            
                            print("Your interval has been set to", xLowerTemp, "< data <", xUpperTemp)
                        except ValueError:
                            print("An incorrect input was given, please try again"," "," ",sep='\n')
                            
                        else:
                            filterTemp = True
                                    
                            
                            # Creating a for loop that goes through each row
                            for i in range(length):
                            
                            # Removing rows with data outside the given interval
                                if data.loc[i,choiceofDataInt] < xLowerTemp or data.loc[i,choiceofDataInt] > xUpperTemp:
                                    data = data.drop(i,axis=0)
                                    numberofRemovals += 1
                                    
                            data = data.reset_index(drop=True)
                            print("A total of", numberofRemovals, "rows have been removed from the dataset, and " + str(length - numberofRemovals) + " remain.")
                            filterActive = True
                            break
                        
                    elif choiceofData == "2":
                        
                        try:
                            # Ask for lower limit in interval
                            print("Please select desired lower limit")
                            xLowerGrowth = float(input())
                            print("Lower limit: " + str(xLowerGrowth) + "\nPlease selected desired upper limit")
                            
                            # Ask for upper limit in interval
                            xUpperGrowth = float(input())
                            print("Upper limit: " + str(xUpperGrowth))
                            
                            print("Your interval has been set to", xLowerGrowth, "< data <", xUpperGrowth)
                        
                        except ValueError:
                            print("An incorrect input was given, please try again"," "," ",sep='\n')
                            
                        else:
                            filterGrowth = True
                                    
                            
                            # Creating a for loop that goes through each row
                            for i in range(length):
                            
                            # Removing rows with data outside the given interval
                                if data.loc[i,choiceofDataInt] < xLowerGrowth or data.loc[i,choiceofDataInt] > xUpperGrowth:
                                    data = data.drop(i,axis=0)
                                    numberofRemovals += 1
                                    
                            data = data.reset_index(drop=True)
                            print("A total of", numberofRemovals, "rows have been removed from the dataset, and " + str(length - numberofRemovals) + " remain.")
                            filterActive = True
                            break
                        
                    # If the input equals 3, a interval based on bacteria type has been selected    
                    elif choiceofData == "3":
                        bacteriaID = 0
                        
                        # A loop that breaks when a correct input has been given (1,2, or 3)
                        # while filterID == False:
                            
                        # Checks whether the input is convertable into an integer
                        print("Please input the Bacteria type number")
                        try:
                            bacteriaID = int(input())
                            
                        except ValueError:
                            print("You have entered an incorrect input, please try again")
                            
                        else:
                            if bacteriaID <= 4 and bacteriaID >= 1:
                                
                                # Sets filterID so loop breaks
                                filterID = True
                                
                                # Creating a for loop that goes through each row
                                for i in range(length):
                                    if data.loc[i,choiceofDataInt] != bacteriaID:
                                            data = data.drop(i,axis=0)
                                            numberofRemovals += 1
                            
                                print("A total of", numberofRemovals, "rows have been removed from the dataset, and " + str(length - numberofRemovals) + " remain.")
                                
                                filterActive = True
                                break
                            
                            else:
                                print("You have entered an incorrect input, please try again")
                
                # Resets the data matrix to avoid future key errors
                data = data.reset_index(drop=True)
                break
                
                break
            
        elif specifiedData == False:
            print("A data file has not yet been input, please begin by loading data (Option 1)")

    

# =============================================================================
# dataStatistics code:
# @Lachlan Houston (s214593)
# =============================================================================
    # Choice number 3 - calls the dataStatistics function
    elif choice == "3" or choice == "statistics" or choice == "generate statistics from file data":
        
        # Checks if data has been loaded yet
        if specifiedData == True:
            print("\nPlease select the data that you'd like to calculate. You have the option of selecting the following: \n1) Mean Temperature \n2) Mean Growth rate \n3) Std Temperature \n4) Std Growth rate \n5) Rows \n6) Mean Cold Growth rate \n7) Mean Hot Growth rate")
            
            # Statistics is defined as an empty string
            statistic = input()
            statistic = statistic.lower()
            
            # Checks if the results equal 0, as if this is the case means the data frame is empty
            if dataStatistics(data, statistic) == 0:
                print("The data could not be calculated from the data given, please try again")
                
            else:
                print("The result is:", dataStatistics(data, statistic))

        # If data has not been loaded, the loop restarts
        elif specifiedData == False:
            print("A data file has not yet been input, please begin by loading data (Option 1)")
    
        
# =============================================================================
# dataPlot + End Program code:
# @Frederik Ravnborg (s204078)
# =============================================================================
    # Choice number 4 - calls the dataPlot function
    elif choice == "4" or choice == "plots" or choice == "generate data plots from file data":
        
        # Checks if data has been loaded yet
        if specifiedData == True:
            dataPlot(data)
            print("Generate data plots from file data has been selected\n\nThe first plot shows how many of each bacteria type there is in the dataset.\nThe second plot shows graphs representing growth rate by temperature for each selected bacteria type.")

        # If data has not been loaded, the loop restarts
        elif specifiedData == False:
            print("A data file has not yet been input, please begin by loading data (Option 1)")
        
    # Choice number 5 - ends the program
    elif choice == "5" or choice == "quit" or choice == "quit the program":
        
        # Changes exitScript to True and therefore closes the loop and ends the program
        print("Ending program.")
        exitScript = True
    
    
# =============================================================================
# Remove filters code:
# @Frederik Ravnborg (s204078)
# =============================================================================
    # Choice number 6 - removes any filters    
    elif choice == "6" or choice == "remove" or choice == "remove filters":
        
        # Checks if data has been loaded yet
        if specifiedData == True and filterActive == True:
            
            # Imports the data again to remove filters
            data = dataLoad(name)
            filterActive = False
            filterTemp = False
            filterGrowth = False
            filterID = False
            
            print("\nAll filters have been removed from the data")
            
        # If data has not been loaded or if there is no filter active, the loop restarts
        elif specifiedData == False or filterActive == False:
            print("There is no filter to remove, please select another option")
        
    else:
        print("An incorrect input was given, please try again")
