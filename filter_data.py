import scipy.signal as signal
from scipy.signal import savgol_filter
import constants

import matplotlib.pyplot as plt
import numpy as np
import random

def butterworth_filtering(input_signal, filter_order = 3, cutoff_frequency = 0.5):
    #obstacle_data_current = savgol_filter(obstacle_data_current, 25, 4)    
    B, A = signal.butter(filter_order, cutoff_frequency, output='ba')
    filtered_signal = signal.filtfilt(B,A, input_signal)
    return filtered_signal
    # plt.plot(obstacle_data_current,'r-')
    # plt.plot(smooth_data,'b-')
    # plt.show()

def savgol_filtering(input_signal, window_size = 9, poly_order = 2):
    filtered_signal = savgol_filter(input_signal, window_size, poly_order)
    return filtered_signal

def filter_zero_reading(original):
    filtered = original.copy()
    for i in range(0, len(original)):
        if(int(original[i]) == 0):
            #print(i)
            if(i == 0):
                i = 1   # To avoid division by zero error, if the first data is 0
            filtered[i] = np.sum(filtered[:i])/len(filtered[:i])
    return filtered

def plot_original_vs_filtered_data(original, filtered):

    plt.figure(figsize=(10, 4))

    times = np.arange(len(original))
    plt.subplot(121)
    plt.plot(times, original)
    plt.title("Original Obstacle Data")
    plt.margins(0, .05)

    plt.subplot(122)
    plt.plot(times, filtered)
    plt.title("Filtered Obstacle Data")
    plt.margins(0, .05)

    plt.tight_layout()
    plt.show()