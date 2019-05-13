#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fizzbuzz(value):
    """Simple process of fizzbuzz.
    This Documents follow by numpydoc(https://numpydoc.readthedocs.io/en/latest/format.html)

    Parameters
    ----------
    value: int
        Int value, this value will converted by fizzbuzz process

    Returns
    ----------
    fizzbuzz: str
    """

    if value % 15 == 0:
        return "fizzbuzz"
    elif value % 3 == 0:
        return "fizz"
    elif value % 5 == 0:
        return "buzz"
    return str(value)
