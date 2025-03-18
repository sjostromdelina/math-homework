import random

def get_random_number(n):
    return random.randint(1, n)

def main():
    num = get_random_number(10)
    print(num)

if __name__ == "__main__":
    main()
