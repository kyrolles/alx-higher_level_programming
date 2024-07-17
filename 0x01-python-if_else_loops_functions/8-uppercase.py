#!/usr/bin/python3
def uppercase(str):
    for s in str:
        print("{}".format(s if ord(s) < 90 else chr(int(ord(s))-32)), end='')
    print("\n")
