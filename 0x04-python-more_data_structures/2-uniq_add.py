#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    number_list = list(uniq_set)
    result = sum(uniq_set)
    return result
