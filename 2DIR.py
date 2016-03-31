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

filecsv = "6ba12_01.csv"

#load data from the file
def load_datacsv(filecsv):
    csvarray = numpy.loadtxt(fname = filecsv, delimiter = ',')
    return csvarray
    
def set_intensity_array(csvarray):
    intensity_matrix = csvarray[1:,:]
    return intensity_matrix
    
csvarray = load_datacsv(filecsv)