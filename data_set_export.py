# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:31:27 2022

@author: bhupendra.singh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

htSmObs = 10
htMdObs = 20
htLgObs = 40

fileName = 'VI_mannual_test_dataset.csv'
datasetFolder = "./dataset"

total_experiments = 360
df = pd.read_csv(fileName)

experiment_number = 1
index = experiment_number
df_new = pd.DataFrame() 
dataList = np.zeros((total_experiments, 2002))
#while experiment_number < 360: 
while experiment_number < total_experiments:
    index = 2*experiment_number
    obstacle_type = int(df.iloc[1, index])
    speed = df.iloc[2, index]
    #expData = df.iloc[3:2003, index].astype(str).astype(int)
    data = df.iloc[3:2003, index]
    #data = [i for i in data if i != 0]
    experiment_number += 1 
    dataList[experiment_number-1, 0] = obstacle_type
    dataList[experiment_number-1, 1] = speed
    dataList[experiment_number-1, 2:] = data
#df = pd.DataFrame(dataList)
#plt.clf()
#plt.plot(dataList[:][10],"+")
#plt.show()
#
#def window(size):
#    return np.ones(size)/float(size)
#
#average = np.convolve(data, window(30), 'same')
#
#plt.plot(average)
#
#plt.plot(dataList[:][0])

dict = {'Obstacle Type': obstacle_type, 'Speed': speed, 'Data': data} 
df = pd.DataFrame(dict)
  
# saving the dataframe
df.to_csv(datasetFolder + '/distanceData.csv')

#### Exporting the plots of the obstacle distance files
i = 0
while i < total_experiments:
    print(i)
    plt.clf()
    plt.plot(dataList[i, 2:], "+")
    if( int(dataList[i, 0]) == 0 ):
        directory = "NO"
    if( int(dataList[i, 0]) == 1 ):
        directory = "SM"
    if( int(dataList[i, 0]) == 2 ):
        directory = "MD"
    if( (dataList[i, 0]) == 3 ):
        directory = "LG"
    plt.savefig(datasetFolder + '/plots/' + directory + "/" + str(i+1) +'.png')
    i = i + 1