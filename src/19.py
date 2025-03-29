import math

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        area = length * width
        perimeter = 2 * (length + width)
        print(f"Rectangle: Area={area}, Perimeter={perimeter}")
    elif shape == "circle":
        radius = dimensions[0]
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print(f"Circle: Area={area}, Circumference={circumference}")
    else:
        print("Invalid shape")

# Example usage
dimensions = [5, 3]  # Rectangle dimensions
calculate_area("rectangle", dimensions)
