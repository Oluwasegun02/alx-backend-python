#!/usr/bin/env python3

''' Type Checking
Use mypy to validate the following piece of code and apply any necessary changes.
'''

from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    zoomed_in: Tuple[int, ...] = tuple(
        item
        for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
