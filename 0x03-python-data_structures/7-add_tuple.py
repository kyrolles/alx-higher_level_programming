#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x, y = (tuple_a + (0, 0))[:2]
    z, u = (tuple_b + (0, 0))[:2]
    tuple_c = ((x+z), (y+u))
    return tuple_c
