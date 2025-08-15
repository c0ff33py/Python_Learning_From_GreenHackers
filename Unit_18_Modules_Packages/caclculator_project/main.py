# main.py
"""Main program for Calculator Package"""

from math_tools import add, subtract, multiply, divide
from math_tools import square, square_root,factorial

print("Welcome to Calculator Package!")

# Using basic funcitons
print(f"5 + 3 = {add(5, 3)}")
print(f"9 - 4 = {subtract(9, 4)}")
print(f"7 x 6 = {multiply(7, 6)}")
print(f"8 ÷ 2 = {divide(8, 2)} ")

# Using advanced functions
print(f"Square of 5 = {square(5)}")
print(f"Squae root of 81 = {square_root(81)}")
print(f"Factorial of 5 = {factorial(5)}")





