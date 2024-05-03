#!/usr/bin/env python3

""" contains a type-annotated function (sum_list)
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of a list of floats.
    """
    sum = 0.0

    for num in input_list:
        if isinstance(num, float):  # if type(num) is float:
            sum += num

    return sum
