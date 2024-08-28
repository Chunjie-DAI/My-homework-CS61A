# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:48:19 2024

@author: Chunjie DAI
"""

def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

print (race(2,3))  # in this case, tortoise passes hare at 8th minutes

# Find positive integers x and y (with y larger than x but not larger than 2 * x) for which either:
#race(x, y) returns the wrong value or
#race(x, y) runs forever