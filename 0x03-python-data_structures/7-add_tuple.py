#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    element_1 = tuple_a + (0, 0)
    element_2 = tuple_b + (0, 0)

    result_1 = 0
    result_2 = 0

    result_1 += element_1[0] + element_2[0]
    result_2 += element_1[1] + element_2[1]

    return (result_1, result_2)
