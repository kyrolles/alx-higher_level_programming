#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{}\n".format(str(num).zfill(2)), end='')
    else:
        print("{}, ".format(str(num).zfill(2)), end='')
