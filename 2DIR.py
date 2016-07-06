# -*- coding: utf-8 -*-
"""
Natalia

This is a script file for calculating two dimensional correlation analysis.
Data are loaded from the csv file.
Corrections are applied.
Moving window analysis is made.
Synchronous and asynchronous spectra are calculated.
"""
import data
import correction as crt
import matplotlib.pyplot as plt

filecsv = "6ba12_01.csv"
filetxt = "6ba12_01.txt"

wavenumber, intensity = data.load_data(filecsv)
#transpose intensity matrix for ploting the data
trans_int = intensity.T

int_baseline = crt.baseline(trans_int)
intensity_without_co2 = crt.removeCO2band(int_baseline, wavenumber)


#ploting IR spectra
for item in intensity_without_co2:
    plt.plot(wavenumber, item)
plt.show()

