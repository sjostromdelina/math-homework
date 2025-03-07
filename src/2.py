from random import randint
import math

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    
    # Determine the operation to perform
    op = ["+", "-", "*", "/"][randint(0, 3)]
    
    # Return the problem in string format
    return f"{num1} {op} {num2} = ?"
