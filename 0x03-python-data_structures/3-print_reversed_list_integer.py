#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return ""
    my_list.sort(reverse=True)
    for i in my_list:
        print("{:d}".format(i))
