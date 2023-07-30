#!/usr/bin/env python3

"""
Async Generator

This module defines a coroutine called `async_generator` that yields random numbers asynchronously.

"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that yields random numbers asynchronously.

    The coroutine loops 10 times, each time asynchronously waiting 1 second,
    then yielding a random number between 0 and 10.

    Returns:
        An asynchronous generator that yields float numbers.

    """

    for _ in range(10):
        
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


