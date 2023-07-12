#!/usr/bin/env python3
"""
Function to measure the execution time of an async ops
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime: Function execute async_com 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the given task
    """
    taskStart = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    taskEnd = time.perf_counter()
    return (taskEnd - taskStart)
