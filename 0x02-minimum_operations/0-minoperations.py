#!/usr/bin/python3
"""
Calculates the minimum operations needed.
"""


def minOperations(n):
    """
    This is a method that calculates the fewest number of 
    operations needed to result in exactly n H characters 
    in the file.
        Args: if n is impossible to achieve
        Return: 0
    """
    if n <= 0:
        return 0
    num_h = 1
    num_ops = 0
    while num_h < n:
        num_ops += 1
        num_h *= 2
    if num_h == n:
        return num_ops
    else:
        return 0
