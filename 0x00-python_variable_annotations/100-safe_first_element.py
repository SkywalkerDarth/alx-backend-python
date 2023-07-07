#!/usr/bin/env python3


""" modify a function """


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the sequence
    Args:
        Ist: sequence(any)

    Return:
        Union: if it exist first element or None if it doesnt exist
    """
    if lst:
        return lst[0]
    else:
        return None
