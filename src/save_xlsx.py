from IV_data import *
from Tm_data import *
import pandas as pd
from extract import *
from Create_Folder import *
from error import *
import time
from tqdm import tqdm

def make_xlsx(file_list):
    b = []
    for file in tqdm(file_list, desc='Saving xlsx files '):
        a = [load_data(file)[0], load_data(file)[1], load_data(file)[2], load_data(file)[3], load_data(file)[4],
             load_data(file)[5], load_data(file)[6], load_data(file)[7], load_data(file)[8], ErrorFlag(file),
             Error_description(file), load_data(file)[9], rsq_ref(file), max_min_ref(file)[0], max_min_ref(file)[1],
             rsq_iv(file), cur_pm_1V(file)[0], cur_pm_1V(file)[1]]
        b.append(a)

        time.sleep(0.1)

    df = pd.DataFrame(np.array(b),
                      columns=["Lot", "Wafer", "Mask", "TestSite", "Name", "Date", "Operator", "Row", "Column",
                               "Error Flag", "Error Description", "Analysis Wavelength(nm)", "Rsq of Ref.spectrum(6th)",
                               "Max transmission of Ref spec(dB)", "Min transmission of Ref spec(dB)",
                               "Rsq of IV", "I at -1V[A]", "I at 1V[A]"])

    path = './res/xlsx_files/'+now.strftime('%Y%m%d_%H-%M-%S')
    createFolder(path)

    with pd.ExcelWriter(path+"/Analysis_Result_A2.xlsx") as writer:
        df.to_excel(writer)
