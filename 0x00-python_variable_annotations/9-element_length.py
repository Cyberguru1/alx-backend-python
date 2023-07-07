#!/usr/bin/env python3
"""
Function with annotated parameters and
return values with defined types.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with the length of each elements
    """
    return [(i, len(i)) for i in lst]
