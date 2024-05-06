#!/usr/bin/env bash

"""
Asynchronous coroutine that takes in an integer
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for some time
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
