# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import data
import matplotlib.pyplot as plt

from data import filecsv

def removeCO2band(intensity_matrix):
    

def main():
    wavenumber, intensity = data.load_data(filecsv)
    #transpose intensity matrix for ploting the data
    trans_int = intensity.T

    #ploting IR spectra
    for item in trans_int:
        plt.plot(wavenumber, item)
    plt.show()
    
if __name__=="__main__":
    main()