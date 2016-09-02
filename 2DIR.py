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
phase = data.get_submatrix(109.0, 103.1, temperature, intensity_without_co2)

moving_window_analysis, mw_temperature = cor.calculate_moving_window_analysis(intensity_without_co2, temperature)
synchronous_spectra = cor.calculate_synchronous_spectra(phase)
power_spectra_syn = cor.calculate_power_spectra_syn(synchronous_spectra)
power_spectra_mw = cor.calculate_power_spectra_mw(105.0, mw_temperature, moving_window_analysis)
#asynchronous_spectra = cor.calculate_asynchronous_spectra(phase)

#pl.irplot(wavenumber,intensity_without_co2)
#pl.contourplot(wavenumber, synchronous_spectra)
#pl.contourplot(wavenumber, asynchronous_spectra)
#pl.moving_window_plot(wavenumber, mw_temperature, moving_window_analysis)
pl.power_spectra_plot(wavenumber, power_spectra_syn, power_spectra_mw)
