import xml.etree.ElementTree as etree

def load_data(file):
    wafer, mask, test, name, date, oper, row, col, analysis_wl = [], [], [], [], [], [], [], [], []

    xml_file = etree.parse(str(file))
    root = xml_file.getroot()

    for data in root.iter():
        if data.tag == 'OIOMeasurement':
            date.append(data.get('CreationDate'))
            oper.append(data.get('Operator'))

        elif data.tag == 'TestSiteInfo':
            test.append(data.get('TestSite'))
            wafer.append(data.get('Wafer'))
            mask.append(data.get('Maskset'))
            row.append(data.get('DieRow'))
            col.append(data.get('DieColumn'))

        elif data.tag == 'DesignParameter':
            if data.attrib.get('Name') == 'Design wavelength':
                analysis_wl.append(data.text)

        elif data.tag == 'ModulatorSite':
            name.append(data.find('Modulator').get('Name'))

    return wafer, mask, test, name, date, oper, row, col, analysis_wl