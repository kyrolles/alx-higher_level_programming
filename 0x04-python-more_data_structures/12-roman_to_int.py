#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str(roman_string) or roman_string is None:
        return 0
    Rom_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    result = 0
    for i in range(len(roman_string)):
        if i > 0 and Rom_map[roman_string[i]] > Rom_map[roman_string[i-1]]:
            result += Rom_map[roman_string[i]] - 2*Rom_map[roman_string[i-1]]
        else:
            result += Rom_map[roman_string[i]]

    return result
