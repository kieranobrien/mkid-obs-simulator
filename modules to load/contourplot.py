# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:54:28 2015

@author: cafolla
"""
import numpy as np
import matplotlib.pyplot as plt
from simulkid import simulatekid


def contourplot(spectra, skyvalues, filename):
    """ Takes as inputs:
    the spectra;
    the sky flux;
    and the name of the file where all the parameters are.
    Calculates a contour plot of SNR, magnitude vs exposure time """
    
    SNR = np.zeros((100,100))
    for i in range(0,100,1):
        mag = 20.0 + i/10.0
        for j in range(0,100,1):
            exptime = 1.0 + 60.0*j 
            SNR[i,j] = simulatekid(spectra*10.0**(-0.4*mag), exptime, skyvalues,filename,1, False )
    print(SNR)
    levels = np.array([3,10,20,100])
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.contour(np.arange(100.0), (np.arange(100.0)/10.0+20), SNR, levels)
    ax.set_xlabel('Exposure Time (minutes)')
    ax.set_ylabel("V Magnitude (mag)")
    ax.set_xlim((1, 100))
    ax.set_ylim(28, 20)
    ax.set_xscale('log')
    ax.set_title('Palomar MKID Camera SNR - Pulsar')
    plt.show()

