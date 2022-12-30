#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    count = 1

    number_of_arg = len(argv) - 1
    if number_of_arg == 0:
        print(f"{number_of_arg:d} arguments.")
    if number_of_arg == 1:
        print(f"{number_of_arg:d} argument:")
    if number_of_arg > 1:
        print(f"{number_of_arg:d} arguments:")
    while count < len(argv):
        print(f"{count:d}: {argv[count]}")
        count += 1
