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
import ploting as pl

filecsv = "6ba12_01.csv"
filetxt = "6ba12_01.txt"

wavenumber, intensity = data.load_data(filecsv)
#transpose intensity matrix for ploting the data
trans_int = intensity.T

int_baseline = crt.baseline(trans_int)
intensity_without_co2 = crt.removeCO2band(int_baseline, wavenumber)

temperature = data.load_temp(filetxt)

moving_window_analysis, mw_temperature = cor.calculate_moving_window_analysis(intensity_without_co2, temperature)
synchronous_spectra = cor.calculate_synchronous_spectra(intensity_without_co2)
asynchronous_spectra = cor.calculate_asynchronous_spectra(intensity_without_co2)

#pl.irplot(wavenumber,intensity_without_co2)
#pl.contourplot(wavenumber, synchronous_spectra)
#pl.contourplot(wavenumber, asynchronous_spectra)
pl.moving_window_plot(wavenumber, mw_temperature, moving_window_analysis)
