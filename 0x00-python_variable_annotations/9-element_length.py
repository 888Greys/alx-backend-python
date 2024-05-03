#!/usr/bin/env python3

"""Module that annotates the below function's parameters
"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes a list of strings
    """
    return [(i, len(i)) for i in lst]
