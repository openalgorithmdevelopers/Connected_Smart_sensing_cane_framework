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
fileName = dataSetFolder + "/distanceData.csv"

obstacle_data = np.array(2000)
df = pd.read_csv(fileName)
obstacle_data = df.iloc[40, 4:]

from scipy.signal import savgol_filter
#obstacle_data = savgol_filter(obstacle_data, 25, 4)
detectedHt = classifier_cluster(obstacle_data)
detectedClass = findNearestClass(detectedHt)
print("Ht. found = " + str(detectedHt) + ", and class found = " + str(detectedClass))
plt.plot(obstacle_data)
plt.show()