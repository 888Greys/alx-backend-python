#!/usr/bin/env python3

"""Module that contains a type-annotated function zoom_array
that takes a tuple of integers and returns a tuple of integers
"""


# import Tuple class from the typing module
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """ Change the annotation for 1st and return the type
        to Tuple
        to indicate that the function accepts and
    """
    zoomed_in: Tuple = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
