import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse of a right-angled triangle given the lengths of the two perpendicular sides.
    
    Parameters:
    a (float): The length of the first side.
    b (float): The length of the second side.
    
    Returns:
    float: The length of the hypotenuse.
    """
    c = math.sqrt(a**2 + b**2)
    return c

# Example usage
side1 = 3.0
side2 = 4.0
print("Hypotenuse:", calculate_hypotenuse(side1, side2))
