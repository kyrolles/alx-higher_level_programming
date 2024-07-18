#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    x = 0
    for num in arguments:
        x += int(num)

print("{}".format(x))
