#!/usr/bin/env python3


""" asynchronous python """


from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ function task_wait_random.
    Args:
        max_delay: input from wait_random delay
    Return:
        task: Any
    """
    task = create_task(wait_random(max_delay))
    return task
