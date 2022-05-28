import xml.etree.ElementTree as etree
from sklearn.metrics import r2_score
from lmfit import Model
from fitting import *


def rsq_iv(file):
    vol, cur = [], []

    xml_file = etree.parse(str(file))
    root = xml_file.getroot()

    for i in root.iter():
        if i.tag == 'Voltage':
            vol = list(map(float, i.text.split(',')))
        elif i.tag == 'Current':
            cur = list(map(float, i.text.split(',')))

    Cmodel = Model(IV_Fitting)
    result = Cmodel.fit(list(map(abs, cur)), v=vol, i_s=1, q=1, nk=1, cst=1, v_list=vol, c_list=list(map(abs, cur)))

    r2 = r2_score(list(map(abs, cur)), result.best_fit)

    return r2

def cur_pm_1V(file):
    cur = []

    xml_file = etree.parse(str(file))
    root = xml_file.getroot()

    for i in root.iter():
        if i.tag == 'Current':
            cur = list(map(float, i.text.split(',')))

    minus1 = cur[4]
    plus1 = abs(cur[-1])

    return minus1, plus1
