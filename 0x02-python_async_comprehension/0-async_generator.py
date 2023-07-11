#!/usr/bin/env python3


""" asynchronous python """


import asyncio
import random


async def async_generator():
    """ function generate rsndom numbers asynchron
    Args: none
    Return:
        asyn_delay: float
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
