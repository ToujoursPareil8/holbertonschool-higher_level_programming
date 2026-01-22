#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """ A function to print a reversed list """
    for i in range(len(my_list), 0, -1):
        print("{:d}".format(my_list[i-1]))
        