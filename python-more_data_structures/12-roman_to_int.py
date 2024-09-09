#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    length = len(roman_string)

    for i in range(length):
        if roman_string[i] not in roman:
            return 0
        value = roman[roman_string[i]]

        if (i + 1 < length and
                roman[roman_string[i]] < roman[roman_string[i + 1]]):
            result -= value
        else:
            result += value

    return result
