#!/usr/bin/python3


def uppercase(str):
    for s in str:
        # if ord(s) < 90:
        #     print("{}".format(s), end='')
        # else:
        print("{}".format(s if ord(s) < 90 else chr(int(ord(s))-32)), end='')
    print("\n")
