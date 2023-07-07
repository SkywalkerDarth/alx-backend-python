#!/usr/bin/env python3


""" returns a tuple using a string and an int or float """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that multiplies a float by the given multiplie
    Args:
        multiplier function (float)

    Returns:
        function returns a Callable float "multiplier_func"
    """

    def multiplier_func(number: float) -> float:
        """Multiplies the number by the multiplier

        Args:
            function number: a float

        Returns:
            number * multiplier
        """
        return number * multiplier

    return multiplier_func
