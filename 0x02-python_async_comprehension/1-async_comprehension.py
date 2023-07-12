#!/usr/bin/env python3
"""
Function that returns 10 random numbers using async comprehension like
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension: function to return 10 random numbers
    Arguments:
        no arguments
    Returns:
        10 random numbers
    """
    res = [i async for i in async_generator()]
    return res
