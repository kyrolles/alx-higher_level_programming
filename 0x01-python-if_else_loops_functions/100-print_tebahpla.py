#!/usr/bin/python3
alpha = 122
while 122 >= alpha > 96:
    print("{}".format(chr(alpha)if alpha % 2 == 0 else chr(alpha - 32)), end='\
')
    alpha -= 1
