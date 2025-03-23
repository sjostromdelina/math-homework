def add_numbers(a, b):
    """
    Adds two numbers.
    
    Args:
        a: The first number.
        b: The second number.
        
    Returns:
        The sum of a and b.
    """
    return a + b

def subtract(numbers, num1, num2):
    """
    Subtracts one number from another.
    
    Args:
        numbers: A list or tuple of numbers.
        num1: The first number to subtract.
        num2: The second number to subtract.
        
    Returns:
        The result of the subtraction.
    """
    return [number1 - num2 for number1 in numbers]

def multiply(numbers):
    """
    Multiplies all the numbers in a list or tuple by 5.
    
    Args:
        numbers: A list or tuple of numbers.
        
    Returns:
        A new list with each element multiplied by 5.
    """
    return [number * 5 for number in numbers]

def divide(numbers, num1, num2):
    """
    Divides one number by another and returns the result.
    
    Args:
        numbers: A list or tuple of numbers.
        num1: The numerator of the division operation.
        num2: The denominator of the division operation.
        
    Returns:
        The quotient of num1 divided by num2.
    """
    return [number / num2 for number in numbers]

def factorial(num):
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
        num: A non-negative integer to calculate the factorial of.
        
    Returns:
        The factorial of the given number.
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def is_even(num):
    """
    Checks if a number is even using the modulo operator.
    
    Args:
        num: A non-negative integer to check for evenness.
        
    Returns:
        True if the given number is even, otherwise False.
    """
    return num % 2 == 0

def main():
    # Example usage
    print("Sum of numbers:", add_numbers(1, 2))
    print("Subtraction: ", subtract([5, 3], 4, -2))
    print("Multiplication result:", multiply([3, 6]))
    print("Division: ", divide([8, 10], 2, 5))
    print("Factorial of 5:", factorial(5))
    print("Is even number 7:", is_even(7))

if __name__ == "__main__":
    main()
