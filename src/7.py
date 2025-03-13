import random
def get_random_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(['+', '-', '*', '/'])
    answer = eval(f'{num1} {op} {num2}')
    return f'What is {num1} {op} {num2}?'