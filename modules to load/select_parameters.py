# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:02:35 2015

@author: cafolla
"""


""" Interactive module to set desired parameters """

def select_parameters():

    # access the folder where the files are stored
    import os
    old = os.getcwd()
    folder = r"../"
    os.chdir(folder)

    n = 0
    while n == 0:
        filename = "allparameters.txt"
        print("Default parameter file is", filename)
        question1 = input("Press y to confirm file. Press c to change it [y/c]: ")
        if question1 == "y":
            print("You are going to use default parameters from ",filename) 
            break
            n=1
      
        if question1 == "c":
            gino = 0
            while gino == 0:
                filequestion = (raw_input("Do you want to access another existing txt file or create a new one?\n" +\
                "Type c for create, e for existing file [c/e]: "))
                if filequestion == "c":
                    q = 0
                    while q == 0:
                        try:
                            filtername = raw_input("Type filename for the filter: ")
                            q = 1
                        except IOError:
                            print("No such file: ", filtername)
                    w = 0
                    while w == 0:
                        try:
                            spectraltype = float(raw_input("Type spectral type: "))
                            w = 1
                        except ValueError:
                            print("This is not a number")
                    l = 0
                    while l == 0:
                        try:
                            mV = float(raw_input("Type visual magnitude: "))
                            l = 1
                        except ValueError:
                            print("This is not a number")
        
                    st = 0
                    while st == 0:
                        try:
                            startrange = int(raw_input("Type start point for the region of interest of the spectra to analyse: "))
                            st = 1
                        except ValueError:
                            print("This is not a number")
                    er = 0
                    while er == 0:
                        try:
                            endrange = int(raw_input("Type end point for the region of interest of the spectra to analyse: "))
                            er = 1
                        except ValueError:
                            print("This is not a number")
                    ar = 0
                    while ar == 0:
                        try:
                            arrsize = int(raw_input("Type size of the array on which to interpolate they data: "))
                            ar = 1
                        except ValueError:
                            print("This is not a number")
                    s = 0
                    while s == 0:
                        try:
                            skyfile = raw_input("Type filename for the sky flux: ")
                            s = 1
                        except IOError:
                            print("No such file")
                    at = 0
                    while at == 0:
                        try:
                            atmofile = raw_input("Type filename for the atmosphere: ")
                            at = 1
                        except IOError:
                            print("No such file")
                    t = 0
                    while t == 0:
                        try:
                            telefile = raw_input("Type filename for the telescope: ")
                            t = 1
                        except IOError:
                            print("No such file")
                    anakin = 0
                    while anakin == 0:
                        try:
                            pbfiltername= raw_input("Type filename for the pb filter: ")
                            anakin = 1
                        except IOError:
                            print("No such file")
                    obiwan = 0
                    while obiwan == 0:
                        try:
                            fudgefactor= float(raw_input("Type fudge factor for other optics:"))
                            obiwan = 1
                        except ValueError:
                            print("This is not a number")
                    exp = 0
                    while exp == 0:
                        try:
                            expostime= float(raw_input("Type exposure time: "))
                            exp= 1
                        except ValueError:
                            print("This is not a number")
                    dia = 0
                    while dia == 0:
                        try:
                            diameter = float(raw_input("Type telescope diameter: "))
                            dia = 1
                        except ValueError:
                            print("This is not a number")
                    se = 0
                    while se == 0:
                            try:
                                seeingvalue = float(raw_input("Type seeing: "))
                                se = 1
                            except ValueError:
                                print("This is not a number")
                    qe = 0
                    while qe == 0:
                        try:
                            quantumeff = float(raw_input("Type quantum efficiency: "))
                            qe = 1
                        except ValueError:
                            print("This is not a number")
                    st2 = 0
                    while st2 == 0:
                        try:
                            startrange2 = int(raw_input("Type start point for the detector q. efficiency area different from zero:"))
                            st2 = 1
                        except ValueError:
                            print("This is not a number")
                    er2 = 0
                    while er2 == 0:
                        try:
                            endrange2 = int(raw_input("Type end point for the detector q. efficiency area different from zero: "))
                            er2 = 1
                        except ValueError:
                            print("This is not a number")
                    vb = 0
                    while vb == 0:
                        try:
                            vbessel = raw_input("Type filename to substitute the v bessel one: ")
                            vb = 1
                        except IOError:
                            print("No such file")
                    um = 0
                    while um == 0:
                        try:
                            umag = raw_input("Type filename with the data of the u mag object: ")
                            um = 1
                        except IOError:
                            print("No such file")
                    gm = 0
                    while gm == 0:
                        try:
                            gmag = raw_input("Type filename with the data of the g mag object: ")
                            gm = 1
                        except IOError:
                            print("No such file")
                    rm = 0
                    while rm == 0:
                        try:
                            rmag = raw_input("Type filename with the data of  the r mag object: ")
                            rm = 1
                        except IOError:
                            print("No such file")
                    im = 0
                    while im == 0:
                        try:
                            imag = raw_input("Type filename with the data of the i mag object: ")
                            im = 1
                        except IOError:
                            print("No such file")
                    zm = 0
                    while zm == 0:
                        try:
                            zmag = raw_input("Type filename with the data of  the r mag object: ")
                            zm = 1
                        except IOError:
                            print("No such file")
                    print('Parameters need to be saved in a new parameter file \n')


                    print('Parameters need to be saved in a new parameter file \n')


                    print('Parameters need to be saved in a new parameter file \n')

                    filename = raw_input("\nType the name for the paramenter file  (no extension required):  ")
                    filename = filename +'.txt'                   
                    new_param = open(filename, 'w')
                    new_param.write('# Filter data\n' + filtername + '\n\n' +\
                            '# Spectra data: spectral type and visual magnitude\n'+str(spectraltype) + '\n' +\
                            str(mV) + '\n\n' + '# Startpoint of spectra region of interest to analyse\n' +\
                            str(startrange) + '\n\n'+ '# Endpoint of spectra region of interest to analyse\n' + \
                            str(endrange) + '\n\n' + '# Size of the array on which o interpolate spectra and filter, and the other data\n' +\
                            str(arrsize) + '\n\n' + '# Sky background noise\n' + skyfile + '\n\n' +\
                            '# Passing through the atmosphere effect data\n' + atmofile + '\n\n' +\
                            '# Bouncing around telescope effect data\n' + telefile + '\n\n' +\
                            '# Pass band filtername\n' + pbfiltername + '\n\n' +\
                            '# Telescope fudge factor for other optics\n' + str(fudgefactor)+ '\n\n' +\
                            '# Exposure time in seconds\n'+ str(expostime)+ '\n\n' +\
                            '# Diameters in meters\n'+ str(diameter)+ '\n\n' +\
                            '# Seeing, FWHM in arcseconds \n'+ str(seeingvalue)+ '\n\n' +\
                            '# Detector quantum efficiency\n'+ str(quantumeff)+ '\n\n' +\
                            '# Start point for the detector region where quantum efficiency  is different from zero:\n'+\
                            str(startrange2)+ '\n\n' +\
                            '# End point for the detector region where quantum efficiency  is different from zero:\n'+\
                            str(endrange2)+ '\n\n' +'# V Bessel filter\n' + str(vbessel)+ '\n\n' +\
                            '# u mag file\n' + str(umag)+ '\n\n' +\
                            '# g mag file\n' + str(gmag)+ '\n\n' +\
                            '# r mag file\n' + str(rmag)+ '\n\n' +\
                            '# i mag file\n' + str(imag)+ '\n\n' +\
                            '# z mag file\n' + str(zmag)+ '\n\n' )
                    new_param.close()
                    print("You are going to use parameters from the new txt file called", filename)
                    gino = 1
                    break   
                                       
                    
                if filequestion == "e":
                    ex_file = 0
                    while ex_file == 0:
                        try:
                            filename= raw_input("Type the parameter file name you wish to use: ")
                            print("File chosen is ", filename)
                            
                              
                            ex_file = 1
                            gino = 1
                            break 
            
                        except IOError:
                            print("No such file")
            n = 1
            break 
#                    
#                else:
#                    print("Incorrect input. Try again! \n")
#                        
                
        else:
            print('\nIncorrect input. Try again! \n')
           
        
    os.chdir(old)
    return filename


