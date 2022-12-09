#!/usr/bin/python3
def best_score(a_dictionary):
    dic_vals = [v for v in a_dictionary.values()]
    mx = dic_vals[0]
    for j in range(1, len(dic_vals)):
        if mx > dic_vals[j]:
            mx = mx
        else:
            mx = dic_vals[j]
    for k in a_dictionary:
        if a_dictionary[k] == mx:
            return (k)
