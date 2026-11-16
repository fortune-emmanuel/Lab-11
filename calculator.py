# https://github.com/fortune-emmanuel/Lab-11
# Partner 1: Fortune Emmanuel
# Partner 2: Daniel Ruiz
"""Calculator functions for Lab 11."""

import math


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return b divided by a, as specified in the lab handout."""
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):
    """Return log base a of b; reject invalid bases and arguments."""
    if a <= 0 or a == 1:
        raise ValueError("The logarithm base must be positive and cannot equal 1.")
    if b <= 0:
        raise ValueError("The logarithm argument must be positive.")
    return math.log(b, a)


def exponent(a, b):
    """Return a raised to the power of b."""
    return a ** b


def square_root(a):
    """Return the square root of a; reject negative inputs."""
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    """Return the hypotenuse for legs a and b."""
    return math.hypot(a, b)


# Partner 2's abbreviated function names, retained as aliases for compatibility.
sub = subtract
mul = multiply
div = divide
log = logarithm
exp = exponent
