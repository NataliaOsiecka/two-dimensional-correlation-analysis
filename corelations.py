# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:37:59 2016

@author: Natalia
"""

import data
import correction as crt
import numpy

filecsv = "6ba12_01.csv"

wavenumber, intensity = data.load_data(filecsv)
#transpose intensity matrix for ploting the data
trans_int = intensity.T

int_baseline = crt.baseline(trans_int)
intensity_without_co2 = crt.removeCO2band(int_baseline, wavenumber)

def calculate_synchronous_spectra(spectra):
    dynamic_spectrum = calculate_dynamic_spectra(spectra)
    synchronous = (1/spectra.shape[0])*numpy.dot(dynamic_spectrum, numpy.transpose(dynamic_spectrum))
    return synchronous
    
def calculate_asynchronous_spectr(spectra):
    dynamic_spectrum = calculate_dynamic_spectra(spectra)
    hilbert_matrix = calculate_hilbert_matrix(spectra.shape[0])
    asynchronous = (1/spectra.shape[0])*numpy.dot(numpy.dot(numpy.transpose(dynamic_spectrum),hilbert_matrix), dynamic_spectrum)
    return asynchronous

def calculate_moving_window_analysis(spectra, temperature):
    pass

def calculate_dynamic_spectra(spectra):
    matrix = spectra.sum(axis=1).reshape(spectra.shape[0],1)
    dynamic_spectrum = spectra - (1/spectra.shape[0])*matrix*numpy.ones(spectra.shape[1])
    return dynamic_spectrum
    
def calculate_hilbert_matrix(number_of_spectra):
    hil = numpy.zeros((number_of_spectra, number_of_spectra))
    for i in range(1, number_of_spectra):
        for j in range(i):
            hil[i,j] = 1/(numpy.pi*(j-i))
            hil[j,i] = -hil[i,j]
    return hil