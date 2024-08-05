#!/usr/bin/env python3
"""
Multiple coroutines
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines at same time
    """
    times = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n))
    )
    return sorted(times)
