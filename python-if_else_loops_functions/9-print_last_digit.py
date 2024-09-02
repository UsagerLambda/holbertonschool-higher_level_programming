#!/usr/bin/python3
def print_last_digit(number):
    i = abs(number) % 10
    print(f"{i}", end='')
    return i
