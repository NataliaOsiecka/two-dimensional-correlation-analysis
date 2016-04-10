# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import data
import matplotlib.pyplot as plt
import numpy

from data import filecsv
from scipy import signal

def removeCO2band(intensity_matrix, wavenumber_vector, wavenumberCO2_low = 2100, wavenumberCO2_high = 2500 ):
    co2band_low = data.lower_index(wavenumber_vector, wavenumberCO2_low)
    co2band_high = data.higher_index(wavenumber_vector, wavenumberCO2_high)
    new_matrix = numpy.ones((len(intensity_matrix),co2band_high-co2band_low)).T*intensity_matrix[:,co2band_low]
    some_matrix = new_matrix.T
    intensity_matrix[:,co2band_low:co2band_high] = some_matrix
    return intensity_matrix

"""
def band_baseline(intensity_matrix, wavenumber_vector, co2band_low, co2band_high):
    ab = numpy.zeros(shape=(len(intensity_matrix),2))
    i = 0
    for column in intensity_matrix:
        x = numpy.array([[co2band_low, 1],[co2band_high, 1]])
        print(column)
        y = numpy.array([column(co2band_low), column(co2band_high)])
        ab[i] = numpy.linalg.solve(x,y)
        i += 1
    return ab
"""

def baseline(intensity_matrix):
    indexes = intensity_matrix.shape
    new_matrix = numpy.empty([indexes[0], indexes[1]])
    for index, column in enumerate(intensity_matrix):
        new_matrix[index,:] = signal.detrend(column)
    return new_matrix
        
   
wavenumber, intensity = data.load_data(filecsv)
#transpose intensity matrix for ploting the data
trans_int = intensity.T

int_baseline = baseline(trans_int)
intesity_without_co2 = removeCO2band(int_baseline, wavenumber)



#ploting IR spectra
for item in int_baseline:
    plt.plot(wavenumber, item)
plt.show()
"""
def band_baseline(intensity_matrix, co2band_low, co2band_high):
    ab = numpy.zeros(shape=(len(intensity_matrix),2))
    for column in intensity_matrix:
        x = numpy.array([[co2band_low, 1],[co2band_high, 1]])
        print(column)
        """
"""
def main():
    wavenumber, intensity = data.load_data(filecsv)
    #transpose intensity matrix for ploting the data
    trans_int = intensity.T

    #ploting IR spectra
    for item in trans_int:
        plt.plot(wavenumber, item)
    plt.show()
    
if __name__=="__main__":
    main()
"""