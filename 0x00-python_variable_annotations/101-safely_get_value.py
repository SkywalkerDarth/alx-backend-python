#!/usr/bin/env python3


""" modify a function """


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """value associated with the given key in the dictionary,
    or the default value if the key is not found.
    Args:
        dict
    Return:
        Union(any),
    """
    if key in dct:
        return dct[key]
    else:
        return default
