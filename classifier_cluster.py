# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 20:31:27 2022

@author: bhupendra.singh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

htSmObs = 10
htMdObs = 20
htLgObs = 40

dataSetFolder = "./dataset"
fileName = dataSetFolder + "/distanceData.csv"

df = pd.read_csv(fileName)
print(df.shape)