#!/usr/bin/env python3


""" asynchronous python """


import time
from asyncio import gather


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute async_comprehension four times
    in parallel using asyncio.gather, measure_runtime
    should measure the total runtime and return it
    Args: none
    Return:
        measured_time: float
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end = time.time()
    measured_time = (end - start)
    return measured_time
