# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:03:04 2015

@author: cafolla
"""
import numpy as np
from extractorinterpol import extractinterpol
from compabmag import abmag
from photons import calculphotons
from skyflux import sky
from simulkid import simulatekid
from setparameters import *
skyvalues = sky()

import os
from setparameters import skyfile
old = os.getcwd()
folder = r"../files to load"
os.chdir(folder)

def PALKID(nmags):
    
    #start loop over magnitude
    for i in range(0,nmags,1): 
        mag = magvals[i]
        # generate fake spectrum
        spectra = generatorspectra(1.e+6,mag) # flat spectrum, v=20
        print'Recovered sdss u,g,r,i,z = ', abmag(spectra,'umag.txt'),
        abmag(spectra,'gmag.txt'), abmag(spectra,'rmag.txt'),
        abmag(spectra,'imag.txt'), abmag(spectra,'zmag.txt')

        print 'Photons/sec/m^2 in V at the top of the atmosphere= ',
        calculphotons(abmagfilter(spectra,"longer",filtername))
   
       # pass through the atmosphere    
        atmos = extractinterpol(wavelengths*1E8,atmofile )
        #put onto transmission
        atmos = 10**(-1 * atmos/2.5)  
 
        #bounce around the telescope
        
        telescope = extractinterpol(wavelengths*1E8,telefile, 10, (1/100))
        telescope=0.75*interpol_data*0.75*interpol_data
    
        # pass through filter pass-band, including fudge factor for other optics        
        pbfilter= fudgefactor*extractinterpol(wavelengths*1E8,pbfiltername) 

        # convert to ergs/s/cm^2/Hz
        fnu = spectra*pbfilter*telescope*atmos*(wavelengths/1E-8)**2/3E18    

        print 'Photons/sec in V = ', np.pi * 2.5**2 \
        *calculphotons(abmag(atmos*telescope*spectra,"VBessel.txt"))    
        print 'Photons/sec in V from sky= ', np.pi * 2.5**2 \
        *calculphotons(abmag(sky2values*telescope, "VBessel.txt"))    
        print 'Photons in 100sec at instrument in R= ', np.pi * 2.5**2 \
        *calculphotons(abmag(100.*atmos*telescope*spectra,"longer",'mkid_r.dat'))

        # loop over exposure time
        for j in range(0,ntimes-1,1):
            exptime = exptimevals[j]
            #put it together and....
            SNR = simulatekid(spectra*pbfilter*telescope*atmos, 
            exptime, diameter, seeing, skyvalues*pbfilter*telescope,1 ) 

            snrgrid[i,j] =SNR        

        print mag, exptime, SNR