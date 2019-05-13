# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:12:04 2015

@author: cafolla
"""

import numpy as np
from reader import reader
import os


""" Module to import the filter and integrate the flux through it """

def loadfilter(filename):
    """ Takes as input the name of the file, where all the parameters are, and
    from this uses the filter data file"""
    
    # import the parameters from the parameter file so to use the filter data file
    filtername, spectraltype, mV,  startrange, endrange, arrsize, skyfile,\
                atmofile, telefile, pbfiltername, fudgefactor, expostime, diameter,\
                seeingvalue, quantumeff, startrange2, endrange2, vbessel, umag, gmag,\
                rmag,imag,zmag = reader(filename)
    
    old = os.getcwd()                           # current folder
    folder = r"../data files to load"           # select the data folder
    os.chdir(folder)                            # and go to it
    
    # load up filter. Default is V filter using data from 
    # hhttp://www.noao.edu/kpno/mosaic/filters/c6026.html                                       
    Vfilter = np.genfromtxt(filtername.strip())
    Vfilter_y = Vfilter[:,1]

    idx = np.where(Vfilter_y < 0)
    if np.prod(np.shape(idx)) != 0: # check that the array is not empty
        if np.min(idx) >= 0:
            Vfilter_y[idx] = 0
    x_values = np.arange(arrsize) # rebin into 1 angstrom bins

    vf = np.interp(x_values, Vfilter[:,0],Vfilter_y/100)
    vf = vf/max(vf) # normalize
    
    # debug below: check the filter by plotting it 
#    plt.figure()
#    plt.plot(Vfilter[:,0],Vfilter[:,1])
#    #plt.plot(Vfilter[:,0],vf, label = "Interpolated data")
#    plt.xlabel("Wavelength (Angstrom)")
#    plt.ylabel("Transmission (%)")
#    plt.legend() 
    
    
    #select the region of interest
    fluxfilt = np.sum(vf[startrange:endrange]) / (endrange-startrange) 
    return vf, fluxfilt

    os.chdir(old)                           # return to the original folder
