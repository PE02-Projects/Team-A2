import sys

sys.path.append('./src')

from filter import *
from IV_data import *
from IV_plot import *
from extract import *
from Tm_data import *
from Tm_plot import *


mid_files, final_files = [], []
coord_list = []

for row in range(-4, 5):
    for column in range(-4, 5):
        coord_list.append(str(row)+','+str(column))
# print(LMZ_files)

wafer_num = list(map(str, input('Insert desired wafer number in the form of "D00" (Ex. D07 D08...) : ').split()))
for selected_wafer in wafer_num:
    for file in LMZ_files:
        if selected_wafer in file:
            mid_files.append(file)
        # else:
        #     print(f'Error : {selected_wafer} not in data..')

print(mid_files)

coord = list(map(str, input('Insert desired coordinate in the form of "row,column" (Ex. -1,0/1,1/...) : ').split('/')))
for selected_coord in coord:
    if selected_coord in coord_list:
        for mid_file in mid_files:
            if selected_coord in mid_file:
                final_files.append(mid_file)
            # else:
            #     print(f'Error : ({selected_coord}) not in data..')
print(final_files)

for final_file in final_files:
    print(load_data(final_file))

