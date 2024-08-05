#!/usr/bin/env python3

"""
Asynchronous coroutine that takes in an integer arguements
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay after several seconds
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
