#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1

    for x in range(i, -1, -1):
        print("{:d}".format(my_list[x]))
