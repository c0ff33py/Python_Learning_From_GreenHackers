# math_tools/basic.py
"""Basic math operations"""

def add(a, b):
    """Return sum of a and b"""
    return a + b

def subtract(a, b):
    """Return difference of a and b"""
    if b > a:
        return b - a
    return a - b 

def multiply(a, b):
    """Return product of a and b"""
    return a * b

def divide(a, b):
    """Return division result of a and b"""
    if b == 0:
        return "❌ cannot divide by zero"
    return a / b