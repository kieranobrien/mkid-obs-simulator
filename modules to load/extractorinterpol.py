# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:57:41 2015

@author: cafolla
"""
import numpy as np

import os


def extractinterpol(x_values, filename, x_multiplier = 1, y_multiplier = 1):
    """Takes a file with x and y values and uses the data to build an 
    interpolated output corresponding to the input x_values
    x and y multipliers allow to modify the original x and y input values."""
    
    old = os.getcwd()                           # current folder
    folder = r"../data files to load"           # select the data folder
    os.chdir(folder)                            # and go to it
    
    data = np.genfromtxt(filename,dtype = None) # load data
    
    if len(np.shape(data))==2:    
        original_x = data[:,0] 
        original_y = data[:,1] 

    # check whether array is made of np.void objects
    if len(np.shape(data)) == 1: 
        original_x = np.zeros(int(np.shape(data)[0]))
        original_y = np.zeros(int(np.shape(data)[0]))
        # loop necessary to deal with an array made of np.void objects
        for k in range(int(np.shape(data)[0])): 
            temp = data[k].item()
            original_x[k] = temp[0]
            original_y[k] = temp[1]    

    interpol_data = np.interp(x_values, original_x * x_multiplier,original_y *y_multiplier)

    return interpol_data

    os.chdir(old)                           # return to the original folder