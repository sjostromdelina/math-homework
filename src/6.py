import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def get_random_operator():
    operators = ["+", "-", "*", "/"]
    return random.choice(operators)

def calculate(left, operator, right):
    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    else:
        return left / right

def get_random_math_expression(max_value):
    left = get_random_number(1, max_value)
    right = get_random_number(1, max_value)
    operator = get_random_operator()
    result = calculate(left, operator, right)
    return "{} {} {} = {}".format(left, operator, right, result)