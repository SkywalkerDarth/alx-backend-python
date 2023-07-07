#!/usr/bin/env python3


""" modify a function """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """list of tuples creator, computes lenght of a list of sequence
    Args:
        Ist: list of string (array)
    Returns:
        list of Tuple(sequence, int)
    """
    return [(i, len(i)) for i in lst]
