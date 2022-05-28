import xml.etree.ElementTree as etree
from dateutil.parser import parse


def load_data(file):
    lot, wafer, mask, test, name, date, oper, row, col, analysis_wl = '', '', '', '', '', '', '', '', '', ''

    xml_file = etree.parse(str(file))
    root = xml_file.getroot()

    for data in root.iter():
        if data.tag == 'OIOMeasurement':
            d = str(parse(data.get('CreationDate')))
            date = d[0:4]+d[5:7]+d[8:10]+"_"+d[11:13]+d[14:16]+d[17:19]
            oper = data.get('Operator')

        elif data.tag == 'TestSiteInfo':
            lot = data.get('Batch')
            test = data.get('TestSite')
            wafer = data.get('Wafer')
            mask = data.get('Maskset')
            row = data.get('DieRow')
            col = data.get('DieColumn')

        elif data.tag == 'DesignParameter':
            if data.attrib.get('Name') == 'Design wavelength':
                analysis_wl = data.text

        elif data.tag == 'ModulatorSite':
            name = data.find('Modulator').get('Name')

    return lot, wafer, mask, test, name, date, oper, row, col, analysis_wl
