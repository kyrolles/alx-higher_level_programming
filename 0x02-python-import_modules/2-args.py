#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{} argument: ".format(len(argv)-1))
    elif len(argv) == 0:
        print("{} arguments.".format(len(argv)-1))
    else:
        print("{} arguments: ".format(len(argv)-1))

    i = 1
    arguments = argv[1:]
    for num in arguments:
        print("{}: {}".format(i, num))
        i += 1
