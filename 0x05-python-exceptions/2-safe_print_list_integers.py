#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        indx = 0
        printed = 0
        while printed < x:
            if type(my_list[indx]) is int:
                print("{:d}".format(my_list[indx]), end='')
                printed += 1
            else:
                x -= 1
            indx += 1
        print()
        return printed
    except ValueError:
        return False
