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
from find_nearest_class import findNearestClass

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
#while i < 1:
    obstacle_data_current = df.iloc[i, 4:]
    true_class = int(df.iloc[i, 2])
    speed = df.iloc[i, 3]
    detectedHt = classifier_cluster(obstacle_data_current)
    detectedHt = int(detectedHt)
    detectedClass = findNearestClass(detectedHt)
    #print("Ht. found = " + str(detectedHt) + ", and class found = " + str(detectedClass) + ", True class = " + str(true_class))
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

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

y_true = raw_results[:, 2]
y_pred = raw_results[:, 4]
target_names = ['NO Obstacle', 'SM', 'MD', 'LG']
print(classification_report(y_true, y_pred, target_names=target_names))


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import itertools
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

CM = confusion_matrix(y_true, y_pred)
plot_confusion_matrix(CM, [0,1,2,3])
plt.show()
print(CM)
