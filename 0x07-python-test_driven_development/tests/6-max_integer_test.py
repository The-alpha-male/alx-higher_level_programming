#!/usr/bin/python3
'''
tis module contains a function that finds the biggest integer of a list
'''

def max_integer(list=[]):
    """Find the max integer in a list
    Args:
        list (list): list to find max integer of
    Returns:
        int: max integer
    """
    if len(list) == 0:
        return None
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max


    
