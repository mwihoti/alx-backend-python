#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
mandatory
"""
import asyncio
from importlib import import_module as use
import time

async_comprehension = use('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
