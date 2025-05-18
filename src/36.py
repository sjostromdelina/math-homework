def sum_of_squares(nums):
    """
    Calculate the sum of squares of numbers in a list.
    
    Args:
    nums (list): A list of integers
    
    Returns:
    int: The sum of squares of the numbers in the list
    """
    return sum(num ** 2 for num in nums)

# Example usage:
nums = [1, 2, 3]
result = sum_of_squares(nums)
print("The sum of squares is:", result)
