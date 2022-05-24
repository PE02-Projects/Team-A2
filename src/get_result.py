from filter import *
from save_xlsx import *
from total_plot import *
import time
import warnings
warnings.filterwarnings('ignore')

mid_files, final_files = [], []
coord_list = []
wafer_list = ['D07', 'D08', 'D23', 'D24']

for row in range(-4, 5):
    for column in range(-4, 5):
        coord_list.append(str(row)+','+str(column))

wafer_num = list(map(str, input('Insert desired wafer number in the form of "D00" (Ex. D07 D08...) : ').split()))
for selected_wafer in wafer_num:
    if selected_wafer in wafer_list:
        for file in LMZ_files:
            if selected_wafer in file:
                mid_files.append(file)
    else:
        print(f'Error : {selected_wafer} not in data..')
print(mid_files)
coord = list(map(str, input('Insert desired coordinate in the form of "row,column" (Ex. -1,0/1,1/...) : ').split('/')))
for selected_coord in coord:
    for mid_file in mid_files:
        if selected_coord in coord_list:
            if selected_coord in mid_file:
                final_files.append(mid_file)

        elif selected_coord == 'all':
            for all_coord in coord_list:
                if all_coord in mid_file:
                    final_files.append(mid_file)
        else:
            print(f'Error : ({selected_coord}) not in data..')

print(final_files)
start_time = time.time()

make_xlsx(final_files)

for final_file in final_files:
    print(load_data(final_file))
    save_plot(final_file)

run_time = time.time() - start_time
print(run_time)
