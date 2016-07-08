# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:37:59 2016

@author: Natalia
"""
import numpy

def synchronous_spectra(spectra):
    matrix = spectra.sum(axis=1).reshape(spectra.shape[0],1)
    dynamic_spectrum = spectra - (1/spectra.shape[0])*matrix*numpy.ones(spectra.shape[1])
    synchronous = (1/spectra.shape[0])*numpy.dot(dynamic_spectrum, numpy.transpose(dynamic_spectrum))
    return synchronous