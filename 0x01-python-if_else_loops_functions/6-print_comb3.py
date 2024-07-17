#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(1, 10):
        if num1 == num2:
            continue
        elif num1 > num2:
            continue
        elif num1 == 8 and num2 == 9:
            print("{}\n".format((str(num1)+str(num2)).zfill(2)))
        else:
            print("{}, ".format((str(num1)+str(num2)).zfill(2)), end='')
