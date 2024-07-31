#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for num, list in enumerate(my_list):
            if num < x:
                print(f"{list}", end='')
            else:
                break
            i += 1
        print()
        return (i)
    except:
        print("Erro")
