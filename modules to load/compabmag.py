# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:06:01 2015

@author: cafolla
"""
import numpy as np 
from setparameters import *
import os

def abmag(spectra,filterfile = filtername): 
    """ Returns the magnitude of a spectrum specified in ergs/s/cm^2/Angstrom.
         If data file is not specified, default Vfilter data will be used"""
         
    old = os.getcwd()                           # current folder
    folder = r"../data files to load"           # select the data folder
    os.chdir(folder)                            # and go to it

    # load up filter. Default is V filter using data from 
    # hhttp://www.noao.edu/kpno/mosaic/filters/c6026.html                                           
    data = np.genfromtxt(filterfile)
    original_x = np.zeros(int(np.shape(data)[0]))
    original_y = np.zeros(int(np.shape(data)[0]))        
    
    idx = np.where(original_y < 0)
    if np.prod(np.shape(idx)) != 0: # check that the array is not empty
        if np.min(idx) >= 0:
            original_y[idx] = 0
 
    x_values = np.arange(arrsize) # rebin into 1 angstrom bins
    vf = np.interp(x_values, original_x,original_y/100)
    vf = vf/max(vf) # Normalize
    
    fluxfilt = np.sum(vf[startrange:endrange])/ (endrange-startrange)
    fluxV = np.sum(vf[startrange:endrange]) * spectra[startrange:endrange]/(endrange-startrange)

    mag = -2.5 * np.log10(fluxV/fluxfilt) - 21.1
    
    return mag

    os.chdir(old)                           # return to the original folder