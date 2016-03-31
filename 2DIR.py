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
def load_datacsv(filename):
    csvarray = numpy.loadtxt(fname = filename, delimiter = ',')
    intensity = csvarray[1:,:]
    wavenumber = csvarray[0,:]
    return intensity, wavenumber
    
intensity, wavenumber = load_datacsv(filecsv)

print(intensity.shape)
intensity.T
print(intensity.shape)

"""
with plt.style.context('fivethirtyeight'):
    for item in intensity:
        plt.plot(wavenumber, item)
    """