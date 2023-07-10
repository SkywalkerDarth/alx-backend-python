#!/usr/bin/env python3


""" asynchronous python """


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ function to spawn wait_random, n times with specified delay.
    Args:
        max_delay: input from wait_random delay
        n(int): random number
    Return:
        asyn_delay: float
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
