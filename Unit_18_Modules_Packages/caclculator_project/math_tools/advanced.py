# math_tools/ advanced.py
"""Advanced math operations"""

import math

def square(num):
    """Return the square of a number"""
    return num ** 2

def square_root(num):
    """Return the square root of a number"""
    return math.sqrt(num)

def factorial(num):
    """Return the factorial of a number"""
    if num < 0:
        return "❌ Factorial not defined for negative numbers"
    return math.factorial(num)

