#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """function multiplies all values
    of a dictionary by 2
    """
    for i in a_dictionary:
            print("{}: {}".format(i, 2*a_dictionary.get(i)))
