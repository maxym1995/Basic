#zad 1 wrapper
# import time
#
# def wrapper_time(a_function):
#     def a_wrapped_function(*args, **kwargs):
#         time_start = time.time()
#         v = a_function(*args, **kwargs)
#         time_stop = time.time()
#         print(">>>>>Function {} executed in {}".format(a_function.__name__, time_stop - time_start))
#
#         return v
#
#     return a_wrapped_function
#
# def get_sequence(n):
#     if n <= 0:
#         return 1
#     else:
#         v = 0
#         for i in range(n):
#             v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
#         return v
#
# print(get_sequence(22))
# wrapper_get_sequence = wrapper_time(get_sequence)
# print(wrapper_get_sequence(18))

#wrapery cd

import os
import functools
import datetime

def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'C:\Users\maxym\Desktop\Python\wrapery_zadania\dummy_file.txt')
delete_file(r'C:\Users\maxym\Desktop\Python\wrapery_zadania\dummy_file.txt')
create_file(r'C:\Users\maxym\Desktop\Python\wrapery_zadania\dummy_file.txt')
delete_file(r'C:\Users\maxym\Desktop\Python\wrapery_zadania\dummy_file.txt')

def wrapper_with_log_file(logged_action,log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(log_file_path,'a')
            file.write()
            file.write()