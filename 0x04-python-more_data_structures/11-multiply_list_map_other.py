#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # new_list = my_list.copy()

    new_list = list(map(lambda n:n*number,my_list))

    # for x,i in enumerate(new_list):
    #     new_list[x] = i * number 

    return new_list

