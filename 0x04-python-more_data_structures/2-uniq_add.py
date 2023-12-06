#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    my_list: list of integers

    Return: sum of all unique integers in the list"""
    unique_integers = set(my_list)
    return sum(unique_integers)

