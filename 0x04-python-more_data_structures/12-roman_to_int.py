#!/usr/bin/python3
import roman


def roman_to_int(roman_string):
    if roman_string is not str(roman_string) or roman_string is None:
        return 0
    return (roman.fromRoman(roman_string))
