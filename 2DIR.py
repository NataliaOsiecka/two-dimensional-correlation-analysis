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
import corelations as cor
import matplotlib.pyplot as plt
import numpy as np

filecsv = "6ba12_01.csv"
filetxt = "6ba12_01.txt"

wavenumber, intensity = data.load_data(filecsv)
#transpose intensity matrix for ploting the data
trans_int = intensity.T

int_baseline = crt.baseline(trans_int)
intensity_without_co2 = crt.removeCO2band(int_baseline, wavenumber)

moving_window_analysis = cor.calculate_moving_window_analysis(intensity_without_co2)
synchronous_spectra = cor.calculate_synchronous_spectra(intensity_without_co2)
asynchronous_spectra = cor.calculate_asynchronous_spectra(intensity_without_co2)
'''
#ploting IR spectra
for item in intensity_without_co2:
    plt.plot(wavenumber, item)
plt.show()
'''
#syn_spectra_image = plt.imshow(synchronous_spectra)
#plt.show()
levels = []
colors = []
X, Y = np.meshgrid(wavenumber, wavenumber)
plt.figure()

if np.min(asynchronous_spectra)<0:
    syn_min = np.min(asynchronous_spectra)
    syn_max = np.max(asynchronous_spectra)
    list1 = [syn_min * i/10 for i in range(1,11)]
    levels = list1[::-1] + [syn_max * i/10 for i in range(11)]
    colors = ['#000066','#000066','#000099','#000099','#0000cc','#0000cc',\
    '#0000ff','#0000ff','#66ccff','w','w','#ff6633','#ff0000','#ff0000','#cc0000',\
    '#cc0000','#990000','#990000','#660000','#660000']
else:
    syn_max = np.max(asynchronous_spectra)
    levels = [syn_max * i/10 for i in range(11)]
    colors = ['w','#ff6633','#ff0000','#ff0000','#cc0000','#cc0000','#990000',\
    '#990000','#660000','#660000']

syn_contourf = plt.contourf(X,Y,asynchronous_spectra, levels, colors=colors)
plt.colorbar(syn_contourf)
plt.xlabel(r'Wavenumber [cm$^{-1}$]')
plt.ylabel(r'Wavenumber [cm$^{-1}$]')
plt.grid()
plt.show()

print(np.max(asynchronous_spectra), np.min(asynchronous_spectra))
'''
X, Y = np.meshgrid(wavenumber, wavenumber)
plt.figure()
syn_cp = plt.contour(X,Y,synchronous_spectra)
plt.colorbar(syn_cp)
plt.xlabel('Wavenumber [cm]')
plt.ylabel('Wavenumber [cm]')
plt.show()
'''