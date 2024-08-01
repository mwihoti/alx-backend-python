#!/usr/bin/env python3
"""
function’s parameters and return values with the appropriate types
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Creates a list of tuples, where each tuple contains a string from
    the given list and its length.
    """
    return [(i, len(i)) for i in lst]
