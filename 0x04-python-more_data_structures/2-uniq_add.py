#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    for x in my_list:
        new_set.add(x)
    total = 0
    for j in new_set:
        total += j
    return (total)
