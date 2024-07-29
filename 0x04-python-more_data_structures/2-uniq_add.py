#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    my_set = set(my_list)
    result =reduce(lambda a,b:a+b,my_set) 
    return result
