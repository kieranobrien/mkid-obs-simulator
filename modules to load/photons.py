# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:04:13 2015

@author: cafolla
"""

def calculphotons(mV):
    """Calculates photons/sec/m^2 at the top of the atmosphere from a Vmag"""
    return 3640.0 * 10.0**(-mV/2.5)* 1.51E7 * 0.16