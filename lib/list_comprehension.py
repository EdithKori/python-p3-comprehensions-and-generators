#!/usr/bin/env python3


# lib/list_comprehension.py

def return_evens(int_list):
    """
    Returns a list of all even numbers in int_list using a list comprehension.
    """
    return [num for num in int_list if num % 2 == 0]


def make_exclamation(sentences):
    """
    Returns a new list where each sentence in the input list has an exclamation mark added at the end.
    """
    return [sentence + "!" for sentence in sentences]
