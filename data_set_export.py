# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:31:27 2022

@author: bhupendra.singh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import constants

df = pd.read_csv(constants.ORIGINAL_DATASET_FILE_NAME)
#df = pd.read_csv(constants.SIMULATED_DATASET_FILE_NAME)

experiment_number = 1
index = experiment_number
df_new = pd.DataFrame() 
dataList = np.zeros((constants.TOTAL_EXPERIMENTS, 2004))
#while experiment_number < 360: 
while experiment_number <= constants.TOTAL_EXPERIMENTS:
    index = 2*experiment_number
    subject = int(df.iloc[0, index])
    obstacle_type = int(df.iloc[1, index])
    speed = df.iloc[2, index]
    #print(df.iloc[0:4, index])
    print(experiment_number)
    #exit()
    data = df.iloc[3:constants.READINGS_PER_SAMPLE+3, index]
    dataList[experiment_number-1, 0] = experiment_number
    dataList[experiment_number-1, 1] = subject
    dataList[experiment_number-1, 2] = obstacle_type
    dataList[experiment_number-1, 3] = speed
    dataList[experiment_number-1, 4:constants.READINGS_PER_SAMPLE+4] = data
    experiment_number += 1 
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
column_names = list()
column_names.append('SNo.')
column_names.append('Subject No.')
column_names.append('Obstacle Type')
column_names.append('Speed') 
i = 0
while i < constants.READINGS_PER_SAMPLE:
    column_names.append("D" + str(i+1))
    i += 1
df = pd.DataFrame(dataList, columns = column_names)
#print(len(column_names))
#exit()
# saving the dataframe
df.to_csv(constants.DATA_SET_FOLDER + '/distanceData.csv', index=False)

### Exporting the plots of the obstacle distance files
i = 0
while i < constants.TOTAL_EXPERIMENTS:
    print(i)
    #print(int(dataList[i, 2]))
    plt.clf()
    plt.plot(dataList[i, 2:], "+")
    if( int(dataList[i, 2]) == 0 ):
        directory = "NO"
    if( int(dataList[i, 2]) == 1 ):
        directory = "SM"
    if( int(dataList[i, 2]) == 2 ):
        directory = "MD"
    if( int(dataList[i, 2]) == 3 ):
        directory = "LG"
    plt.savefig(constants.DATA_SET_FOLDER + '/plots/' + directory + "/" + str(i+1) +'.png')
    i = i + 1