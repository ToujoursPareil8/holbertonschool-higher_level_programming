#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """ A function to print a reversed list """
    for i in reversed(my_list):
        print("{:d}".format(i))