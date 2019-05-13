# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:32:16 2015

@author: cafolla
"""
import numpy as np
from fundconstants import *
from reader import reader


""" Module to simulate an MKID observation """

def simulatekid(spectra, expostime, sky, filename, output,default_exptime =True):

    """Takes as input the initial spectra, 
        the exposure time in seconds,
        the sky spectra,
        the name of the file, where all the parameters are,
        if default_exptime = True uses the exposure time in the parameter file,
        otherwise that inserted in the input.
        outpt=1 returns SNR; output = 3 returns SNR, photons and skyphotons"""
                 
        
    # import the parameters from the parameter file 
    filtername, spectraltype, mV,  startrange, endrange, arrsize, skyfile,\
                atmofile, telefile, pbfiltername, fudgefactor, exposure_time, diameter,\
                seeingvalue, quantumeff, startrange2, endrange2, vbessel, umag, gmag,\
                rmag,imag,zmag  = reader(filename)
    
    # if default_exptime = True uses the exposure time in the parameter file,
    # otherwise that inserted in the input.
    if default_exptime == True:
        expostime = exposure_time 
        
    wavelength = np.arange(arrsize) * 1E-8 # wavelength in cm
    kidQE = np.zeros(arrsize) 
    kidQE[startrange2:endrange2] = quantumeff

    # compue photons from spectra and convert into ergs/Angstrom 
    photons = spectra * np.pi * expostime * (diameter*50.0)**2   
    photons = photons * kidQE # take into account QE of the device
    photons = photons * wavelength / (h*c)
    tphot = np.sum(photons)

    # Compute sky background and convert into ergs/Angstrom
    skyphotons = sky* np.pi *expostime * (diameter*50.0)**2 * np.pi * (seeingvalue/2.0)**2 
    skyphotons = skyphotons * kidQE # takes into account QE of the device
    skyphotons = skyphotons *wavelength/ (h*c)
    tsky = np.sum(skyphotons)

    SNR = tphot/np.sqrt(tsky)
    if  tphot < 10 :
        SNR = 0.0

    # select desired output
    if output == 3:
        return SNR, photons,skyphotons
    if output == 1:
        return SNR
