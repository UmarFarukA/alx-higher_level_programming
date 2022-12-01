#!/usr/bin/python3
import sys
count = 0
n = len(sys.argv)
for i in range(1, n):
    count += 1
if count == 0:
    print("{} arguments.".format(count))
elif count == 1:
    print("{} argument:".format(count))
    print("{}: {}".format(count, sys.argv[count]))
else:
    print("{} arguments:".format(count))
    for j in range(1, n):
        print("{}: {}".format(j, sys.argv[j]))
