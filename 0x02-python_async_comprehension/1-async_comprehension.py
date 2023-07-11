#!/usr/bin/env python3
''' 1. Async Comprehensions
'''
import asyncio
from typing import List

async def async_comprehension() -> List[float]:
    async_generator = __import__('0-async_generator').async_generator
    return [num async for num in async_generator()]

