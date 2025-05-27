def sum_of_squares(n):
    """
    Calculate the sum of squares of numbers from 1 to n.
    
    Parameters:
        n (int): The upper limit of the range of numbers.
        
    Returns:
        int: The sum of squares of numbers from 1 to n.
    """
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# Example usage and verification (you can replace this with actual code)
print(sum_of_squares(5))  # Output: 55
