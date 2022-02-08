# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:31:27 2022

@author: bhupendra.singh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

import constants
from classifier_cluster import classifier_cluster
from find_nearest_class import findNearestClass
from prepare_results import prepareResults
from filter_data import *

fileName = constants.DATA_SET_FOLDER + "/distanceData.csv"

obstacle_data = np.array(constants.READINGS_PER_SAMPLE)
obstacle_data_all_cases = np.array((constants.TOTAL_EXPERIMENTS, constants.READINGS_PER_SAMPLE))

df = pd.read_csv(fileName)
obstacle_data_all_cases = df.iloc[:, 4:]

raw_results = np.zeros((constants.TOTAL_EXPERIMENTS, 6))

i = 0
while i < constants.TOTAL_EXPERIMENTS:
# while i < 2:
    obstacle_data_current = df.iloc[i, 4:]
    true_class = int(df.iloc[i, 2])
    speed = df.iloc[i, 3]

    ##### Process the current obstacle data array here #########
    # if( i < 276):
    #     i += 1
    #     continue
    #obstacle_data_current = butterworth_filtering(obstacle_data_current, 3, 0.1)
    obstacle_data_current = obstacle_data_current.tolist()
    obstacle_data_current = [x for x in obstacle_data_current if x != 0]
    obstacle_data_current = np.array(obstacle_data_current)

    zeroed_handled = adjust_zero_reading(obstacle_data_current)
    filtered = savgol_filter(obstacle_data_current, 45, 2)
    
    # plot_original_vs_filtered_data(obstacle_data_current, zeroed_handled)
    # #plt.plot(obstacle_data_current, "+")
    # #plt.plot(filtered, ".")
    # plt.show()
    # #exit()
    # obstacle_data_current = filtered
    ######## Processing complete       #########

    detectedHt = classifier_cluster(obstacle_data_current)
    detectedHt = int(detectedHt)
    print(detectedHt)
    detectedClass = findNearestClass(detectedHt)
    print("i = " + str(i+1) + "found = " + str(detectedClass) + " true = " + str(true_class))
    #print("Ht. found = " + str(detectedHt) + ", and class found = " + str(detectedClass) + ", True class = " + str(true_class))
    raw_results[i, 0] = i + 1
    raw_results[i, 1] = speed
    raw_results[i, 2] = true_class
    raw_results[i, 3] = detectedHt
    raw_results[i, 4] = detectedClass
    if( true_class == detectedClass ):
        raw_results[i, 5] = 1
    else:
        raw_results[i, 5] = 0
    i += 1
#plt.plot(obstacle_data_current)
#plt.show()

column_names = list()
column_names.append('Experiment No.')
column_names.append('Speed')
column_names.append('True Class')
column_names.append('Detected Height') 
column_names.append('Detected Class') 
column_names.append('Classification Result') 

df = pd.DataFrame(raw_results, columns = column_names)
#print(len(column_names))

df.to_csv(constants.RESULTS_FOLDER + '/raw_results.csv', index=False)

y_true = raw_results[:, 2]
y_pred = raw_results[:, 4]

classes = ['NO Obstacle', 'SM Obstacles', 'MD Obstacles', 'LG Obstacles']
prepareResults(y_true=y_true, y_pred=y_pred, target_names=classes)