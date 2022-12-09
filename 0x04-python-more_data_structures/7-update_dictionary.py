#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    dict_keys = [k for k in a_dictionary.keys()]
    if key in dict_keys:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return (a_dictionary)
