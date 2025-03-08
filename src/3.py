def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def generate_math_homework():
    # Generate a random math problem and solution
    operator = random.choice(["+", "-", "*", "/"])
    num1 = get_random_number(1, 10)
    num2 = get_random_number(1, 10)
    solution = eval(f"{num1} {operator} {num2}")
    return f"What is {num1} {operator} {num2}?"
