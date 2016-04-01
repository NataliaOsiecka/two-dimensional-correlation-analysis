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
import matplotlib.pyplot as plt
import re

filecsv = "6ba12_01.csv"
filetxt = "6ba12_01.txt"

#load IR data from the file
def load_data(filename):
    csvarray = numpy.loadtxt(fname = filename, delimiter = ',')   
    intensity, wavenumber = cut_data(csvarray[:,1:], csvarray[:,0]) 
    return wavenumber, intensity
    
#taking data only in the region of near infrared    
def cut_data(intensities, wavenumbers):
    low_index = lower_index(wavenumbers,600)
    high_index = len(list(wavenumbers)) - higher_index(wavenumbers,3500)
    new_intens = intensities[low_index:high_index,:]
    new_wavenu = wavenumbers[low_index:high_index]
    return new_intens, new_wavenu
    
    
def lower_index(wavenumber_vector, number):
    wavenumber_list = list(wavenumber_vector)
    for item in wavenumber_list:
        if item > number:
            return wavenumber_list.index(item)
            
def higher_index(wavenumber_vector, number):
    wavenumber_list = list(wavenumber_vector[::-1])
    for item in wavenumber_list:
        if item < number:
            return wavenumber_list.index(item)
         
#load temperature file, and use regular expresion (number.number) to get temperature data
def load_temp(filename):
    with open(filename, 'r') as f:
        temp_data = f.read().splitlines()
    assert f.closed

    temperature = numpy.array([])
    for item in temp_data:
        if line_start_with_no(item):
            #numpy.insert(temperature, get_temp_value(item))
            temperature_value = get_temp_value(item)
            print(temperature_value)
            numpy.append(temperature, temperature_value)
    return temperature
      
def line_start_with_no(string_temp_data):
    pattern = r"no"
    if re.match(pattern, string_temp_data):
        return True
    else: 
        return False
        
def get_temp_value(string_temp_data):
    pattern = r'\b(\d+\.\d+)\b'
    return re.findall(pattern, string_temp_data)
    

wavenumber, intensity = load_data(filecsv)

#transpose intensity matrix for ploting the data
trans_int = intensity.T

temperature = load_temp(filetxt)

#ploting IR spectra
for item in trans_int:
    plt.plot(wavenumber, item)
    
plt.show()
