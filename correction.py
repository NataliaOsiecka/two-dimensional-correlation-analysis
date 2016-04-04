# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import data
import matplotlib.pyplot as plt
import numpy

from data import filecsv

def removeCO2band(intensity_matrix, wavenumber_vector, wavenumberCO2_low = 2100, wavenumberCO2_high = 2500 ):
    co2band_low = data.lower_index(wavenumber_vector, wavenumberCO2_low)
    co2band_high = data.higher_index(wavenumber_vector, wavenumberCO2_high)
    ab = band_baseline(intensity_matrix, co2band_low, co2band_high)
    j = 0
    for column in intensity_matrix:
        part_of_column = column[co2band_low:co2band_high]
        for i, each_wavenumber in enumerate(part_of_column):
            each_wavenumber = (i+co2band_low)*ab[j,0] + ab[j,1]
    return intensity_matrix
            


def band_baseline(intensity_matrix, co2band_low, co2band_high):
    ab = numpy.zeros(shape=(len(intensity_matrix),2))
    i = 0
    for column in intensity_matrix:
        x = numpy.array([[co2band_low, 1],[co2band_high, 1]])
        print(column)
        y = numpy.array([column(co2band_low), column(co2band_high)])
        ab[i] = numpy.linalg.solve(x,y)
        i += 1
    return ab
       
wavenumber, intensity = data.load_data(filecsv)
#transpose intensity matrix for ploting the data
trans_int = intensity.T

intesity_without_co2 = removeCO2band(trans_int, wavenumber)

#ploting IR spectra
for item in trans_int:
    plt.plot(wavenumber, item)
plt.show()
