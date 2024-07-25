# Requirements

# 2 inputs, positive, float or integer (is digit)
# 1 output, float
# external library? No external library


# Create a function - calculate hypot = sqrt(a**2 + b**2)
def hypot(a, b):
    """A function that calculates the hypotenuse of a right angle triangle

    Args:
        a (float): one side of triangle
        b (float): the other side of the triangle

    Returns:
        output (float): the hypotenuse of the triangle
    """
    return sqrt(a**2 + b**2)


# Create a square root function : receive a positive number, runs a float
def sqrt(a):
    """Calculate a square root, where negative values are made positive

    Args:
        a (float): Input value

    Returns:
        output (float): square root of absolute of input value
    """
    return abs(a) ** 0.5
