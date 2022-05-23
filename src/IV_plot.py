import xml.etree.ElementTree as etree
import matplotlib.pyplot as plt
from lmfit import Model
from sklearn.metrics import r2_score
from fitting import *

def iv_plot(file):
    # ======================================= Voltage-Current(Raw data) ========================================== #
    plt.subplot(2, 3, 4)
    vol, cur = [], []               # reset the value of Voltage and Current

    xml_file = etree.parse(str(file))     # load xml file
    root = xml_file.getroot()

    for i in root.iter():
        if i.tag == 'Voltage':
            vol = list(map(float, i.text.split(',')))   # if tag name is 'Voltage', save voltage value as list form
        elif i.tag == 'Current':
            cur = list(map(float, i.text.split(',')))   # else if tag name is 'Current', save current value as list form

    plt.plot(vol, list(map(abs, cur)), 'co', label='raw_data')

    # ====================================== Voltage-Current(Fitting) ========================================== #

    Cmodel = Model(IV_Fitting)
    result = Cmodel.fit(list(map(abs, cur)), v=vol, i_s=1, q=1, nk=1, cst=1, v_list=vol, c_list=list(map(abs, cur)))

    r2 = r2_score(list(map(abs, cur)), result.best_fit)

    plt.plot(vol, result.best_fit, '--', label=f'Fitting : r² = {r2}')

    plt.text(-1, result.best_fit[4], str(result.best_fit[4])[:4]+str(result.best_fit[4])[-4:]+'A', weight='bold',
             color='r', horizontalalignment='center', verticalalignment='bottom')
    plt.text(1, result.best_fit[-1], str(result.best_fit[-1])[:6]+'A', weight='bold',
             color='r', horizontalalignment='center', verticalalignment='bottom')

    # ========================================= Setting of graph ================================================ #

    font_axis = {                   # font setting for axis label
        'family': 'monospace',     # font style
        'weight': 'bold',          # font weight
        'size': 10                 # font size
    }

    font_title = {                  # font setting for title
        'family': 'monospace',     # font style
        'weight': 'bold',          # font weight
        'size': 15                 # font size
    }

    plt.title('IV-analysis', fontdict=font_title)       # Write a label with a setting of font_title
    plt.xlabel('Voltage[V]', labelpad=10, fontdict=font_axis)
    plt.ylabel('Current[A]', labelpad=10, fontdict=font_axis)
    plt.xticks(fontsize=10)         # Set the font size of axis value
    plt.yticks(fontsize=10)         # Set the font size of axis value
    plt.yscale('logit')       # Set the y-axis scale to log type
    plt.minorticks_off()
    plt.legend(loc='upper left', ncol=2, fontsize=10)
    plt.grid(True, which='major', alpha=0.5)

    # =========================================================================================================== #
