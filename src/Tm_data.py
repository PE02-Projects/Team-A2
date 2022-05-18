import xml.etree.ElementTree as etree
import numpy as np
from sklearn.metrics import r2_score


def rsq_ref(x):
    # x is the file directory which glob by the filtering module
    xml_file = etree.parse(x)           # load xml file
    root = xml_file.getroot()           # get root(element) of file

    wl_ref, tm_ref = [], []

    for i in root.iter():
        if i.tag == 'Modulator':
            if i.attrib.get('Name') == 'DCM_LMZC_ALIGN' or i.attrib.get('Name') == 'DCM_LMZO_ALIGN':
                wl_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('L').text.split(',')))
                tm_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))

    fit = np.polyfit(np.array(wl_ref), np.array(tm_ref), 6)
    fit_eq = np.poly1d(fit)
    r2_ref = r2_score(tm_ref, fit_eq(wl_ref))

    return r2_ref

def max_min_ref(x):
    # x is the file directory which glob by the filtering module
    xml_file = etree.parse(x)           # load xml file
    root = xml_file.getroot()           # get root(element) of file

    tm_ref = []

    for i in root.iter():
        if i.tag == 'Modulator':
            if i.attrib.get('Name') == 'DCM_LMZC_ALIGN' or i.attrib.get('Name') == 'DCM_LMZO_ALIGN':
                tm_ref = list(map(float, i.find('PortCombo').find('WavelengthSweep').find('IL').text.split(',')))

    arr_tm = np.array(tm_ref)
    max_ref = np.max(arr_tm)
    min_ref = np.min(arr_tm)

    return max_ref, min_ref
