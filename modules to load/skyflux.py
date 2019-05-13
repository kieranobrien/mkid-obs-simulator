# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:26:10 2015

@author: cafolla
"""
import numpy as np
import os
from reader import reader 

def sky(filename):
    """ Takes as input the name of the file, where all the parameters are, and
    from this takes the sky data file (Palomar data as default choice).
    Returns flux from sky."""
    
    # import the parameters from the parameter file so to use the sky data file
    filtername, spectraltype, mV,  startrange, endrange, arrsize, skyfile,\
                atmofile, telefile, pbfiltername, fudgefactor, expostime, diameter,\
                seeingvalue, quantumeff, startrange2, endrange2, vbessel, umag, gmag,\
                rmag,imag,zmag = reader(filename)
    
    old = os.getcwd()                           # current folder
    folder = r"../data files to load"           # select the data folder
    os.chdir(folder)                            # and go to it
    
    skydata = np.genfromtxt(skyfile)
    skydata_spectra = skydata[:,1] * 2.5 # add 1 mag for Palomar sky 
    
    # debug by plotting skydata
#    plt.figure()
#    plt.plot(skydata[:,0],skydata_spectra)
#    plt.xlabel(" ")
#    plt.ylabel(" ")
#    plt.title("Sky spectrum")
#    plt.show()
 
    return skydata_spectra

    os.chdir(old)                           # return to the original folder
