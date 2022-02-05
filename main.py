# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:31:27 2022

@author: bhupendra.singh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import constants
from classifier_cluster import classifier_cluster
from nearest_class import findNearestClass

dataSetFolder = "./dataset"
resultsFolder = "./results"
fileName = dataSetFolder + "/distanceData.csv"

obstacle_data = np.array(constants.READINGS_PER_SAMPLE)
obstacle_data_all_cases = np.array((constants.TOTAL_EXPERIMENTS, constants.READINGS_PER_SAMPLE))

df = pd.read_csv(fileName)
obstacle_data_all_cases = df.iloc[:, 4:]

from scipy.signal import savgol_filter
#obstacle_data = savgol_filter(obstacle_data, 25, 4)

raw_results = np.zeros((constants.TOTAL_EXPERIMENTS, 5))

i = 0
while i < constants.TOTAL_EXPERIMENTS:
    obstacle_data_current = df.iloc[i, 4:]
    true_class = int(df.iloc[i, 2])
    speed = df.iloc[i, 3]
    detectedHt = classifier_cluster(obstacle_data_current)
    detectedHt = int(detectedHt)
    detectedClass = findNearestClass(detectedHt)
    print("Ht. found = " + str(detectedHt) + ", and class found = " + str(detectedClass) + ", True class = " + str(true_class))
    raw_results[i, 0] = i + 1
    raw_results[i, 1] = speed
    raw_results[i, 2] = true_class
    raw_results[i, 3] = detectedHt
    raw_results[i, 4] = detectedClass
    i += 1
#plt.plot(obstacle_data_current)
#plt.show()

column_names = list()
column_names.append('Experiment No.')
column_names.append('Speed')
column_names.append('True Class')
column_names.append('Detected Height') 
column_names.append('Detected Class') 

df = pd.DataFrame(raw_results, columns = column_names)
print(len(column_names))
#exit()
# saving the dataframe
df.to_csv(resultsFolder + '/raw_results.csv', index=False)