#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list
    if idx < 0:
        return new_list
    elif idx > (len(my_list) - 1):
        return new_list
    else:
        new_list.pop(idx)
        new_list.insert((idx), element)
        return new_list
