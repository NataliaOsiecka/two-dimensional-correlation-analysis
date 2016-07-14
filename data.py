# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:16:50 2016
IR data are loaded from the csv file.
Temperature information are reading from the txt file.
@author: Natalia
"""

import numpy
import re

filetxt = "6ba12_01.txt"

#load IR data from the file
def load_data(filename):
    csvarray = numpy.loadtxt(fname = filename, delimiter = ',')   
    intensity, wavenumber = cut_data(csvarray[:,1:], csvarray[:,0]) 
    return wavenumber, intensity
    
#taking data only in the region of near infrared    
def cut_data(intensities, wavenumbers):
    low_index = lower_index(wavenumbers,600)
    high_index = higher_index(wavenumbers,3500)
    new_intens = intensities[low_index:high_index,:]
    new_wavenu = wavenumbers[low_index:high_index]
    return new_intens, new_wavenu
    
#finding the index of data of the lower value of wavenumber in near infrared regon   
def lower_index(wavenumber_vector, number):
    wavenumber_list = list(wavenumber_vector)
    for item in wavenumber_list:
        if item > number:
            return wavenumber_list.index(item)
            
#finding the index of data of the higer value of wavenumber in near infrared regon           
def higher_index(wavenumber_vector, number):
    wavenumber_list = list(wavenumber_vector[::-1])
    for item in wavenumber_list:
        if item < number:
            return len(list(wavenumber_vector)) - wavenumber_list.index(item)
         
#load temperature file, and use regular expresion (number.number) to get temperature data
def load_temp(filename):
    #reading all data from temperature file
    with open(filename, 'r') as f:
        temp_data = f.read().splitlines()
    assert f.closed
    #extracting only information with temperature
    temperature = []
    for item in temp_data:
        if line_start_with_no(item):
            temperature_value = get_temp_value(item)
            for item in temperature_value:
                temperature.append(float(item))
    return temperature[::-1]
      
def line_start_with_no(string_temp_data):
    pattern = r"no"
    if re.match(pattern, string_temp_data):
        return True
    else: 
        return False
        
def get_temp_value(string_temp_data):
    pattern = r'\b(\d+\.\d+)\b'
    return re.findall(pattern, string_temp_data)

def get_submatrix(temp1, temp2, temperature, spectra):
    temp = temperature[::-1]
    index2 = len(temp) - temp.index(temp1)
    index1 = len(temp) - temp.index(temp2)
    sub_matrix = spectra[index1:index2, :]
    return sub_matrix