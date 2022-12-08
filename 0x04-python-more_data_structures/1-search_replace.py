#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return ([my_list[j] = replace if my_list[j] == search for j in range(len(my_list))])
