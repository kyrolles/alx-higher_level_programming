#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    for char in char_list:
        if char == "c":
            char_list.remove("c")
        elif char == "C":
            char_list.remove("C")
    return ''.join(char_list)
