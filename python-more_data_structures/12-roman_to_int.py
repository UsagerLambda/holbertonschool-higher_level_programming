#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    length = len(roman_string)

    if len(roman_string) < 0 or roman_string is None:
        return 0

    for i in range(length):
        value = roman[roman_string[i]]

        if (i + 1 < length and
                roman[roman_string[i]] < roman[roman_string[i + 1]]):
            result -= value
        else:
            result += value

    return result
