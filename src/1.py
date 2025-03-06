import random

def get_random_math_problem():
    operation = random.choice(["+", "-", "*", "/"])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operation == "+":
        return f"{num1} {operation} {num2} = ?"
    elif operation == "-":
        return f"{num1} {operation} {num2} = ?"
    elif operation == "*":
        return f"{num1} {operation} {num2} = ?"
    else:
        return f"{num1} {operation} {num2} = ?"
