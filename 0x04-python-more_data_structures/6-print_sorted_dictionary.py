#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """function prints dictionary
    by ordered keys
    """
    dict_keys = list(a_dictionary)
    dict_keys = sorted(a_dictionary)
    for i in dict_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
