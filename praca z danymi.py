# import os
# import time
#
# # a = C:\Users\maxym\Desktop\Python
# # b = testowy_doc.txt
# while True:
#     adress = input('podaj sciezke')
#
#     if (os.path.isdir(adress)) is False:
#         print('this is not directory')
#     else:
#         print('directory correct')
#         file = input('podaj nazwe pliku')
#         path = os.path.join(adress,file)
#         if not os.path.isfile(path):
#             print('this is not good doc name')
#         else:
#             print(f'this is correct file name {path}')
#             print(f'''displaying properties of file {path}
# Lat modified date {time.localtime(os.path.getmtime(path))}
# Size in bytes = {os.path.getsize(path)}
# Current directory is : {os.getcwd()}
# Relative path to the file is {os.path.relpath(path)}
# ''')
#             break
#
# #
# ZADANIE 2

# import os
# import datetime
#
# data_input_catalog = r'C:\Users\maxym\Desktop\inputy\input_catalog'
# data_output_catalog = r'C:\Users\maxym\Desktop\inputy\output_catalog'
# today = datetime.date.today()
# print(today)
# today = today.strftime("%Y-%m-%d")
# today_output_catalog = os.path.join(data_output_catalog,today)
# print(today_output_catalog)
# is_input_catalog = os.path.isdir(data_input_catalog) #1 check
# print(is_input_catalog)
# is_output_catalog = os.path.isdir(data_output_catalog)
# print(is_output_catalog)  #2 check
# is_today_output_catalog = not(os.path.isdir(today_output_catalog)) and \
#                           not (os.path.isfile(today_output_catalog))
# print(is_today_output_catalog) #3 check
# if is_output_catalog  and is_input_catalog and is_today_output_catalog:
#     print('conditions met lets go')
# else:
#     if is_today_output_catalog is False:
#         print('error with today catalog')
#     elif is_output_catalog is False:
#         print('error with output catalog')
#     elif is_input_catalog is False:
#         print('error with input catalog')
#
# # ZADANIE 3
#
import os

file_path = r'C:\Users\maxym\Desktop\inputy\input_catalog\apteka.txt'

with open(file_path, "r") as file:
    for line in file:

        line = line.replace('\n', '')
        print(line)
        order = line.split(',')

        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)

print("Processing finished")

