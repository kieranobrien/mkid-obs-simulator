# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:04:21 2015

@author: cafolla
"""

' Module to read and import the parameters from the desired txt file'

import os


def reader(filename='allparameters.txt'):
    old = os.getcwd()
    folder = r"../"
    os.chdir(folder)


    # import the parameters from default file
    dictionaryfile = open(filename)
    lines = dictionaryfile.readlines()

    filtername = lines[1].strip()       # wavelength filter, strip removes end of line characters
    spectraltype = float(lines[4])      # spectra data: spectral type
    mV = float(lines[5])                # and visual magnitude

    # startpoint and endpoint of spectra region of interest to analyse
    startrange = int(lines[8])
    endrange = int(lines[11])

    #size of the array on which interpolate the data
    arrsize = int(lines[14])

    skyfile = lines[17].strip()    # default sky background noise
    atmofile = lines[20].strip()   # passing through the atmosphere effect data
    telefile = lines[23].strip()      # bouncing effect around telescope
    pbfiltername = lines[26].strip()  # pass band filtername
    fudgefactor = float(lines[29])   # fudge factor for other optics
    expostime = float(lines[32])    # exposure time in seconds
    diameter = float(lines[35])      # diameters in meters
    seeingvalue = float(lines[38])   # FWHM in arcseconds
    quantumeff = float(lines[41])    # detector quantum efficiency

    # start & end for detector region where quantum eff is not zero:
    startrange2 = int(lines[44])
    endrange2 = int(lines[47])
    
    vbessel = lines[50].strip()         # V Bessel filter
    umag = lines[53].strip()            # u mag data file
    gmag = lines[56].strip()            # g mag data file
    rmag = lines[59].strip()            # r mag data file
    imag = lines[62].strip()            # i mag data file
    zmag = lines[65].strip()            # z mag data file
    
    dictionaryfile.close()
    
    os.chdir(old)

    return  filtername, spectraltype, mV,  startrange, endrange, arrsize, skyfile,\
                atmofile, telefile, pbfiltername, fudgefactor, expostime, diameter,\
                seeingvalue, quantumeff, startrange2, endrange2, vbessel, umag, gmag,\
                rmag,imag,zmag


