#!/usr/bin/env python3

"""contains  type-annotated function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to create and return a function that multiplies a float.
    """
    def multiply(n: float) -> float:
        """Function that multiplies a float by multiplier.
        """
        return n * multiplier
    return multiply
