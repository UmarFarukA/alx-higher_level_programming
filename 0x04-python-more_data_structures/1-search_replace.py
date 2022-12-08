#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = my_list[:]
    for j in range(len(lst)):
        if lst[j] == search:
            lst[j] = replace
    return (lst)
