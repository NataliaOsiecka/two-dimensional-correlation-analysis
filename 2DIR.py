# -*- coding: utf-8 -*-
"""
Natalia

This is a script file for calculating two dimensional correlation analysis.
Data are loaded from the csv file.
Corrections are applied.
Moving window analysis is made.
Synchronous and asynchronous spectra are calculated.
"""
import numpy
import matplotlib.pyplot as plt

filecsv = "6ba12_01.csv"

#load IR data from the file
def load_data(filename):
    csvarray = numpy.loadtxt(fname = filename, delimiter = ',')   
    intensity, wavenumber = cut_data(csvarray[:,1:], csvarray[:,0]) 
    return wavenumber, intensity
    
#taking data only in the region of near infrared    
def cut_data(intensities, wavenumbers):
    low_index = lower_index(wavenumbers,500)
    #high_index = high_index(wavenumbers,3500)
    new_intens = intensities[low_index:,:]
    new_wavenu = wavenumbers[low_index:]
    return new_intens, new_wavenu
    
    
def lower_index(some_vector, number):
    some_list = list(some_vector)
    for item in some_list:
        if item > number:
            return some_list.index(item)

wavenumber, intensity = load_data(filecsv)


#transpose intensity matrix for ploting the data
trans_int = intensity.T

#ploting IR spectra
for item in trans_int:
    plt.plot(wavenumber, item)
    
plt.show()
