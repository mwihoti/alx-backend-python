#!/usr/bin/env python3
"""
coroutine async_comprehension
"""
import asyncio
from typing import List
from importlib import import_module as use

async_generator = use('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers
    """
    return [rad async for rad in async_generator()]   
