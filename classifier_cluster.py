# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 20:31:27 2022

@author: bhupendra.singh
"""

def classifier_cluster(obstacle_data):
    import numpy as np
    import matplotlib.pyplot as plt
    import kmeans1d

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

    #plt.plot(obstacle_data, ".", color="blue")
    clusters, centroids = kmeans1d.cluster(obstacle_data, 2)

    idendifiedObstacleHt = abs(centroids[0] - centroids[1])
    return idendifiedObstacleHt
    #plotClusters(obstacle_data=obstacle_data, clusters=clusters)