# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:37:59 2016

@author: Natalia
"""

import numpy

def calculate_synchronous_spectra(spectra):
    dynamic_spectrum = calculate_dynamic_spectra(spectra)
    synchronous = (1/spectra.shape[0])*numpy.dot(numpy.transpose(dynamic_spectrum), dynamic_spectrum)
    return synchronous
    
def calculate_asynchronous_spectra(spectra):
    dynamic_spectrum = calculate_dynamic_spectra(spectra)
    hilbert_matrix = calculate_hilbert_matrix(spectra.shape[0])
    asynchronous = (1/spectra.shape[0])*numpy.dot(numpy.dot(numpy.transpose(dynamic_spectrum),hilbert_matrix), dynamic_spectrum)
    return asynchronous

def calculate_moving_window_analysis(spectra, temperature):
    moving_window = numpy.zeros((spectra.shape[1], spectra.shape[0]-2))
    mw_temperature = numpy.zeros((moving_window.shape[1]))
    for it in range(spectra.shape[0]):
        if it == 0:
            pass
        elif it == spectra.shape[0] - 1:
            pass
        else:
            window = spectra[it-1:it+2]
            mw_temperature[it-1] = numpy.sum(temperature[it-1:it+2])/3
            syn = calculate_synchronous_spectra(window)
            for i in range(spectra.shape[1]):
                moving_window[i, it-1] = syn[i,i]
    return moving_window, mw_temperature

def calculate_dynamic_spectra(spectra):
    matrix = spectra.sum(axis=0).reshape(spectra.shape[1],1)
    dynamic_spectrum = spectra - numpy.transpose((1/spectra.shape[0])*matrix*numpy.ones(spectra.shape[0]))
    return dynamic_spectrum
    
def calculate_hilbert_matrix(number_of_spectra):
    hil = numpy.zeros((number_of_spectra, number_of_spectra))
    for i in range(1, number_of_spectra):
        for j in range(i):
            hil[i,j] = 1/(numpy.pi*(j-i))
            hil[j,i] = -hil[i,j]
    return hil
    
