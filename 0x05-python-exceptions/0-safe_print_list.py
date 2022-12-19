#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for j in range(x):
            print(my_list[j], end="")
            count += 1
    except IndexError:
        print("Index error out fo bound")
    return count
