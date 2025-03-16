import random

def get_random_math_problem(max_value=100):
    """
    Generates a random math problem of the form "What is the value of x in the equation:
    3x + 5 = 20"
    :param max_value: The maximum value that x can take
    :return: A string representing the math problem
    """
    x = random.randint(1, max_value)
    equation = "What is the value of x in the equation: 3x + 5 = {}".format(20 - (x * 3 + 5))
    return equation
