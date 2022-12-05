#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = my_list[0]
    if len(my_list) == 0:
        return (None)
    for j in range(1, len(my_list)):
        if my_list[j] > mx:
            mx = my_list[j]
    return (mx)
