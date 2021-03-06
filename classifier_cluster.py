# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 20:31:27 2022

@author: bhupendra.singh
"""
import constants
import numpy as np
import matplotlib.pyplot as plt
import kmeans1d

def classifier_cluster(obstacle_data):
    #plt.plot(obstacle_data, ".", color="blue")
    clusters, centroids = kmeans1d.cluster(obstacle_data, 2)

    # ######## Handle if zero readings turns out to be one cluster
    # if(int(centroids[0]) == 0):
    #     centroids[0] = centroids[1]
    # if(int(centroids[1]) == 0):
    #     centroids[1] = centroids[0]
    # ########################################################

    ####### Handle the case for tiny size cluster
    count_arr = np.bincount(clusters)
    print('Cluster 0 = ', count_arr[0])
    print('Cluster 1 = ', count_arr[1])
    if(count_arr[0] < constants.CLUSTER_MIN_SIZE):
        return 0    #As cluster too is tiny, means insignificant ht. of obstacle
    if(count_arr[1] < constants.CLUSTER_MIN_SIZE):
        return 0    #As cluster too is tiny, means insignificant ht. of obstacle
    #exit()
    #####################

    identifiedObstacleHt = abs(centroids[0] - centroids[1])
    print(centroids)
    #plotClusters(obstacle_data=obstacle_data, clusters=clusters)
    return identifiedObstacleHt

# Provide the original data and the clusters obtained on it.
# It will plot the two classes in two colors.
def plotClusters(obstacle_data, clusters):
    obstacle_class_data = np.zeros(len(obstacle_data))
    groud_class_data = np.zeros(len(obstacle_data))

    i = 0
    while i < len(clusters):
        if(clusters[i] == 0):
            #print("0")
            obstacle_class_data[i] = obstacle_data[i]
        else:
            #print("1")
            groud_class_data[i] = obstacle_data[i]
        i += 1

    plt.plot(obstacle_class_data, "+", color="red")
    plt.plot(groud_class_data, ".", color="green")
    plt.show()