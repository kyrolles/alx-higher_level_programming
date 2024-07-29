#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = dict(sorted(a_dictionary.items()))
    for a in s:
        print(f"{a}: {s[a]}")
