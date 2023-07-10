#!/usr/bin/env python3


""" asynchronous python """


import time
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ function to measure runtime.
    Args:
        max_delay: input from wait_random delay
        n(int): random number
    Return:
        average_time (float)
    """
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
