import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score


def tm_plot(x):
    xml_file = etree.parse(x)           # load xml file
    root = xml_file.getroot()           # get root(element) of file

    # setting of font
    font_title = {              # font setting for title
        'family': 'monospace',  # font style
        'weight': 'bold',       # font weight
        'size': 15              # font size
    }

    # ==================================================================================================================== #
    plt.figure(figsize=(20, 10))
    plt.suptitle(x[24:], fontsize=20, weight='bold')
    plt.subplots_adjust(hspace=0.3)
    # ==================================================================================================================== #

    # Wavelength-Transmission(Raw data)
    wl_list, tm_list = [], []
    wl_ref, tm_ref = [], []
    DC_bias = -2.0
    plot_color = ['lightcoral', 'coral', 'gold', 'lightgreen', 'lightskyblue', 'plum']
    color_number = 0

    plt.subplot(2, 3, 1)
    for i in root.iter():
        if i.tag == 'WavelengthSweep':
            if i.attrib.get('DCBias') == str(DC_bias):
                wl = list(map(float, i.find('L').text.split(',')))
                wl_list.append(wl)
                tm = list(map(float, i.find('IL').text.split(',')))
                tm_list.append(tm)
                plt.plot(wl, tm, plot_color[color_number], label=f'DCBias = {DC_bias}V')
                DC_bias += 0.5
                color_number += 1

            plt.title('Transmission spectra - as measured', fontdict=font_title)
            plt.xlabel('Wavelength[nm]', fontsize=10)
            plt.ylabel('Measured transmission[dB]', fontsize=10)
            plt.legend(loc='lower center', ncol=2, fontsize=10)

        # Reference
        elif i.tag == 'Modulator':
            if i.attrib.get('Name') == 'DCM_LMZC_ALIGN' or i.attrib.get('Name') == 'DCM_LMZO_ALIGN':
                wl_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
                tm_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))
                plt.plot(wl_ref, tm_ref, color='#7f7f7f', linestyle=':', label='Reference')
                plt.subplot(2, 3, 2)
                plt.plot(wl_ref, tm_ref, color='#7f7f7f', linestyle=':', label='Reference')

    # Wavelength-Transmission(Fitting)
    rsq_ref = []
    for p in range(2, 7):
        fit = np.polyfit(np.array(wl_ref), np.array(tm_ref), p)
        fit_eq = np.poly1d(fit)
        rsq_ref.append(r2_score(tm_ref, fit_eq(wl_list[0])))
        plt.plot(wl_ref, fit_eq(wl_ref), label=f'{p}th R² : {r2_score(tm_ref, fit_eq(wl_list[0]))}')

    plt.title('Transmission spectra - as measured', fontdict=font_title)
    plt.xlabel('Wavelength[nm]', fontsize=10)
    plt.ylabel('Measured transmission[dB]', fontsize=10)
    plt.legend(loc='lower center', fontsize=10)

    DC_bias = -2.0
    plt.subplot(2, 3, 3)

    for j in range(6):
        plt.plot(wl_ref, tm_ref - fit_eq(wl_ref))
        plt.plot(wl_list[j], tm_list[j] - fit_eq(wl_list[j]), plot_color[j], label=f'DC_bias={DC_bias}')
        DC_bias += 0.5

    plt.title('Flat Transmission spectra - as measured', fontdict=font_title)
    plt.xlabel('Wavelength[nm]', fontsize=10)
    plt.ylabel('Measured transmission[dB]', fontsize=10)
    plt.legend(loc='lower center', ncol=2, fontsize=10)

    plt.show()