import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1: Data load Funktion:
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


#print(dataLoad("test.txt"))

# 2: Data statistik funktion:
def dataStatistics(data, statistic):
    

    result = 0
    return result

# 3: Data plot funktion:
#def dataPlot(data):
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

# Designing the plot
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
    
  
# Del, der ikke virker:
data = dataLoad("test.txt")
datanp = np.array(data)
shape = np.shape(datanp)
nr_rows = shape[0]
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


for i in range(shape[0]):
    if datanp[i,2] == 2:
        x2[x] = datanp[i,0]
        y2[x] = datanp[i,1]
        x += 1
        
    if datanp[i,2] == 1:
        x1[y] = datanp[i,0]
        y1[y] = datanp[i,1]
        y += 1
        
    if datanp[i,2] == 3:
        x3[w] = datanp[i,0]
        y3[w] = datanp[i,1]
        w += 1
        
    if datanp[i,2] == 4:
        x4[z] = datanp[i,0]
        y4[z] = datanp[i,1]
        z += 1
        
print(x1,y1)
print(" ")
print(x2,y2)
print(" ")
print(x3,y3)
print(" ")
print(x4,y4)
print(" ")
