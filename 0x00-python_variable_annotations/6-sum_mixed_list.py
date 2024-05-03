#!/usr/bin/env python3

""" contains a type-annotated function (sum_mixed_list)

"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """return the sum of a list of integers and floats.
    """
    mxd_sum = 0.0

    for idx in mxd_list:
        if isinstance(idx, int) or isinstance(idx, float):
            mxd_sum += idx

    return mxd_sum
