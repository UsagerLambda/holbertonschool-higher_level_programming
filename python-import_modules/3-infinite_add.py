#!/usr/bin/python3
import sys

if __name__ == "__main__":
    nb_args = len(sys.argv) - 1
    args = sys.argv[1:]
    result = 0

for arg in args:
    result += int(arg)
print(result)

