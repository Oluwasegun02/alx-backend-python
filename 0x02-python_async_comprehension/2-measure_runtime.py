#!/usr/bin/env python3

'''Run time for four parallel comprehensions
'''

import asyncio
from time import perf_counter

async def measure_runtime() -> float:
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    return end_time - start_time

