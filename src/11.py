import random

def get_random_code():
    code = []
    for i in range(10):
        code.append(random.randint(0, 9))
    return "".join(str(x) for x in code)