#!/usr/bin/env python3


""" asynchronous python """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ function to wait until max delay time of 10 seconds
    Args:
        max_delay(int): maximum delay time to wait
    Return:
        asyn_delay: float
    """
    async_delay = random.uniform(0, max_delay)
    await asyncio.sleep(async_delay)
    return async_delay
