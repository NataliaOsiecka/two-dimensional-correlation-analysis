# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:41:16 2016

@author: Natalia
"""
import matplotlib.pyplot as plt
import numpy as np

def irplot(wavenumber, spectra):
    for item in spectra:
        plt.plot(wavenumber, item)
    plt.show()
    
def contourplot(wavenumber, spectra):
    levels = []
    colors = []
    X, Y = np.meshgrid(wavenumber, wavenumber)
    plt.figure()
#usually positive peaks are red and negative peaks are blue on syn and asyn spectra
    if np.min(spectra)<0:
        syn_min = np.min(spectra)
        syn_max = np.max(spectra)
        list1 = [syn_min * i/10 for i in range(1,11)]
        levels = list1[::-1] + [syn_max * i/10 for i in range(11)]
        #colors = ['#000066','#000066','#000099','#000099','#0000cc','#0000cc',\
        #'#0000ff','#0000ff','#66ccff','w','w','#ff6633','#ff0000','#ff0000','#cc0000',\
        #'#cc0000','#990000','#990000','#660000','#660000']
        colors = ['#000066','#000066','#000099','#000099','#0000cc','#0000cc',\
        '#0000ff','#0000ff','w','w','w','w','w','#ff0000','#cc0000',\
        '#cc0000','#990000','#990000','#660000','#660000']
    else:
        syn_max = np.max(spectra)
        levels = [syn_max * i/20 for i in range(21)]
        colors = ['w','w','#000080','#000080','#00008b','#00008b',\
        '#0000cd','#0000cd','#0000ff','#191970','#191970','#ff6633','#ff0000','#ff0000','#cc0000',\
        '#cc0000','#990000','#990000','#660000','#660000']

    syn_contourf = plt.contourf(X,Y,spectra, levels, colors=colors)
    plt.colorbar(syn_contourf)
    plt.xlabel(r'Wavenumber (cm$^{-1}$)', fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.xlim(3100,700)
    plt.ylabel(r'Wavenumber (cm$^{-1}$)', fontsize = 16)
    plt.yticks(fontsize = 14)
    plt.ylim(3100,700)
    plt.grid()
    plt.show()
    
def moving_window_plot(wavenumber, temperature, spectra):
    X, Y = np.meshgrid(wavenumber, temperature)
    plt.figure()
    mw_max = np.max(spectra)
    levels = [mw_max * i/100 for i in range(101)]
    plt.contour(X, Y, np.transpose(spectra),levels, colors='black')
    #plt.colorbar(mv_contourf)
    plt.xlabel(r'Wavenumber (cm$^{-1}$)', fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.xlim(3100,700)
    plt.ylabel(r'Temperature (K)', fontsize = 16)
    plt.yticks(fontsize = 14)
    plt.ylim(305,365)
    plt.grid()
    plt.show()
    
def power_spectra_plot(wavenumber, power_spectra_syn, power_spectra_mw):
    plt.plot(wavenumber, power_spectra_syn, 'r--', wavenumber, power_spectra_mw, 'b-.')
    plt.xlabel(r'Wavenumber [cm$^{-1}$]', fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.ylabel(r'Intensity [a. u.]', fontsize = 16)
    plt.yticks(fontsize = 14)
    plt.grid()
    plt.show()