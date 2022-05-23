from extract import *
from IV_data import *
from Tm_data import *
import pandas as pd


def make_xlsx(file_list):
    b = []
    for file in file_list:
        a = [load_data(file)[0], load_data(file)[1], load_data(file)[2], load_data(file)[3], load_data(file)[4],
             load_data(file)[5], load_data(file)[6], load_data(file)[7], load_data(file)[8], load_data(file)[9],
             rsq_ref(file), max_min_ref(file)[0], max_min_ref(file)[1], rsq_iv(file),
             cur_pm_1V(file)[0], cur_pm_1V(file)[1]]
        b.append(a)

    df = pd.DataFrame(np.array(b),
                      columns=['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', "Operator", "Row", "Column",
                               "Analysis Wavelength(nm)", "Rsq of Ref.spectrum(6th)", "Max transmission of Ref spec(dB)",
                               "Min transmission of Ref spec(dB)", "Rsq of IV", "I at -1V[A]", "I at 1V[A]"])

    with pd.ExcelWriter("./res/xlsx_files/Analysis_Result_A2.xlsx") as writer:
        df.to_excel(writer)
