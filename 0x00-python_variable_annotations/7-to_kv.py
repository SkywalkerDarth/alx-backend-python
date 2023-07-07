#!/usr/bin/env python3


""" returns a tuple using a string and an int or float """


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing the string k and the square of v.
    Args:
        k: string
        v: int or float

    Return:
        k, float(v ** 2)
    """
    return k, float(v ** 2)
