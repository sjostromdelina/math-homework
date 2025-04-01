def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def square_root(num):
    if num >= 0:
        return num ** 0.5
    else:
        raise ValueError("Cannot find a square root of a negative number")

# Example usage:
result = add_numbers(2, 3)
print(result)

multiply_result = multiply_numbers(4, 6)
print(multiply_result)

try:
    divide_result = divide_numbers(4, 0)
except ValueError as e:
    print(e)

square_root_result = square_root(-1)
print(square_root_result)
